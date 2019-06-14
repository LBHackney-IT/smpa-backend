# -*- coding: utf-8 -*-

"""
    rdb.registry
    ~~~~~~~~~~~~
    Keep a record of all the models registered.
"""

import os
import rethinkdb
from rethinkdb.errors import ReqlOpFailedError

from ..helpers.console import console
from .connection import rconnect


r = rethinkdb.RethinkDB()


class ModelRegistry(object):

    def __init__(self):
        self._models = {}
        self._tables = []
        self._initialsed = False

    def add(self, name, model, meta):
        # console.info(f'Registering {name} (initialised: {self._initialsed})')

        if name in self._models:
            return
        if type(model) != meta:
            raise ValueError('{} is not of type({})'.format(model, meta))

        self._models[name] = model
        if self._initialsed is True:
            # This model is appearing after init has already run, so we need to _init_model it.
            self._init_model(name, model)

    def purge(self):
        """Purges all records from all tables, without dropping those tables.
        """
        total = len(self._models)
        count = 0
        for name, model in self._models.items():
            count += 1
            progress = count / total * 100
            console.progress('Dropping tables', progress)
            try:
                # console.info('Drop {} table'.format(model._table))
                with rconnect() as conn:
                    query = r.db(model._db).table(model._table).get_all().delete()
                    query.run(conn)
            except ReqlOpFailedError as e:
                console.warn(e)
                console.warn('{} table failed to purge'.format(model._table))
            except Exception as e:
                console.warn(e)
                raise
        return True

    def drop_tables(self):
        total = len(self._models)
        count = 0
        for name, model in self._models.items():
            count += 1
            progress = count / total * 100
            console.progress('Dropping tables', progress)
            try:
                # console.info('Drop {} table'.format(model._table))
                with rconnect() as conn:
                    query = r.db(model._db).table_drop(model._table)
                    # console.info(query)
                    query.run(conn)
            except ReqlOpFailedError as e:
                console.warn(e)
                console.warn('{} table failed to drop'.format(model._table))
            except Exception as e:
                console.warn(e)
                raise
        return True

    def init(self):
        total = len(self._models)
        count = 0
        for name, model in self._models.items():
            count += 1
            progress = count / total * 100
            console.progress('Registering models', progress)
            self._init_model(name, model)
        self._initialsed = True
        console.reset()
        console.success('READY')

    def _init_model(self, name, model):
        from smpa.app import config
        model._model = model
        setattr(model, '_db', config.RDB_DB)
        self._create_table(name, model)
        self._add_indexes(name, model)

    def _create_table(self, name, model):
        if name not in self._tables:
            try:
                # console.info('create {} table for {}'.format(model._table, name))
                with rconnect() as conn:
                    query = r.db(model._db).table_create(model._table)
                    # console.info(query)
                    query.run(conn)
            except ReqlOpFailedError:
                pass
                # console.info('{} table probably already exists'.format(model._table))
            except Exception as e:
                console.warn(e)
                raise
            else:
                self._tables.append(name)

    def _add_indexes(self, name, model):
        table = r.db(model._db).table(model._table)
        with rconnect() as conn:
            try:
                table.index_create("created_at", r.row["created_at"]).run(conn)
                table.index_create("updated_at", r.row["updated_at"]).run(conn)
            except rethinkdb.errors.ReqlOpFailedError:
                # Already exists.
                pass


model_registry = ModelRegistry()
