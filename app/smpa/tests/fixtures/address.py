import pytest

from mixer.main import mixer
from smpa.models.address import Address, SiteAddress


@pytest.fixture
def address():
    obj = Address()
    obj.number = "42"
    obj.property_name = "property name"
    obj.address_line_1 = "address line 1"
    obj.address_line_2 = "address line 2"
    obj.address_line_3 = "address line 3"
    obj.town_city = "town city"
    obj.postcode = "postcode"
    obj.validate()
    return obj


@pytest.fixture
def site_address():
    obj = SiteAddress()
    obj.number = "42"
    obj.property_name = "property name"
    obj.address_line_1 = "address line 1"
    obj.address_line_2 = "address line 2"
    obj.address_line_3 = "address line 3"
    obj.town_city = "town city"
    obj.postcode = "postcode"
    obj.validate()
    return obj
