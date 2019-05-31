import pytest


def test_address_fixture(address):
    assert address.number == "42"
