# -*- coding: utf-8 -*-

"""
    smpa.db.documentdb.registry
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Model registry for DocumentDB
"""


import pymongo
from smpa.helpers.console import console


class RegistryError(Exception):
    pass


class ModelRegistry(object):

    def __init__(self):
        self._models = {}
        self._tables = []
        self._initialsed = False

    def get_class(self, name):
        if name in self._models:
            return self._models[name]
        else:
            raise RegistryError(f'Model {name} not found')

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
                q = model._db[model._table]
                q.delete_many({})
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
                q = model._db[model._table]
                q.delete_many({})
            except Exception as e:
                console.warn(e)
                raise
        return True

    def init(self):
        if not self._initialsed:
            total = len(self._models)
            count = 0
            for name, model in self._models.items():
                count += 1
                progress = count / total * 100
                console.progress('Registering models', progress)
                self._init_model(name, model)
            self._initialsed = True
            console.reset()

    def _init_model(self, name, model):
        from smpa.app import db
        model._model = model
        setattr(model, '_db', db)
        self._create_table(name, model)
        self._add_indexes(name, model)

    def _create_table(self, name, model):
        pass

    def _add_indexes(self, name, model):
        if model._uniques:
            for key in model._uniques:
                model._db[model._table].create_index(key, background=True, sparse=True, unique=True)

        model._db[model._table].create_index('id', background=True, sparse=True, unique=True)


model_registry = ModelRegistry()
