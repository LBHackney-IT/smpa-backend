# -*- coding: utf-8 -*-

"""
    smpa.db.documentdb.connection
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    DocumentDB connection class
"""
import os
import socket
import envkey  # NOQA
import bugsnag
from urllib.parse import quote_plus
from pymongo import MongoClient
from pathlib import Path

from smpa.helpers.console import console


class TransactionFailure(Exception):
    pass


class DocumentDB:

    def __init__(self, config):
        console.info('CONFIG', config.to_dict())
        self._config = config
        self._hostname = socket.gethostname()
        self._authenticated = False
        if config.DOCUMENT_DB_USER is not None and os.environ.get('SERVER_ENV') != 'staging':
            self._production_connect()
        else:
            self._staging_connect()

        try:
            console.info('CLIENT', self.client)
            if self.client:
                self.db = self.client[config.DOCUMENT_DB_DB]
                console.info('DB', self.db)
        except Exception:
            console.warn("Didn't create DB")
            pass

    def _staging_connect(self):
        self.client = MongoClient(self._config.DOCUMENT_DB_HOST, int(self._config.DOCUMENT_DB_PORT))
        console.info('Doing basic connection')
        bugsnag.notify(
            "DocumentDB basic connection",
            extra_data={
                'hostname': self._hostname,
                'config': self._config.to_dict(),
                'DOCUMENT_DB_HOST': self._config.DOCUMENT_DB_HOST,
                'DOCUMENT_DB_PORT': self._config.DOCUMENT_DB_PORT,
            }, severity='warn'
        )

    def _production_connect(self):
        config = self._config
        self._user = quote_plus(config.DOCUMENT_DB_USER)
        self._password = quote_plus(config.DOCUMENT_DB_PASSWORD)
        self._super_user = quote_plus(config.DOCUMENT_DB_SUPERUSER)
        self._super_password = quote_plus(config.DOCUMENT_DB_SUPERPASS)
        # self._cert = '/usr/srv/rds-combined-ca-bundle.pem'
        self._cert = '/tmp/rds-combined-ca-bundle.pem'

        if not self._ensure_cert_exists():
            console.warn('Cert not found')

        try:
            connection_string = self.get_connection_str()
            self.client = MongoClient(connection_string, connect=False)
            self.init()
            self.client.admin.command('ismaster')
            self.db = self.client[config.DOCUMENT_DB_DB]
            self._test_transaction()
        except TransactionFailure as e:
            bugsnag.notify(
                e,
                extra_data={
                    'connection_type': 'string',
                    'hostname': self._hostname,
                    'server_env': os.environ.get('SERVER_ENV'),
                    'connection_string': connection_string,
                    'config': config.to_dict(),
                }, severity='error'
            )
            try:
                self.client = MongoClient(
                    host=self._config.DOCUMENT_DB_HOST,
                    port=int(self._config.DOCUMENT_DB_PORT),
                    ssl=True,
                    ssl_ca_certs=self._cert,
                    connect=True,
                    connectTimeoutMS=self._config.DOCUMENT_DB_CONNECT_TIMEOUT,
                    serverSelectionTimeoutMS=self._config.DOCUMENT_DB_CONNECT_TIMEOUT
                )
                self.init()
                self.client.admin.command('ismaster')
                self.db = self.client[config.DOCUMENT_DB_DB]
                self._test_transaction()
            except TransactionFailure as e:
                bugsnag.notify(
                    e,
                    extra_data={
                        'connection_type': 'object',
                        'hostname': self._hostname,
                        'server_env': os.environ.get('SERVER_ENV'),
                        'client': self.client,
                        'config': config.to_dict(),
                    }, severity='error'
                )
                try:
                    self.client = MongoClient(
                        host=self._config.DOCUMENT_DB_HOST,
                        port=int(self._config.DOCUMENT_DB_PORT),
                        ssl=False,
                        connect=True,
                        connectTimeoutMS=self._config.DOCUMENT_DB_CONNECT_TIMEOUT,
                        serverSelectionTimeoutMS=self._config.DOCUMENT_DB_CONNECT_TIMEOUT
                    )
                    self.init()
                    self.client.admin.command('ismaster')
                    self.db = self.client[config.DOCUMENT_DB_DB]
                    self._test_transaction()
                except TransactionFailure as e:
                    bugsnag.notify(
                        e,
                        extra_data={
                            'connection_type': 'object NO SSL',
                            'hostname': self._hostname,
                            'server_env': os.environ.get('SERVER_ENV'),
                            'client': self.client,
                            'config': config.to_dict(),
                        }, severity='error'
                    )
                else:
                    bugsnag.notify(
                        Exception('CONNECTION SUCCEEDED'),
                        extra_data={
                            'connection_type': 'object NO SSL',
                            'hostname': self._hostname,
                            'server_env': os.environ.get('SERVER_ENV'),
                            'client': self.client,
                            'config': config.to_dict(),
                        }, severity='info'
                    )
            else:
                bugsnag.notify(
                    Exception('CONNECTION SUCCEEDED'),
                    extra_data={
                        'connection_type': 'object',
                        'hostname': self._hostname,
                        'server_env': os.environ.get('SERVER_ENV'),
                        'client': self.client,
                        'config': config.to_dict(),
                    }, severity='info'
                )
        except Exception as e:
            console.warn('Failed to do full connection')
            console.warn(e)
            bugsnag.notify(
                e,
                extra_data={
                    'hostname': self._hostname,
                    'server_env': os.environ.get('SERVER_ENV'),
                    'connection_string': connection_string,
                    'config': config.to_dict(),
                }, severity='error'
            )
        else:
            bugsnag.notify(
                Exception('CONNECTION SUCCEEDED'),
                extra_data={
                    'connection_type': 'string',
                    'hostname': self._hostname,
                    'server_env': os.environ.get('SERVER_ENV'),
                    'connection_string': connection_string,
                    'config': config.to_dict(),
                }, severity='info'
            )

    def get_connection_str(self):
        """This connection string apparently works from inside the container...

        user = config.DOCUMENT_DB_USER
        passw = config.DOCUMENT_DB_SUPERPASS

        'mongodb://{user}:{passw}@smpa.cluster-cjja8v30lilr.eu-west-2.docdb.amazonaws.com:27017/
        ?ssl=true
        &ssl_ca_certs=rds-combined-ca-bundle.pem
        &replicaSet=rs0
        &readPreference=secondaryPreferred'

        Returns:
            str: A connection string for mongo client
        """
        config = self._config
        user = config.DOCUMENT_DB_USER
        passw = config.DOCUMENT_DB_SUPERPASS

        protocol = "mongodb://"
        host = f"{user}:{passw}@smpa.cluster-cjja8v30lilr.eu-west-2.docdb.amazonaws.com"
        port = f":{config.DOCUMENT_DB_PORT}/"
        ssl = "?ssl=true"
        certs = "&ssl_ca_certs=/tmp/rds-combined-ca-bundle.pem"
        rs = "&replicaSet=rs0"
        rp = "&readPreference=secondaryPreferred"

        connection_string = protocol + host + port + ssl + certs + rs + rp

        self.connection_string = connection_string
        return connection_string

    def _ensure_cert_exists(self):
        cert = Path(self._cert)
        if cert.is_file():
            return True
        else:
            bugsnag.notify(
                Exception("Failed to find certificate"), severity='error'
            )

    def _authenticate(self, user, password):
        plen = len(password) - 5
        obfus = "*" * plen
        passw = password[:5] + obfus
        try:
            self.db.authenticate(user, password)
        except Exception as e:
            bugsnag.notify(
                Exception(f"Auth failed for {user} {passw}"),
                extra_data={
                    'error': e,
                    'connection_string': self.connection_string,
                    'user': user,
                    'pass': password,
                    'config': self._config.to_dict(),
                }, severity='warn'
            )
        else:
            bugsnag.notify(
                Exception(f"Auth SUCCEEDED for {user} {passw}"),
                extra_data={
                    'connection_string': self.connection_string,
                    'user': user,
                    'pass': password,
                    'config': self._config.to_dict(),
                }, severity='info'
            )
            self._authenticated = True
        return self._authenticated

    def init(self):
        if not self._authenticated:
            if hasattr(self, '_user') and hasattr(self, '_super_password'):
                self._authenticate(self._user, self._super_password)

        if not self._authenticated:
            if hasattr(self, '_super_user') and hasattr(self, '_super_password'):
                self._authenticate(self._super_user, self._super_password)

        if not self._authenticated:
            if hasattr(self, '_user') and hasattr(self, '_password'):
                self._authenticate(self._user, self._password)

        if not self._authenticated:
            if hasattr(self, '_super_user') and hasattr(self, '_password'):
                self._authenticate(self._super_user, self._password)

        return self.db

    def _test_transaction(self):
        # Try a basic insert and retrieve
        try:
            collection = self.db['startup_test']
            collection.insert_one({
                'test': 'test',
                'hostname': self._hostname
            })
            rv = collection.find_one({'hostname': self._hostname})
        except Exception as e3:
            bugsnag.notify(
                e3,
                context="Failed test transactions",
                extra_data={
                    'connection_string': self.connection_string,
                    'hostname': self._hostname,
                    'config': self._config.to_dict(),
                }, severity='error'
            )
            raise TransactionFailure('Failed test transactions')
        else:
            if hasattr(self, 'connection_string'):
                bugsnag.notify(
                    Exception("Test transactions succeeded"),
                    context="Passed test transactions",
                    extra_data={
                        'connection_string': self.connection_string,
                        'hostname': self._hostname,
                        'rv': rv,
                    }, severity='info'
                )
