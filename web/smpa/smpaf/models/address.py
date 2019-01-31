
# 3rd Party
import sqlalchemy as sa

from ..helpers.database import MyUUID

# Module
from .core import BaseModel


class BaseAddress(BaseModel):

    """Base address which can be extended / altered to provide address variants.

    Attributes:
        number (Unicode): It's a string to allow for 'Flat 3b' etc
        property_name (Unicode): Property name, eg: Hackney House
        address_line_1 (Unicode): Address line 1
        address_line_2 (Unicode): Address line 2
        address_line_3 (Unicode): Address line 3
        town_city (Unicode): Town or city
        postcode (Unicode): UK Postcode
    """

    __abstract__ = True

    number = sa.Column(sa.Unicode(255))
    property_name = sa.Column(sa.Unicode(255))
    address_line_1 = sa.Column(sa.Unicode(255))
    address_line_2 = sa.Column(sa.Unicode(255))
    address_line_3 = sa.Column(sa.Unicode(255))
    town_city = sa.Column(sa.Unicode(255))
    postcode = sa.Column(sa.Unicode(12))


class Address(BaseAddress):

    """A basic address.

    Attributes:
        postcode (Unicode): Postcode is a required field.

    TODO: Check other required fields.
    """

    __tablename__ = 'addresses'

    postcode = sa.Column(sa.Unicode(12), nullable=False)


class SiteAddress(BaseAddress):

    """A site address. Site addresses may not have a postcode assigned
    so this becomes optional and we add fields for easting, northing
    and description.

    Attributes:
        postcode (TYPE): Description
        easting (TYPE): Description
        northing (TYPE): Description
        description (TYPE): Description
    """

    __tablename__ = 'site_addresses'

    postcode = sa.Column(sa.Unicode(12), nullable=True)
    easting = sa.Column(sa.Unicode(255))
    northing = sa.Column(sa.Unicode(255))
    description = sa.Column(sa.Unicode(255))


class BS7666Address(BaseModel):

    """A BS7666 compatible address.

    https://data.gov.uk/education-standards/sites/default/files/CL-Address-Line-Type-v3-0.pdf

    Attributes:
        street_description (Unicode): Street name, description or street number
        locality (Unicode): Locality name
        town (Unicode): Town name
        post_town (Unicode): Town or city within which Royal Mail sorting office is located
        postcode (Unicode): The postcode for a UK address
        unique_property_reference_number (Unicode): Inherited from old schema
        paon (Unicode): Primary Addressable Object Name – e.g. building name or street number
        country (Unicode): Country name
    """

    __tablename__ = 'bs7666_addresses'

    street_description = sa.Column(sa.Unicode(255))
    locality = sa.Column(sa.Unicode(255))
    town = sa.Column(sa.Unicode(255))
    post_town = sa.Column(sa.Unicode(255))
    postcode = sa.Column(sa.Unicode(255))
    unique_property_reference_number = sa.Column(sa.Unicode(255))
    paon = sa.Column(sa.Unicode(255))
    country = sa.Column(sa.Unicode(255))


class InternationalAddress(BaseModel):

    """Used for international addresses

    Attributes:
        line1 (Unicode): The rest of the address
        country (Unicode): The country
        international_postal_code (Unicode): The international postal code
    """

    __tablename__ = 'international_addresses'

    line1 = sa.Column(sa.Unicode(255))
    country = sa.Column(sa.Unicode(255))
    international_postal_code = sa.Column(sa.Unicode(255))


class ExternalAddress(BaseModel):

    """Yet to work out how or why this is used.
    """

    __tablename__ = 'external_addresses'

    international_address = sa.Column(MyUUID, sa.ForeignKey('international_address.id'))
