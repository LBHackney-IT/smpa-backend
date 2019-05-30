import sqlite3

from contextlib import contextmanager
from inspect import Parameter
from typing import Iterator


class DB:
    def __init__(self) -> None:
        self._db = sqlite3.connect(":memory:")
        self._db.row_factory = sqlite3.Row

        with self.get_cursor() as cursor:
            cursor.execute("create table todos(description text, status text)")

    @contextmanager
    def get_cursor(self) -> Iterator[sqlite3.Cursor]:
        cursor = self._db.cursor()

        try:
            yield cursor
            self._db.commit()
        except Exception:
            self._db.rollback()
            raise
        finally:
            cursor.close()


class DBComponent:
    is_cacheable = True
    is_singleton = True

    def can_handle_parameter(self, parameter: Parameter) -> bool:
        return parameter.annotation is DB

    def resolve(self) -> DB:
        return DB()
