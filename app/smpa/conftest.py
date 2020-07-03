import pytest
from smpa.helpers.console import console
from smpa.tests.fixtures.address import *  # NOQA
from smpa.tests.fixtures.app import *  # NOQA
from smpa.tests.fixtures.auth import *  # NOQA
from smpa.tests.fixtures.user import *  # NOQA


# @pytest.yield_fixture(scope='session', autouse=True)
# def setup_teardown():
#     console.log('ENTER TESTS')
#     # Set up
#     running = True
#     from smpa.app import db
#     console.warn(f'DB = {db.db}')
#     from smpa.rdb.registry import model_registry
#     yield running
#     # Tear down
#     if db.db.startswith('test_'):
#         model_registry.purge()
#     else:
#         console.warn('Refusing to drop non-test database')
#     console.log('EXIT TESTS')


@pytest.yield_fixture(scope='session', autouse=True)
def setup_teardown():
    from smpa.app import db
    from smpa.db.documentdb.registry import model_registry

    console.log('ENTER TESTS')
    # Set up
    running = True
    console.warn(f'DB = {db.db}')
    if db.name.startswith('test_'):
        model_registry.purge()
    yield running
    # Tear down
    if db.name.startswith('test_'):
        model_registry.purge()
    else:
        console.warn('Refusing to drop non-test database')
    console.log('EXIT TESTS')
