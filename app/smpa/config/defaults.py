# -*- coding: utf-8 -*-

"""
    config.defaults
    ~~~~~~~~~~~~~~~
    Some default data, used by startup to initialise the DB with required data.
"""

import os
import envkey  # NOQA


####################################################################################################
# Units / locations
####################################################################################################


AREA_UNITS = [
    ("457898dd-3da1-4d14-b283-be6398981183", "sq centimetres"),
    ("095bd097-f66e-4c66-bc1e-3521a0358e8d", "sq metres"),
    ("c0d0cc35-4923-4a68-a09c-cf2a748b257b", "hectares"),
    ("d1c88255-7e32-480b-9015-b47ff573755d", "sq miles"),
]
LINEAR_UNITS = [
    ("664a35f2-78c9-4a0a-a8c3-9689192d286a", "centimetres"),
    ("2c19e89a-620d-451f-8a0f-c12f59f68a77", "metres"),
    ("708f28a7-2bac-4fcc-83ce-f3e8c7f8796a", "miles")
]
DOCUMENT_SIZES = [
    ("a3ec6180-a863-43e9-8f6c-de7a171ce489", "A1"),
    ("1a88eefb-aa38-4ee0-a916-6c197dc7e461", "A2"),
    ("6c5b4c9b-1938-4962-923f-ee722f550f26", "A3"),
    ("1b3b842c-70e7-413c-b6c7-4503b12dd417", "A4"),
    ("bb71f138-d5ff-4699-a3af-cf0298136a8c", "A5"),
]

DOCUMENT_TYPES = [
    ('a8dd4e62-5e6f-438c-82c1-9a15b3483ba5', 'Location plan'),
    ('d6658515-a5a5-4a2c-9d49-67e74037ab9c', 'Design statement'),
    ('2af46301-ef5e-48ef-bc6a-369d54dc54f1', 'Heritage statement'),
    ('793d3caa-68d3-4166-99d1-d29be390228a', 'Block plan'),
    ('7090f4a9-2386-45a9-8fd6-0729e98de96b', 'Elevations'),
    ('8b80d334-e24a-4d15-b9a5-8356000ee760', 'Sections'),
    ('9ca5b818-38a0-43d8-90db-6de0f94f3a78', 'Site layout plan'),
    ('00d40b18-bbd3-4aa5-8dbc-d1b8a0c4c8ea', 'Roof plans'),
    ('cbddcfc8-d062-4202-b350-f875c04c6aa0', 'Floor plans'),
    ('f1ff39d9-aab3-46e3-8749-dad11c04e3b8', 'Other'),
]

WORKS_LOCATIONS = [
    ("66d1b304-5729-4654-91df-d6306e249e54", "Rear"),
    ("4f464424-ca54-4bc4-b980-c5d957a5ad1a", "Side"),
    ("243d44e8-8a8b-44de-b2ed-e7caa0628e98", "Front"),
    ("9dc99f40-ac1d-421e-a408-c253d7ead671", "Rear / side wrap-around"),
]


####################################################################################################
# Works types
####################################################################################################


BASEMENT_WORKS_TYPES = [
    ("c1d2ba2b-78d3-4826-80e1-517a90b448fd", "Excavation of a new basement"),
    ("1e7c55ff-1634-4eb6-852b-502dde20d111", "Enlargement of an existing basement"),
    ("5f563635-1a81-4f29-9763-d92ce51f20fb", "Addition of lightwell(s)"),
    ("bfbe0d4e-7bc9-4006-b461-09f009d78527", "Other alterations to the appearance of the house"),
]
ROOF_WORKS_TYPES = [
    ("f7adf884-760a-4896-9202-0f36394c191c", "Addition of a dormer extension"),
    ("fcb1bae9-6888-45ce-a7ab-d030794f7622", "Removal of a dormer extension"),
    ("59631416-c70e-48fd-8a8c-f0400273d579", "Creation of a mansard styled roof extension"),
    ("65a120df-37ad-4585-9747-e0cb2f634925", "Installation of rooflight(s) and/or roof lantern(s)"),
    ("ed26c6eb-d1b9-4cba-a3c3-1f6e64141cc4", "Addition of a new storey(s)"),
    ("8307112c-0f0b-4b6d-952d-81e80f920fc5", "Alteration of a roof slope"),
    ("73bb66f9-6a5d-46d3-951f-5db6dd01a107", "Replacement of a roof structure and/or covering"),
    ("8b2b35bc-ea62-432c-a6d6-baa3b9062c85", "Removal of chimney"),
    ("1d038d56-2602-4c86-b199-bfab695a43d9", "Addition of chimney"),
]
BORDER_WORKS_TYPES = [
    ("337eafe7-fae0-4e00-9cf0-5289cfc857f7", "Addition of a new entrance"),
    ("317b8adf-9c57-4e36-999a-35e918f15f56", "Removal of an entrance"),
    ("4fe9a1f3-6ea9-420c-a6e7-8000832fbea6", "Replacement and/or repair of wall"),
    ("dbd3a9dd-61f5-4152-9f9f-6fcb779ac6f2", "Replacement and/or repair of pillar caps"),
]
ACCESS_WORKS_SCOPES = [
    ("44c566ba-95dc-4cff-b0a9-53de934d309e", "Only for pedestrian access"),
    ("6d7c5aa1-7c6b-42be-b791-8aed006b1482", "Only for vehicle access"),
    ("b716a875-8928-48f7-9e77-3b8c1eced6af", "For vehicle and pedestrian access"),
]
ACCESS_WORKS_TYPES = [
    ("f09b702e-c3c6-4db4-9faa-b70288176cac", "Addition of a new entrance"),
    ("679143a9-0ee5-478e-984f-11c990979061", "Removal of an entrance"),
    ("164ac9b1-2201-49d2-a572-444c58850378", "Improve disabled access"),
    ("b6745de3-1867-4b01-82e3-d0e06a385e9e", "Dropped kerb and formation of vehicular access"),
]
PARKING_WORKS_SCOPES = [
    ("c4358d0e-c649-4b48-9a05-405d6ee90c0c", "Only car parking spaces"),
    ("0e5f59ac-fb07-4419-8578-41e011a83d1f", "Only cycle parking spaces"),
    ("8033164a-49e1-47db-810e-b0cac4ecd84b", "Both, car and bike parking spaces"),
]
EQUIPMENT_WORKS_TYPES = [
    ("fa6f8957-a775-4dc0-adfc-4c3ddfd42698", "Satellite dish or antenna"),
    ("cc70f42f-dc59-4a03-bf7e-fbb2e7ff3b5b", "Air conditioning unit"),
    ("b36079c1-dc9f-4225-a94d-b7c54c83b86e", "Tank"),
]
EQUIPMENT_WORKS_CONSERVATION_TYPES = [
    ("4b2aa4a1-e01e-49ff-aedc-ddd638695839", "CCTV"),
    ("510e6d41-168d-45e6-ad7e-329a578961d2", "Security alarm"),
    ("9f9390fa-f175-4d7a-8599-48c40644f0c3", "Solar panel or other sustainable energy equipment"),
]

GATES_FENCES_WALLS_TYPES = [
    ("3f583868-33bb-4296-b924-2903f4d6ec1b", "Addition of a new gate"),
    ("5da6ca36-1bfa-4835-9b08-5efe97f0678d", "Removal of a gate"),
    ("4898743a-b2f6-4c78-ae1d-dc9fe01ed829", "Replacement and/or repair of any boundary treatment"),
    ("800d7390-21e2-45ca-8cdb-42b771daf0c6", "Replacement and/or repair of pillar caps "),
]


####################################################################################################
# Materials
####################################################################################################


MATERIALS_ROOF = [
    ("d470020f-984f-4acf-9e75-387f58db4604", "Tiles"),
    ("475c1f26-9e15-4419-9ce2-9f632e630471", "Concrete"),
    ("adbc7df9-35aa-43ca-8945-a5cee867ade7", "Slate"),
    ("23f28798-6f04-4a3b-8f3b-be61d94f94f5", "Metal"),
    ("4e832373-c6bf-420a-a00e-8164e637aad6", "Thatch"),
    ("6d00c616-a110-4560-8ede-c8130bacbdba", "Asphalt shingles"),
    ("93e5e703-94d0-467d-8caf-df5cff98aac4", "Unknown"),
    ("586e27ee-4bb3-4ce2-b918-f951ef3a77af", "Other"),
]

MATERIALS_WALL = [
    ("0e0cd4ea-a3c2-460e-b2b1-c520152766df", "Concrete"),
    ("79de5841-ff1e-470d-b602-4938bd3b1139", "Mortar plaster"),
    ("6a2b6898-b71c-434c-9d12-0e621f5d8424", "Natural stone cladding"),
    ("778a12c0-f08d-4053-9124-a2f17e460465", "Brick"),
    ("aa7a3988-7c79-47c1-ad18-9fcd8f9b33d6", "Ceramic facade"),
    ("83ac9f7f-276a-4e41-94fa-284c8fa9d78a", "Wooden cladding"),
    ("1d36eeac-d324-4b56-9f0b-d53a80d66b2e", "Metal cladding"),
    ("5d88eec9-6533-42bd-92a4-1ab5b61f5dc7", "Plastic cladding"),
    ("8c7cc8c0-bd3d-4a4d-94e3-d4417d70292c", "Glass enclosures"),
    ("981e7a28-1ad0-4bd3-8f64-757484589a53", "Other"),
]

MATERIALS_WINDOW = [
    ("0a4ebe60-1c53-4089-9930-e4861b11db3a", "Wood"),
    ("16f18419-2fa6-4d71-9cdb-f3b30b2ed04d", "Vynil"),
    ("9fc33156-5364-460a-a97a-14b9499e2562", "Aluminium"),
    ("93cc4a56-e437-46a0-8377-fd92a19a106e", "Fiberglass"),
    ("454d35e4-3f46-4569-901f-ec732129e750", "Other"),
]

MATERIALS_DOOR = [
    ("33a0cc2d-6fbc-4d40-af8e-4d0a38186de0", "Wood"),
    ("cf961526-43aa-4dfe-af2a-8786112745b8", "Steel"),
    ("85fa0514-ba0d-4be0-8931-2e97890d5a84", "Fiberglass"),
    ("e0e8d5ae-ffd6-4899-b537-3a3d1496910e", "Glass"),
    ("3595dcb8-76c3-4fb3-ba1c-5dcd1ecf6ee6", "Other"),
]


####################################################################################################
# Users
####################################################################################################


ROLES = [
    ("b8d33b86-5a84-46ff-b99e-1a0f1c6138f6", 'SuperAdmin'),
    ("109825c7-6735-4799-8b7b-f8ad78252b49", 'Admin'),
    ("831083f5-b7c9-4967-8561-ac4011be54e4", 'User'),
]

SUPERADMIN_USERS = [
    {
        "id": "d485c8d2-e116-4573-acf8-ddccc4dff129",
        "email": "systems@hactar.is",
        "password": os.environ.get('HACTAR_PASSWORD')
    }
]
