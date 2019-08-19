import uuid
import arrow
import falcon
import pymongo
from bson.objectid import ObjectId
from datetime import datetime, date
import simplejson as json
from slugify import slugify
from typing import List, Any, Optional, Iterable, Dict  # NOQA

from smpa.models.core import BaseModel
from smpa.helpers.console import console


class DService(object):
    """A service that operates on a DocumentDB database. Every database interaction should
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

    def __init__(self):
        self.__model__._service = self

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
        from smpa.app import db
        collection = db[self.__model__._table]
        return collection

    def new(self, *args, **kwargs):
        kwargs = self._preprocess(**kwargs)
        j = self._jsonify(kwargs)
        m = self.__model__()

        for k, v in j.items():
            if hasattr(m, k):
                setattr(m, k, v)

        return m

    def get(self, id: Optional[str] = None, oid: Optional[ObjectId] = None) -> BaseModel:
        if id is None and oid is None:
            raise ValueError('You must supply an id or oid')
        if oid is not None:
            rv = self.q.find_one({'_id': oid})
        else:
            rv = self.q.find_one({'id': str(id)})

        if rv is not None:
            return self._model_out(rv)
        return None

    def get_or_404(self, id: str):
        instance = self.get(id=id)
        if not instance:
            raise falcon.HTTPError(falcon.HTTP_404, 'Object not found')

        return instance

    def first(self, **kwargs):
        """Fetch the first item that matches your filter.

        Args:
            **kwargs: keyword args on which to filter, column=value

        Returns:
            TYPE: Description

        Raises:
            ValueError: Description
        """
        kwargs = self._preprocess(**kwargs)
        rv = self.q.find(kwargs).sort("created_at", pymongo.ASCENDING).limit(1)
        try:
            return self._model_out(rv[0])
        except Exception:
            return None

    def first_or_404(self, **kwargs):
        rv = self.first(**kwargs)
        if not rv:
            raise falcon.HTTPError(falcon.HTTP_404, 'Object not found')

        return rv

    def last(self, **kwargs):
        rv = self.q.find(kwargs).sort("created_at", pymongo.DESCENDING).limit(1)
        return self._model_out(rv[0])

    def create(self, **kwargs):
        """Creates one or more records from the json data. You can pass json directly to
        the method by using `json` as a keyword arg.
        """
        kwargs = self._preprocess(**kwargs)
        j = self._jsonify(kwargs)
        j = self._set_id(j)
        if isinstance(j, list):
            rv = self._insert_some(j)
        else:
            rv = self._insert_one(j)

        return rv

    def save(self, instance: BaseModel):
        """Save an instance.

        Args:
            instance (BaseModel): The model we're saving.
        """
        updating = False
        if instance._id is not None and instance.id is not None:
            updating = True
        data = instance.to_primitive()
        j = self._jsonify(data)
        if j.get('created_at', None) is None:
            j['created_at'] = arrow.now().datetime
        j['updated_at'] = arrow.now().datetime
        j = self._set_id(j)
        if updating:
            j.pop('_id', None)
            self.update(str(instance.id), json=j)
            obj = self.get(instance.id)
            return obj
        try:
            rv = self.q.insert_one(j)
        except Exception as e:
            console.error(e)
        else:
            obj = self.get(oid=rv.inserted_id)
            return obj

    def count(self, **kwargs):
        j = self._jsonify(kwargs)
        return self.q.count_documents(j)

    def all(self, order_by: Optional[str] = None, limit: Optional[int] = None) -> list:
        query = self.q.find({})
        if order_by is not None:
            query = self._order_by(query, order_by)
        if limit:
            query = query.limit(limit)
        rv = [self._model_out(obj) for obj in query]
        return rv

    def valid(self, order_by: Optional[str] = None, limit: Optional[int] = None) -> list:
        query = self.q.find({})
        rv = []
        if order_by is not None:
            query = self._order_by(query, order_by)
        if limit:
            query = query.limit(limit)
        for _ in query:
            try:
                obj = self._model_out(_)
            except Exception as e:
                console.error(e)
            else:
                rv.append(obj)

        return rv

    def invalid(self, order_by: Optional[str] = None, limit: Optional[int] = None) -> list:
        query = self.q.find({})
        rv = []
        if order_by is not None:
            query = self._order_by(query, order_by)
        if limit:
            query = query.limit(limit)
        for _ in query:
            try:
                self.__model__(_)
            except Exception:
                rv.append(_['id'])

        return rv

    def find(self, order_by: Optional[str] = None, limit: Optional[int] = None, **kwargs):
        """
        Find all items that matches your kwargs.
        :param limit: How many rows to fetch.
        :param order_by: column on which to order the results. \
        To change the sort, prepend with < or >.
        """
        kwargs = self._preprocess(**kwargs)
        j = self._jsonify(kwargs)
        query = self.q.find(j)
        if order_by is not None:
            query = self._order_by(query, order_by)
        if limit is not None:
            query = query.limit(limit)

        rv = [self._model_out(obj) for obj in query]
        return rv

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

    def update(self, id: str, **kwargs: dict):
        """updates a record from the json data

        Args:
            id (uuid): Description
            json (json): The data

        Returns:
            __model__: Single model instance
        """
        kwargs = self._preprocess(**kwargs)
        j = self._jsonify(kwargs)
        if isinstance(id, uuid.UUID):
            id = str(id)

        # First validate that the data should be going in by passing it
        # into a schematics model loaded with existing data
        try:
            tmodel = self.get(id)
            for k, v in j.items():
                setattr(tmodel, k, v)
            tmodel.validate()
        except Exception:
            raise

        self.q.update_one({'id': id}, {"$set": j})
        return self.get(id)

    def delete(self, instance: BaseModel):
        """
            Delete an instance from the DB.
        """
        rv = self.q.delete_one({'id': str(instance.id)})
        return rv

    def delete_by_id(self, id: str):
        """
            Delete an instance from the DB.
        """
        rv = self.q.delete_one({'id': str(id)})
        if rv.deleted_count > 0:
            msg = {
                "success": True,
                "message": f"Deleted {rv.deleted_count}"
            }
        else:
            raise falcon.HTTPError(falcon.HTTP_404, 'Object not found')
        return json.dumps(msg)

    ################################################################################################
    # PRIVATE METHODS
    ################################################################################################

    def _model_out(self, data):
        return self.__model__(data, strict=False)

    def _order_by(self, query, order_by):
        sort_order = pymongo.ASCENDING
        if order_by.startswith('>'):
            sort_order = pymongo.DESCENDING
        order_by = order_by.replace('<', '').replace('>', '')
        query = query.sort(order_by, sort_order)
        return query

    def _insert_one(self, data):
        data['created_at'] = arrow.now().datetime
        try:
            rv = self.q.insert_one(data)
        except Exception as e:
            console.error(e)
        else:
            obj = self.get(oid=rv.inserted_id)
            return obj

    def _insert_some(self, data):
        for item in data:
            item['created_at'] = arrow.now().datetime
        try:
            rv = self.q.insert_many(data)
        except Exception as e:
            console.error(e)
        else:
            return [self.get(oid=oid) for oid in rv.inserted_ids]

    def _set_id(self, data) -> dict:
        if isinstance(data, list):
            for item in data:
                if not item.get('id', None):
                    item['id'] = str(uuid.uuid4())
        else:
            if not data.get('id', None):
                data['id'] = str(uuid.uuid4())

        return data

    def _purge(self):
        """Use with caution. Mostly here to help with tests cleanup.
        """
        self.q.delete_many({})

    @staticmethod
    def _preprocess(**kwargs):
        for k, v in kwargs.items():
            if isinstance(v, uuid.UUID):
                kwargs[k] = str(v)

        return kwargs

    @staticmethod
    def _restore_uuids(**kwargs):
        for k, v in kwargs.items():
            if len(k) > 3 and k.endswith('_id'):
                kwargs[k] = uuid.UUID(v)

        return kwargs

    @staticmethod
    def _jsonify(data: dict):
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
                if isinstance(v, ObjectId):
                    data[k] = str(v)
                if isinstance(v, uuid.UUID):
                    data[k] = str(v)
                if isinstance(v, datetime) or isinstance(v, date):
                    data[k] = arrow.get(v).isoformat()

            # Create json from kwargs
            j = json.dumps(data)
        return json.loads(j)

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
