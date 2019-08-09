import os
from smpa.helpers.console import console


class Config(object):
    resources: list = []
    base: str = 'config'
    debug = False

    BASE_URL = 'http://localhost:8080'

    # Payments
    PAYMENT_AMOUNT = 20600
    PAYMENT_DESCRIPTION = "Submit my Planning Application payment"
    GOV_PAY_API_KEY = os.environ.get('GOV_PAY_API_KEY')
    PAYMENT_RETURN_URL = '/payment/check'

    # RethinkDB Database (deprecated)
    RDB_HOST = os.environ.get('RDB_HOST')
    RDB_PORT = os.environ.get('RDB_PORT')
    RDB_DB = os.environ.get('RDB_DB')
    RDB_PASSWORD = os.environ.get('RDB_PASSWORD')

    # DocumentDB database
    DOCUMENT_DB_USER = None  # Overridden in remote configs
    DOCUMENT_DB_HOST = os.environ.get('DOCUMENT_DB_HOST')
    DOCUMENT_DB_PORT = os.environ.get('DOCUMENT_DB_PORT')
    DOCUMENT_DB_DB = os.environ.get('DOCUMENT_DB_DB')
    DOCUMENT_DB_PASSWORD = os.environ.get('DOCUMENT_DB_PASSWORD', '')

    # Notifications
    GOV_NOTIFY_API_KEY = os.environ.get('GOV_NOTIFY_API_KEY')
    NOTIFICATIONS_REPLY_TO = 'andy+smpa@hactar.is'
    NOTIFICATIONS_NOTIFY = 'andy@hactar.is'

    def get_verification_url(self, verification_token: str) -> str:
        return f"{self.BASE_URL}/accounts/verify/{verification_token}"

    def get_payment_return_url(self, application_id, payment_id) -> str:
        p_id = payment_id
        return f"{self.BASE_URL}/applications/{application_id}{self.PAYMENT_RETURN_URL}/{p_id}"

    def get_view_application_url(self, application_id: str) -> str:
        return f"{self.BASE_URL}/applications/{application_id}/view"

    def get_password_reset_url(self, token: str) -> str:
        return f"{self.BASE_URL}/accounts/reset-password/{token}"


class ConfigTest(Config):

    """Settings for test running.
    """
    base = "test"
    debug = True

    RDB_DB = 'test_' + str(os.environ.get('RDB_DB'))
    DOCUMENT_DB_DB = 'test_' + str(os.environ.get('DOCUMENT_DB_DB'))


class ConfigDevelopment(Config):
    base: str = 'development'


class ConfigStaging(Config):
    base = 'stage'
    DOCUMENT_DB_USER = os.environ.get('DOCUMENT_DB_USER')
    NOTIFICATIONS_REPLY_TO = 'planning@hackney.gov.uk'
    NOTIFICATIONS_NOTIFY = 'planning@hackney.gov.uk'


class ConfigProduction(Config):
    base = 'production'
    DOCUMENT_DB_USER = os.environ.get('DOCUMENT_DB_USER')
    NOTIFICATIONS_REPLY_TO = 'planning@hackney.gov.uk'
    NOTIFICATIONS_NOTIFY = 'planning@hackney.gov.uk'


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
