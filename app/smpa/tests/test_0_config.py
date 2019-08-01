import os
from smpa.app import config, db


def test_env():
    assert os.environ.get('SERVER_ENV', None) == 'test'


# def test_db_connection():
#     assert db.db.startswith('test_')


def test_documentdb_connection():
    dbname = str(db.name)
    assert dbname.startswith('test_') is True


def test_testmode():
    assert config.base == 'test'
    assert config.debug is True
