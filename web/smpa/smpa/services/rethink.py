
# stdlib
import json
import uuid
import arrow
from datetime import datetime, date
from importlib import import_module

# 3rd party
import falcon
import rethinkdb
from slugify import slugify
from typing import List, Any, Optional, Iterable  # NOQA
from rethinkdb.errors import RqlDriverError, RqlRuntimeError, ReqlOpFailedError
from schematics.types.base import UUIDType
from schematics.types.serializable import serializable

# Module
from ..models.core import BaseModel
from ..rdb.connection import RDB_DB, rconnect
from ..helpers.console import console


r = rethinkdb.RethinkDB()


class RService(object):
    """A service that operates on a RethinkDB database. Every database interaction should
    go through a service class instance, then if the backend data store ever changes you
    can simply swap out this service class for a different one with the same method signature.

    Public method signature
        * q : property, the base query
        * get: Return one, by id
        * get_or_404: Return one, by id, otherwise 404
        * count: Count the total
        * all: return all
        * find: return multiple instances that match kwargs
        * first: return one instance that matcges kwargs
        * first_or_404: like first, but returns a 404 instead of None
        * new: create a new, unsaved instance
        * create: create a new SAVED instance
        * update: update an existing instance
        * delete: delete an existing instance
        # TODO
        * last: Get the last created instance
        * save: Save one


    """

    __model__ = BaseModel

    @property
    def q(self):
        """
        Shorthand property for accessing the query property of the model.
        You can also override this on an individual service level, for instance
        if you need to implement soft-deletes on a specific service this could be
        overridden to return self.__model__.query.filter(deleted=True)

        Returns:
            [type]: [description]
        """
        return r.db(RDB_DB).table(self.__model__._table)

    def new(self, *args, **kwargs):
        kwargs = self._preprocess(**kwargs)
        j = self._jsonify(kwargs)
        m = self.__model__()

        for k, v in kwargs.items():
            if hasattr(m, k):
                setattr(m, k, v)

        return m

    def get(self, id: str):
        with rconnect() as conn:
            if id is None:
                raise ValueError

            if isinstance(id, uuid.UUID):
                id = str(id)

            try:
                query = self.q.get(id)
                rv = query.run(conn)
            except ReqlOpFailedError as e:
                console.warn(e)
                raise
            except Exception as e:
                console.warn(e)
                raise
            else:
                if rv is not None:
                    instance = self.__model__(rv)
                    return instance
        return None

    def count(self):
        with rconnect() as conn:
            query = self.q.count()
            return query.run(conn)

    def get_or_404(self, id: str):
        instance = self.get(id=id)
        if not instance:
            raise falcon.HTTPError(falcon.HTTP_404, 'Object not found')

        return instance

    def last(self, **kwargs):
        return self.first(order_by='>created_at', **kwargs)

    def first(self, order_by: Optional[str] = '<created_at', **kwargs):
        """Fetch the first item that matches your filter.
        To set the sorting direction prepend with `<` or `>`

        Args:
            order_by (str, optional): column on which to order the results
            **kwargs: keyword args on which to filter, column=value

        Returns:
            TYPE: Description

        Raises:
            ValueError: Description
        """
        kwargs = self._preprocess(**kwargs)
        with rconnect() as conn:
            try:
                query = self.q
                if order_by is not None:
                    query = self._order_by(query, order_by)

                # NOTE: Always filter before limiting
                if len(kwargs) > 0:
                    query = query.filter(kwargs)
                query = self._limit(query, 1)
                rv = query.run(conn)

            except ReqlOpFailedError as e:
                console.warn(e)
                raise
            except Exception as e:
                console.warn(e)
                raise
            else:
                try:
                    data = [self.__model__(_) for _ in rv]
                    return data[0]
                except IndexError:
                    return None

    def first_or_404(self, order_by: Optional[str] = None, **kwargs):
        kwargs = self._preprocess(**kwargs)
        instance = self.first(order_by=order_by, **kwargs)
        if not instance:
            raise falcon.HTTPError(falcon.HTTP_404, 'Object not found')

        return instance

    def create(self, **kwargs):
        """Creates one or more records from the json data. You can pass json directly to
        the method by using `json` as a keyword arg.

        Args:
            kwargs (dict): The data

        Returns:
            __model__ or list: Single model instance or list of them.
        """
        kwargs = self._preprocess(**kwargs)
        j = self._jsonify(kwargs)

        with rconnect() as conn:
            query = self.q.insert(j)
            rv = query.run(conn)
            data = []
            if 'generated_keys' in rv:
                for _ in rv['generated_keys']:
                    data.append(self.get(_))

            if len(data) > 1:
                return [self.__model__(_) for _ in rv]

            if len(data):
                return self.__model__(data[0])

    def save(self, instance):
        """Saves a specific instance.

        Args:
            instance (BaseModel): A new or existing insance of the model

        Returns:
            {
              u'errors': 0,
              u'deleted': 0,
              u'generated_keys': [u'dd8ad1bc-8609-4484-b6c4-ed96c72c03f2'],
              u'unchanged': 0,
              u'skipped': 0,
              u'replaced': 0,
              u'inserted': 1
            }
        """
        # If this is a new unsaved object, it'll likely have an
        # id of None, which RethinkDB won't like. So if it's None,
        # generate a UUID for it. If the save fails, we should re-set
        # it to None.
        with rconnect() as conn:
            if instance.id is None:
                instance.id = str(uuid.uuid4())
                console.debug(instance.id)

            try:
                query = self.q.insert(
                    instance.to_primitive(),
                    conflict="replace"
                )
                rv = query.run(conn)
                console.debug(rv)
            except Exception as e:
                console.error(e)
                instance.id = None
                raise
            else:
                return instance

    def find(self, order_by: Optional[str] = None, limit: int = 0, **kwargs):
        """
        Find all items that matches your kwargs.
        :param limit: How many rows to fetch.
        :param order_by: column on which to order the results. \
        To change the sort, prepend with < or >.

        Args:
            order_by (str, optional): Column to sort on
            limit (int, optional): Limit your query to this number, 0 = no limit
            **kwargs: The kwargs to search on

        Returns:
            TYPE: Description

        Raises:
            ValueError: Description
        """
        kwargs = self._preprocess(**kwargs)
        j = self._jsonify(kwargs)

        with rconnect() as conn:
            try:
                query = self.q
                if order_by is not None:
                    query = self._order_by(query, order_by)
                if limit > 0:
                    query = self._limit(query, limit)
                query = query.filter(j)
                rv = query.run(conn)
            except Exception as e:
                console.warn(e)
                raise
            else:
                data = [self.__model__(_) for _ in rv]
                return data

    def get_or_create(self, **kwargs):
        """Will return the first instance that matches your kwargs, or
        create a new instance if one is not found.

        Args:
            **kwargs: The params, ie: name="something"
        """
        kwargs = self._preprocess(**kwargs)
        found = self.first(**kwargs)
        if found is not None:
            return found

        new = self.create(**kwargs)
        return new

    def update(self, id, **kwargs):
        """updates a record from the json data

        Args:
            id (uuid): Description
            json (json): The data

        Returns:
            __model__ or list: Single model instance or list of them.
        """
        kwargs = self._preprocess(**kwargs)
        j = self._jsonify(kwargs)

        with rconnect() as conn:
            query = self.q.get(id).update(j, return_changes=True)
            rv = query.run(conn)
            if len(rv['changes']):
                return self.__model__(rv['changes'][0]['new_val'])
            else:
                return self.get(id)

    def all(self, order_by: Optional[str] = None, limit: int = 0):
        with rconnect() as conn:
            try:
                query = self.q
                if order_by is not None:
                    query = self._order_by(query, order_by)
                if limit > 0:
                    query = self._limit(query, limit)
                rv = query.run(conn)
            except Exception as e:
                console.warn(e)
                raise
            else:
                rv = query.run(conn)
                data = [self.__model__(_) for _ in rv]
                return data

    def delete(self, instance: BaseModel):
        """
            Delete an instance from the DB.
        """
        with rconnect() as conn:
            id = str(instance.id)
            try:
                query = self.q.get(id).delete()
                rv = query.run(conn)
            except Exception as e:
                console.warn(e)
                raise
            else:
                return True

    # Private methods - these do not form part of the public API or method signature of the
    # service class.

    def _preprocess(self, **kwargs):
        for k, v in kwargs.items():
            if isinstance(v, uuid.UUID):
                kwargs[k] = str(v)

        return kwargs

    def _restore_uuids(self, **kwargs):
        for k, v in kwargs.items():
            if k.endswith('_id'):
                kwargs[k] = uuid.UUID(v)

        return kwargs

    def _jsonify(self, data):
        """Allows methods to take arbitrary keywords or json

        Args:
            data (dict): Pass your kwargs in here

        Returns:
            json: Get back JSON

        """
        j = data.pop('json', None)
        if isinstance(j, dict):
            return j
        if j is None:
            for k, v in data.items():
                if isinstance(v, datetime) or isinstance(v, date):
                    data[k] = arrow.get(v).isoformat()

            # Create json from kwargs
            j = json.dumps(data)
        return json.loads(j)

    def _order_by(self, query, column):
        if column.startswith('>'):
            index = r.desc(column[1:])
        elif column.startswith('<'):
            index = r.asc(column[1:])
        else:
            index = column

        try:
            rv = query.order_by(index)
        except Exception as e:
            console.warn(e)
            raise
        else:
            return rv

    def _limit(self, query, limit):
        if not isinstance(limit, int):
            raise ValueError('Limit must be an integer')
        try:
            rv = query.limit(limit)
        except Exception as e:
            console.warn(e)
            raise
        else:
            return rv

    def _make_slug(
            self, instance: BaseModel,
            field: Optional[str] = None,
            fields: Optional[List[str]] = None) -> str:
        """
        Make a slug for ``instance`` using ``field`` as the input, or optionally ``fields``,
        useful for when you want to slug on two or more fields like firstname-lastname.

        Args:
            instance (Model): The model instance that we want a slug for
            field (str, optional): Defaults to None. The field to take the input from
            fields (str, optional): Defaults to None. For creating multi field slugs

        Raises:
            ValueError: If the supplied field(s) are None or empty strings

        Returns:
            str: The slug
        """
        if field is not None:
            text = str(getattr(instance, field))
            if text is None or text == '':
                raise ValueError('There was no string to make a slug from')
        elif fields is not None:
            parts = [str(getattr(instance, field)) for field in fields]
            text = '-'.join(parts)
            if text is None or text.replace('-', '') == '':
                raise ValueError('There was no string to make a slug from')

        concrete_slug = slugify(text, to_lower=True)
        slug = concrete_slug
        counter = 1
        while self.q.filter_by(slug=slug).first() is not None:
            slug = '{}-{}'.format(concrete_slug, counter)
            counter += 1
        return slug
