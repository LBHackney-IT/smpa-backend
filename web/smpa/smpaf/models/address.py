# -*- coding: utf-8 -*-

"""
    models.address
    ~~~~~~~~~~~~~~
    Address related models.
"""

from .core import BaseModel, ORMMeta
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType, FloatType, ModelType
)


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
    number = StringType(max_length=255)
    property_name = StringType(max_length=255)
    address_line_1 = StringType(max_length=255)
    address_line_2 = StringType(max_length=255)
    address_line_3 = StringType(max_length=255)
    town_city = StringType(max_length=255)
    postcode = StringType(max_length=15)


class Address(BaseAddress, metaclass=ORMMeta):

    """A basic address.

    Attributes:
        postcode (Unicode): Postcode is a required field.

    TODO: Check other required fields.
    """
    postcode = StringType(max_length=15, required=True)


class SiteAddress(BaseAddress, metaclass=ORMMeta):

    """A site address. Site addresses may not have a postcode assigned
    so this becomes optional and we add fields for easting, northing, ward,
    bplu, uprn, property type and description.

    Attributes:
        postcode (TYPE): Description
        easting (TYPE): Description
        northing (TYPE): Description
        description (TYPE): Description
    """
    postcode = StringType(max_length=15, required=True)
    easting = StringType(max_length=255)
    northing = StringType(max_length=255)
    ward = StringType(max_length=255)
    bplu = StringType(max_length=255)
    uprn = StringType(max_length=255)
    property_type = StringType(max_length=255)
    description = StringType(max_length=255)


class Article4Direction(BaseModel, metaclass=ORMMeta):

    """Article 4 directions should probably come from a predefined list.

    TODO: Create these at startup.

    Attributes:
        name (str): The name of the direction.
    """

    name = StringType(max_length=255)


class SiteConstraints(BaseModel, metaclass=ORMMeta):

    """These details get pulled through from another API and saved here
    for convenience.

    Attributes:
        conservation_area (str): The name of the conservation area
        listed_statutary (bool): The statutary listed status
        listed_local (bool): The local listed status
        flood_zone (str): TODO
        tree_preservation_orders (str): TODO
        article_4_directions (list): List of fk relations to Article4Directions
    """

    conservation_area = StringType(max_length=255)
    listed_statuary = BooleanType(default=False)
    listed_local = BooleanType(default=False)
    flood_zone = StringType(max_length=255)
    tree_preservation_orders = StringType(max_length=255)
    article_4_directions = ListType(ModelType(Article4Direction))


class BS7666Address(BaseModel, metaclass=ORMMeta):

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
    street_description = StringType(max_length=255)
    locality = StringType(max_length=255)
    town = StringType(max_length=255)
    post_town = StringType(max_length=255)
    postcode = StringType(max_length=255)
    unique_property_reference_number = StringType(max_length=255)
    paon = StringType(max_length=255)
    country = StringType(max_length=255)


class InternationalAddress(BaseModel, metaclass=ORMMeta):

    """Used for international addresses

    Attributes:
        line1 (Unicode): The rest of the address
        country (Unicode): The country
        international_postal_code (Unicode): The international postal code
    """
    line1 = StringType(max_length=255)
    country = StringType(max_length=255)
    international_postal_code = StringType(max_length=255)


class ExternalAddress(BaseModel, metaclass=ORMMeta):

    """Yet to work out how or why this is used.
    """
    international_address_id = UUIDType(required=True)  # rel: InternationalAddress
