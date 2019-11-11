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


class DocumentDB:

    def __init__(self, config):
        console.info('CONFIG', config.to_dict())
        self._config = config
        self._hostname = socket.gethostname()
        self._authenticated = False
        from smpa.app import __version__
        self.__version__ = __version__
        if config.DOCUMENT_DB_USER is not None:
            self._config = config
            self._user = quote_plus(config.DOCUMENT_DB_USER)
            self._password = quote_plus(config.DOCUMENT_DB_PASSWORD)
            self._super_user = quote_plus(config.DOCUMENT_DB_SUPERUSER)
            self._super_password = quote_plus(config.DOCUMENT_DB_SUPERPASS)
            # self._cert = '/usr/srv/rds-combined-ca-bundle.pem'
            self._cert = '/tmp/rds-combined-ca-bundle.pem'

            if not self._ensure_cert_exists():
                console.warn('Cert not found')
                return False

            try:
                connection_string = self.get_connection_str()
                self.client = MongoClient(connection_string, connect=False)
            except Exception as e:
                console.warn('Failed to do full connection')
                console.warn(e)
                bugsnag.notify(
                    e,
                    extra_data={
                        'version': self.__version__,
                        'hostname': self._hostname,
                        'server_env': os.environ.get('SERVER_ENV'),
                        'connection_string': connection_string,
                        'config': config.to_dict(),
                    }, severity='error'
                )
        else:
            self.client = MongoClient(config.DOCUMENT_DB_HOST, int(config.DOCUMENT_DB_PORT))
            console.info('Doing basic connection')
            bugsnag.notify(
                "DocumentDB basic connection",
                extra_data={
                    'version': self.__version__,
                    'hostname': self._hostname,
                    'config': config.to_dict(),
                    'DOCUMENT_DB_HOST': config.DOCUMENT_DB_HOST,
                    'DOCUMENT_DB_PORT': config.DOCUMENT_DB_PORT,
                }, severity='warn'
            )
        try:
            console.info('CLIENT', self.client)
            if self.client:
                self.db = self.client[config.DOCUMENT_DB_DB]
                console.info('DB', self.db)
        except Exception:
            console.warn("Didn't create DB")
            pass

    def get_connection_str(self):
        host = "{}:{}".format(self._config.DOCUMENT_DB_HOST, int(self._config.DOCUMENT_DB_PORT))
        # uri = f"mongodb://{self._user}:{self._password}@{host}/{self._config.DOCUMENT_DB_DB}"
        uri = f"mongodb://{self._super_user}:{self._super_password}@{host}/"
        uri_plus = f"{uri}?authSource={self._config.DOCUMENT_DB_DB}"
        ssl = "&ssl=true&ssl_ca_certs=" + self._cert
        # ssl_off = "&ssl=false"
        rs = "&replicaSet=rs0"
        rp = "&readPreference=secondaryPreferred"
        # connection_string = uri_plus + ssl + rs
        # connection_string = uri + ssl + rs
        # connection_string = uri_plus + rs
        # connection_string = uri_plus + ssl_off + rs + rp
        connection_string = uri_plus + rs + rp
        # connection_string = uri_plus + ssl + rs + rp
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
                    'version': self.__version__,
                    'user': user,
                    'pass': password,
                    'config': self._config.to_dict(),
                }, severity='warn'
            )
        else:
            bugsnag.notify(
                Exception(f"Auth SUCCEEDED for {user} {passw} / {self.__version__}"),
                extra_data={
                    'connection_string': self.connection_string,
                    'version': self.__version__,
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
            if hasattr('self', '_super_user') and hasattr('self', '_super_password'):
                self._authenticate(self._super_user, self._super_password)

        if not self._authenticated:
            if hasattr(self, '_user') and hasattr(self, '_password'):
                self._authenticate(self._user, self._password)

        if not self._authenticated:
            if hasattr('self', '_super_user') and hasattr('self', '_password'):
                self._authenticate(self._super_user, self._password)

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
                    'version': self.__version__,
                    'hostname': self._hostname,
                    'config': self._config.to_dict(),
                }, severity='error'
            )
        else:
            if hasattr(self, 'connection_string'):
                bugsnag.notify(
                    Exception("Test transactions succeeded"),
                    context="Passed test transactions",
                    extra_data={
                        'connection_string': self.connection_string,
                        'version': self.__version__,
                        'hostname': self._hostname,
                        'rv': rv,
                    }, severity='info'
                )

        return self.db
