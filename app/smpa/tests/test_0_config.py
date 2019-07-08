import os
from smpa.app import config, db


def test_env():
    assert os.environ.get('SERVER_ENV', None) == 'test'


def test_db_connection():
    assert db.db.startswith('test_')


def test_testmode():
    assert config.base == 'test'
    assert config.debug is True
