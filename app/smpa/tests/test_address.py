import pytest
from smpa.services.address import _addresses


def test_address_fixture(address):
    assert address.number == "42"


def test_address_validates(address):
    assert address.validate() is None


####################################################################################################
# Test the address service
#
# Some of these are marked as slow just because they access the database.
#
####################################################################################################

@pytest.mark.slow
def test_address_save_and_get(address):
    a = _addresses.save(address)
    assert _addresses.count() == 1
    assert a.id is not None
    assert _addresses.get(a.id) is not None
    _addresses.delete(a)
    assert _addresses.count() == 0


@pytest.mark.slow
def test_address_find(address):
    a = _addresses.save(address)
    assert len(_addresses.find(number='42')) > 0
    _addresses.delete(a)
    assert _addresses.count() == 0


def test_new(address):
    a = _addresses.new(
        number="23",
        property_name="The Big Building",
        address_line_1="A Street",
        address_line_2="Some district",
        address_line_3="Something else",
        town_city="London",
        postcode="N1 1NN"
    )
    assert a.validate() is None
