
# 3rd Party
import sqlalchemy as sa

# Module
from .core import BaseModel


class Address(BaseModel):

    """A BS7666 compatible address.

    https://data.gov.uk/education-standards/sites/default/files/CL-Address-Line-Type-v3-0.pdf

    Attributes:
        country (Unicode): Country name
        locality (Unicode): Locality name
        paon (Unicode): Primary Addressable Object Name – e.g. building name or street number
        post_town (Unicode): Town or city within which Royal Mail sorting office is located
        postcode (Unicode): The postcode for a UK address
        street_description (Unicode): Street name, description or street number
        town (Unicode): Town name
        unique_property_reference_number (Unicode): Inherited from old schema
    """

    __tablename__ = 'address'

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
        country (Unicode): The country
        international_postal_code (Unicode): The international postal code
        line1 (Unicode): The rest of the address
    """

    __tablename__ = 'international_address'

    line1 = sa.Column(sa.Unicode(255))
    country = sa.Column(sa.Unicode(255))
    international_postal_code = sa.Column(sa.Unicode(255))


class ExternalAddress(BaseModel):

    """Yet to work out how or why this is used.
    """

    __tablename__ = 'external_address'

    international_address = sa.Column(sa.Integer, sa.ForeignKey('international_address.id'))
