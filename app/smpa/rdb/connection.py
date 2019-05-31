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
        from smpa.app import config
        self.host = RDB_HOST
        self.port = RDB_PORT
        self.pw = RDB_PASSWORD
        self.db = RDB_DB
        if config.base == 'test':
            self.db = f"test_{RDB_DB}"
        try:
            self.conn = r.connect(
                host=self.host,
                port=self.port,
                db=self.db,
                password=self.pw
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

    def __init__(self, *args, **kwargs):
        from smpa.app import config
        self.host = RDB_HOST
        self.port = RDB_PORT
        self.pw = RDB_PASSWORD
        self.db = RDB_DB
        if config.base == 'test':
            self.db = f"test_{RDB_DB}"

    def connection(self):
        conn = r.connect(host=self.host, port=self.port, password=self.pw)
        connections.append(conn)
        return conn

    def setup(self):
        conn = r.connect(host=self.host, port=self.port, password=self.pw)
        if r.db_list().contains(self.db).run(conn) is False:
            try:
                with rconnect() as conn:
                    r.db_create(self.db).run(conn)
                    console.info('Database setup completed')
            except RqlRuntimeError as e:
                console.warn(e)
                raise
        else:
            console.info('Skipping DB creation')

    def drop_all(self):
        with rconnect() as conn:
            return r.db_drop(self.db).run(conn)

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
                host=self.host,
                port=self.port,
                db=self.db
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
