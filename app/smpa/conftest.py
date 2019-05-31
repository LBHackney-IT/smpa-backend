import pytest
from smpa.tests.fixtures.app import *  # NOQA
from smpa.tests.fixtures.address import *  # NOQA
from smpa.helpers.console import console


@pytest.yield_fixture(scope='session', autouse=True)
def setup_teardown():
    console.log('ENTER TESTS')
    # Set up
    running = True
    from smpa.app import db
    from smpa.rdb.registry import model_registry
    yield running
    # Tear down
    if db.db.startswith('test_'):
        model_registry.drop_tables()
        db.drop_all()
    else:
        console.warn('Refusing to drop non-test database')
    console.log('EXIT TESTS')
