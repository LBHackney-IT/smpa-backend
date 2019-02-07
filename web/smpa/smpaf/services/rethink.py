
import uuid
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError, ReqlOpFailedError
from ..helpers.console import console
from ..rdb.connection import rconnect, RDB_DB
from ..models.core import BaseModel


class RService(object):
    """A service that operates on a RethinkDB database."""

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

    def create(self, json):
        """Creates one or more records from the json data

        Args:
            json (json): The data

        Returns:
            __model__ or list: Single model instance or list of them.
        """
        with rconnect() as conn:
            query = self.q.insert(json)
            rv = query.run(conn)
            data = []
            for _ in rv['generated_keys']:
                data.append(self.get(_))

            if len(data) > 2:
                return [self.__model__(_) for _ in rv]

            return self.__model__(data[0])

    def update(self, id, json):
        """updates a record from the json data

        Args:
            id (uuid): Description
            json (json): The data

        Returns:
            __model__ or list: Single model instance or list of them.
        """
        with rconnect() as conn:
            query = self.q.get(id).update(json, return_changes=True)
            rv = query.run(conn)
            if len(rv['changes']):
                return self.__model__(rv['changes'][0]['new_val'])
            else:
                return self.get(id)

    def all(self, **kwargs):
        with rconnect() as conn:
            query = self.q
            rv = query.run(conn)
            data = [self.__model__(_) for _ in rv]
            return data
