from smpa.tests.fixtures.app import *  # NOQA
from smpa.tests.fixtures.address import *  # NOQA
from smpa.helpers.console import console


def pytest_unconfigure(config):
    console.log('STOPPING TESTS')
