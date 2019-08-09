# -*- coding: utf-8 -*-

"""
    smpa.db.documentdb.connection
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    DocumentDB connection class
"""

from urllib.parse import quote_plus
from pymongo import MongoClient


class DocumentDB:

    def __init__(self, config):
        if config.DOCUMENT_DB_USER is not None:
            user = quote_plus(config.DOCUMENT_DB_USER)
            password = quote_plus(config.DOCUMENT_DB_PASSWORD)
            host = quote_plus("{}:{}".format(config.DOCUMENT_DB_HOST, int(config.DOCUMENT_DB_PORT)))
            uri = f"mongodb://{user}:{password}@{host}"
            self.client = MongoClient(uri)
        else:
            self.client = MongoClient(config.DOCUMENT_DB_HOST, int(config.DOCUMENT_DB_PORT))
        self.db = self.client[config.DOCUMENT_DB_DB]

    def init(self):
        return self.db
