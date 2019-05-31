# -*- coding: utf-8 -*-

"""
    core.rethink
    ~~~~~~~~~~~~
    Setup of a RethinkDB connection.
"""

import os
import rethinkdb
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
from ..helpers.console import console


RDB_HOST = os.environ.get('RDB_HOST')
RDB_PORT = os.environ.get('RDB_PORT')
RDB_DB = os.environ.get('RDB_DB')
RDB_PASSWORD = os.environ.get('RDB_PASSWORD')


connections = []


r = rethinkdb.RethinkDB()


class rconnect(object):
    def __enter__(self):
        # console.info('CONNECT ENTER - {}:{}/{}'.format(RDB_HOST, RDB_PORT, RDB_DB))
        try:
            self.conn = r.connect(
                host=RDB_HOST,
                port=RDB_PORT,
                db=RDB_DB,
                password=RDB_PASSWORD
            )
        except RqlDriverError as e:
            console.warn(e)
            raise
        else:
            connections.append(self.conn)
            return self.conn

    def __exit__(self, type, value, traceback):
        # console.info('CONNECT EXIT')
        connections.remove(self.conn)
        self.conn.close()


class RethinkDB(object):

    def connection(self):
        conn = r.connect(host=RDB_HOST, port=RDB_PORT, password=RDB_PASSWORD)
        connections.append(conn)
        return conn

    @staticmethod
    def setup():
        conn = r.connect(host=RDB_HOST, port=RDB_PORT, password=RDB_PASSWORD)
        if r.db_list().contains(RDB_DB).run(conn) is False:
            try:
                with rconnect() as conn:
                    r.db_create(RDB_DB).run(conn)
                    console.info('Database setup completed')
            except RqlRuntimeError as e:
                console.warn(e)
                raise
        else:
            console.info('Skipping DB creation')

    def drop_all(self):
        with rconnect() as conn:
            return r.db_drop(RDB_DB).run(conn)

    def disconnect(self):
        console.info('============== DISCONNECT ===============')

        try:
            if self.rdb_conn in connections:
                connections.remove(self.rdb_conn)
            self.rdb_conn.close()
        except AttributeError:
            pass

    def connect(self):
        console.info('=============== CONNECT =================')

        try:
            self.rdb_conn = r.connect(
                host=RDB_HOST,
                port=RDB_PORT,
                db=RDB_DB
            )
            connections.append(self.rdb_conn)
            self._check_connections()
        except RqlDriverError as e:
            console.warn(e)
            raise

    def get_connection(self):
        return self.rdb_conn

    def _check_connections(self):
        if self.rdb_conn not in connections:
            raise RqlRuntimeError('Connection is not in the connection pool')

    def init(self):
        console.info('RethinkSetup.init')
        self.setup()

        # # open connection before each request
        # @app.before_request
        # def before_request():
        #     self.connect(app)

        # # close connection at end of each request
        # @app.teardown_request
        # def teardown_request(exception):
        #     self.disconnect(app)
