import os
from smpa.helpers.console import console


class Config(object):
    resources: list = []
    base: str = 'config'
    debug = False

    RDB_HOST = os.environ.get('RDB_HOST')
    RDB_PORT = os.environ.get('RDB_PORT')
    RDB_DB = os.environ.get('RDB_DB')
    RDB_PASSWORD = os.environ.get('RDB_PASSWORD')


class ConfigTest(Config):

    """Settings for test running.
    """
    base = "test"
    debug = True

    RDB_DB = 'test_' + str(os.environ.get('RDB_DB'))


class ConfigDevelopment(Config):
    base: str = 'development'


class ConfigStaging(Config):
    base = 'stage'


class ConfigProduction(Config):
    base = 'production'


CONF_MAP = {
    'test': ConfigTest,
    'development': ConfigDevelopment,
    'staging': ConfigStaging,
    'production': ConfigProduction,
}


def init_settings():
    env = os.environ.get('SERVER_ENV')
    klass = CONF_MAP[env]
    settings = klass()

    return settings
