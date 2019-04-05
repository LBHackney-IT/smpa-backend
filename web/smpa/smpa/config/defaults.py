# -*- coding: utf-8 -*-

"""
    config.defaults
    ~~~~~~~~~~~~~~~
    Some default data, used by startup to initialise the DB with required data.
"""

import os
import envkey  # NOQA


AREA_UNITS = ["sq centimetres", "sq metres", "hectares", "sq miles"]
LINEAR_UNITS = ["centimetres", "metres", "miles"]
DOCUMENT_SIZES = ["A1", "A2", "A3", "A4", "A5"]
WORKS_LOCATIONS = ["Rear", "Side", "Front", "Rear / side wrap-around"]
BASEMENT_WORKS_TYPES = [
    "Excavation of a new basement",
    "Enlargement of an existing basement",
    "Addition of lightwell(s)",
    "Other alterations to the appearance of the house",
]
ROOF_WORKS_TYPES = [
    "Addition of a dormer extension",
    "Removal of a dormer extension",
    "Creation of a mansard styled roof extension",
    "Installation of rooflight(s) and/or roof lantern(s)",
    "Addition of a new storey(s)",
    "Alteration of a roof slope",
    "Replacement of a roof structure and/or covering",
    "Removal of chimney",
    "Addition of chimney",
]
BORDER_WORKS_TYPES = [
    "Addition of a new entrance",
    "Removal of an entrance",
    "Replacement and/or repair of wall",
    "Replacement and/or repair of pillar caps",
]
ACCESS_WORKS_SCOPES = [
    "Only for pedestrian access",
    "Only for vehicle access",
    "For vehicle and pedestrian access",
]
ACCESS_WORKS_TYPES = [
    "Addition of a new entrance",
    "Removal of an entrance",
    "Improve disabled access",
    "Dropped kerb and formation of vehicular access",
]
PARKING_WORKS_SCOPES = [
    "Only car parking spaces",
    "Only cycle parking spaces",
    "Both, car and bike parking spaces",
]
EQUIPMENT_WORKS_TYPES = [
    "Satellite dish or antenna",
    "Air conditioning unit",
    "Tank",
]
EQUIPMENT_WORKS_CONSERVATION_TYPES = [
    "CCTV",
    "Security alarm",
    "Solar panel or other sustainable energy equipment",
]
MATERIALS_ROOF = [
    "Tiles",
    "Concrete",
    "Slate",
    "Metal",
    "Thatch",
    "Asphalt shingles",
    "Unknown",
    "Other",
]

MATERIALS_WALL = [
    "Concrete",
    "Mortar plaster",
    "Natural stone cladding",
    "Brick",
    "Ceramic facade",
    "Wooden cladding",
    "Metal cladding",
    "Plastic cladding",
    "Glass enclosures",
    "Other",
]

MATERIALS_WINDOW = [
    "Wood",
    "Vynil",
    "Aluminium",
    "Fiberglass",
    "Other",
]

MATERIALS_DOOR = [
    "Wood",
    "Steel",
    "Fiberglass",
    "Glass",
    "Other",
]

ROLES = ['SuperAdmin', 'Admin', 'User']
SUPERADMIN_USERS = [
    {
        "email": "systems@hactar.is",
        "password": os.environ.get('HACTAR_PASSWORD')
    }
]
