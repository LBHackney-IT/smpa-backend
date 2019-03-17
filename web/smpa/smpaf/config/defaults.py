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
BASEMENT_WORKS_LOCATIONS = [
    "Excavation of a new basement",
    "Enlargement of an existing basement",
    "Addition of lightwell(s)",
    "Other alterations to the appearance of the house",
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

MATERIALS_WALLS = [
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

MATERIALS_WINDOWS = [
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
