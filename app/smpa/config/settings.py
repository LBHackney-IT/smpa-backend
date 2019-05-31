import os
from smpa.helpers.console import console


class Config(object):
    resources: list = []
    base: str = 'config'
    debug = False


class ConfigTest(Config):

    """Settings for test running.
    """
    base = "test"
    debug = True


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
