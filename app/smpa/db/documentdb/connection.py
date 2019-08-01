# -*- coding: utf-8 -*-

"""
    smpa.db.documentdb.connection
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    DocumentDB connection class
"""


from pymongo import MongoClient


class DocumentDB:

    def __init__(self, config):
        self.client = MongoClient(config.DOCUMENT_DB_HOST, int(config.DOCUMENT_DB_PORT))
        self.db = self.client[config.DOCUMENT_DB_DB]

    def init(self):
        return self.db
