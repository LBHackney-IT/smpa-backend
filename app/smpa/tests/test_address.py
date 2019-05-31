import pytest
from smpa.services.address import _addresses


def test_address_fixture(address):
    assert address.number == "42"


def test_address_validates(address):
    assert address.validate() is None


def test_address_save(address):
    a = _addresses.save(address)
    assert _addresses.count() == 1
