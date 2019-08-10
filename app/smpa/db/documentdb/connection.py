# -*- coding: utf-8 -*-

"""
    smpa.db.documentdb.connection
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    DocumentDB connection class
"""
import os
import envkey  # NOQA
from urllib.parse import quote_plus
from pymongo import MongoClient


class DocumentDB:

    def __init__(self, config):
        if config.DOCUMENT_DB_USER is not None:
            self._user = quote_plus(config.DOCUMENT_DB_USER)
            self._password = quote_plus(config.DOCUMENT_DB_PASSWORD)

        if config.DOCUMENT_DB_USER is not None:
            host = "{}:{}".format('127.0.0.1', int(config.DOCUMENT_DB_PORT))
            uri = f"mongodb://{self._user}:{self._password}@{host}/{config.DOCUMENT_DB_DB}"
            uri_plus = f"{uri}?authSource={config.DOCUMENT_DB_DB}"
            self.client = MongoClient(uri_plus)
        else:
            self.client = MongoClient(config.DOCUMENT_DB_HOST, int(config.DOCUMENT_DB_PORT))
        self.db = self.client[config.DOCUMENT_DB_DB]

    def init(self):
        if hasattr(self, '_user'):
            self.db.authenticate(self._user, self._password)
        return self.db
