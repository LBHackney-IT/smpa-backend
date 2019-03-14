
import json
from typing import Optional
import uuid
import rethinkdb
from rethinkdb.errors import RqlRuntimeError, RqlDriverError, ReqlOpFailedError
from ..helpers.console import console
from ..rdb.connection import rconnect, RDB_DB
from ..models.core import BaseModel


r = rethinkdb.RethinkDB()


class RService(object):
    """A service that operates on a RethinkDB database. Every database interaction should
    go through a service class instance, then if the backend data store ever changes you
    can simply swap out this service class for a different one with the same method signature.
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

    def get(self, id: str):
        with rconnect() as conn:
            if id is None:
                raise ValueError

            if isinstance(id, uuid.UUID):
                id = str(id)

            try:
                query = self.q.get(id)
                console.debug(query)
                rv = query.run(conn)
            except ReqlOpFailedError as e:
                console.warn(e)
                raise
            except Exception as e:
                console.warn(e)
                raise
            else:
                if rv is not None:
                    return self.__model__(rv)
        return None

    def first(self, order_by: Optional[str] = None, **kwargs):
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
        with rconnect() as conn:
            if len(kwargs) == 0:
                raise ValueError

            try:
                query = self.q
                if order_by is not None:
                    query = self._order_by(query, order_by)

                # NOTE: Always filter before limiting
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
                data = [self.__model__(_) for _ in rv]
                try:
                    return data[0]
                except IndexError:
                    return None

    def create(self, **kwargs):
        """Creates one or more records from the json data. You can pass json directly to
        the method by using `json` as a keyword arg.

        Args:
            kwargs (dict): The data

        Returns:
            __model__ or list: Single model instance or list of them.
        """
        j = self._jsonify(kwargs)

        with rconnect() as conn:
            query = self.q.insert(j)
            rv = query.run(conn)
            data = []
            for _ in rv['generated_keys']:
                data.append(self.get(_))

            if len(data) > 2:
                return [self.__model__(_) for _ in rv]

            return self.__model__(data[0])

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

    # Private methods - these do not form part of the public API or method signature of the
    # service class.

    def _jsonify(self, data):
        """Allows methods to take arbitrary keywords or json

        Args:
            data (dict): Pass your kwargs in here

        Returns:
            json: Get back JSON

        """
        j = data.pop('json', None)
        if j is None:
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
