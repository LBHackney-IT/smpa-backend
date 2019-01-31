# -*- coding: utf-8 -*-

"""
    rdb.registry
    ~~~~~~~~~~~~
    Keep a record of all the models registered.
"""

import os
import rethinkdb as r
from rethinkdb.errors import ReqlOpFailedError

from ..helpers.console import console
from .connection import rconnect


class ModelRegistry(object):

    def __init__(self):
        self._models = {}
        self._tables = []
        self._initialsed = False

    def add(self, name, model, meta):
        console.info(f'Registering {name} (initialised: {self._initialsed})')

        if name in self._models:
            return
        if type(model) != meta:
            raise ValueError('{} is not of type({})'.format(model, meta))

        self._models[name] = model
        if self._initialsed is True:
            # This model is appearing after init has already run, so we need to _init_model it.
            self._init_model(name, model)

    def drop_tables(self):
        for name, model in self._models.items():
            try:
                console.info('Drop {} table'.format(model._table))
                with rconnect() as conn:
                    query = r.db(model._db).table_drop(model._table)
                    console.info(query)
                    query.run(conn)
            except ReqlOpFailedError as e:
                console.info('{} table failed to drop'.format(model._table))
            except Exception as e:
                log.warn(e)
                raise
        return True

    def init(self):
        console.info('registry init')
        for name, model in self._models.items():
            self._init_model(name, model)
        self._initialsed = True

    def _init_model(self, name, model):
        model._model = model
        setattr(model, '_db', os.environ.get('RDB_DB'))
        self._create_table(name, model)

    def _create_table(self, name, model):
        if name not in self._tables:
            try:
                console.info('create {} table for {}'.format(model._table, name))
                with rconnect() as conn:
                    query = r.db(model._db).table_create(model._table)
                    console.info(query)
                    query.run(conn)
            except ReqlOpFailedError as e:
                console.info('{} table probably already exists'.format(model._table))
            except Exception as e:
                log.warn(e)
                raise
            else:
                self._tables.append(name)


model_registry = ModelRegistry()
