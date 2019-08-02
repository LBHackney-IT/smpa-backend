"""
    Test a walk through of hitting each endpoint in order.
"""

import os
import simplejson as json
import falcon
from .test_auth import get_token
from ..util import json_match, reset_test_user

from smpa.services.document import _document_files
from smpa.helpers.console import console

from smpa.config.defaults import (  # NOQA
    AREA_UNITS,
    LINEAR_UNITS,
    DOCUMENT_SIZES,
    WORKS_LOCATIONS,
    BASEMENT_WORKS_TYPES,
    ROOF_WORKS_TYPES,
    BORDER_WORKS_TYPES,
    ACCESS_WORKS_SCOPES,
    ACCESS_WORKS_TYPES,
    PARKING_WORKS_SCOPES,
    EQUIPMENT_WORKS_TYPES,
    EQUIPMENT_WORKS_CONSERVATION_TYPES,
    GATES_FENCES_WALLS_TYPES,
    MATERIALS_ROOF,
    MATERIALS_WALL,
    MATERIALS_WINDOW,
    MATERIALS_DOOR,
    ROLES,
    SUPERADMIN_USERS
)

TEXT_BLOB = """Praesent commodo cursus magna,
vel scelerisque nisl consectetur et. Praesent commodo cursus
magna, vel scelerisque nisl consectetur et. Donec sed odio dui.
Nullam id dolor id nibh ultricies vehicula ut id elit. Cum sociis
natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
"""

DEFAULT_DATA_ENDPOINTS = [
    "/api/v1/roof-works-types",
    "/api/v1/works-locations",
    "/api/v1/basement-works-types",
    "/api/v1/border-works-types",
    "/api/v1/access-works-scopes",
    "/api/v1/access-works-types",
    "/api/v1/parking-works-scopes",
    "/api/v1/gate-fences-walls-types",
    "/api/v1/equipment-works-types",
    "/api/v1/equipment-works-conservation-types",
    "/api/v1/area-units",
    "/api/v1/linear-units",
    "/api/v1/document-sizes",
    "/api/v1/materials/options/roof",
    "/api/v1/materials/options/wall",
    "/api/v1/materials/options/door",
    "/api/v1/materials/options/window",
]

ID_STR = "cbddcfc8-d062-4202-b350-f875c04c6aa0,f1ff39d9-aab3-46e3-8749-dad11c04e3b8"
APPLICATION_ID = None
EXTENSION_PROPOSAL_ID = None
EQUIPMENT_PROPOSAL_ID = None
SITE_ADDRESS_ID = None
TOKEN = None


reset_test_user()


def test_get_default_data(session_client):
    for url in DEFAULT_DATA_ENDPOINTS:
        rv = session_client.get(url)
        assert rv.status == '200 OK'
        assert rv is not None
        assert rv.body is not None

        try:
            result = json.loads(rv.body)
            assert len(result)
        except Exception as e:
            console.error(e)
            console.error(url)
            console.error(rv)
            console.error(rv.status)
            console.error(rv.body)


def test_application_create(session_client):
    """
        Send a post request to create an application
    """
    global APPLICATION_ID
    global TOKEN
    TOKEN = get_token()
    rv = session_client.post(
        '/api/v1/applications',
        "{}",
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    APPLICATION_ID = j['id']
    assert APPLICATION_ID is not None
    assert j['owner_id'] is not None


def test_site_contraints(session_client):
    body = json.dumps(
        {
            "uprn": 10008300829,
            "has_boundary": "yes",
            "nb_a4d": 2,
            "a4d_name": "Storage and Distribution to Residential, Light Industrial to Residential",
            "nb_conarea": 1,
            "conarea_name": "Victoria Park",
            "nb_tpo": 0,
            "tpo_name": "",
            "is_listed_building": "0",
            "is_floodzone_2": "0",
            "is_floodzone_3a": "0",
            "is_floodzone_3b": "0",
            "application_id": APPLICATION_ID
        }
    )
    rv = session_client.post(
        f'/api/v1/site-constraints',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['uprn'] == 10008300829
    assert j['has_boundary'] == "yes"


def test_application_update(session_client):
    body = """
        {
            "works_started": true,
            "date_works_started": "2018-01-01"
        }
    """
    rv = session_client.patch(
        f'/api/v1/applications/{APPLICATION_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['works_started'] is True
    assert j['date_works_started'] == "2018-01-01"


def test_application_free_text(session_client):
    body = json.dumps(
        {
            "free_text_description": TEXT_BLOB
        }
    )
    rv = session_client.patch(
        f'/api/v1/applications/{APPLICATION_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['free_text_description'] is not None
    assert j['free_text_description'] == TEXT_BLOB


def test_site_address_create(session_client):
    global SITE_ADDRESS_ID
    body = json.dumps(
        {
            "application_id": f"{APPLICATION_ID}",
            "address_line_1": "12 Stephen Mews",
            "town_city": "London",
            "postcode": "W1T 1AH",
            "description": "Hactar Towers"
        }
    )
    rv = session_client.post(
        f'/api/v1/site-addresses',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['id'] is not None
    assert json_match(result, body)
    SITE_ADDRESS_ID = result['id']


def test_extension_proposal_create(session_client):
    global EXTENSION_PROPOSAL_ID
    body = json.dumps(
        {
            "application_id": f"{APPLICATION_ID}",
        }
    )
    rv = session_client.post(
        f'/api/v1/extension-proposals',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['id'] is not None
    assert json_match(result, body)
    EXTENSION_PROPOSAL_ID = result['id']


def test_extension_proposal_update(session_client):
    body = json.dumps(
        {
            "original_house": {},
            "incidental_buildings": {}
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert "original_house" in j
    assert "incidental_buildings" in j


def test_extension_proposal_update_work_locations(session_client):
    body = json.dumps(
        {
            "original_house": {
                "single_storey_extension": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0]
                    ]
                },
                "basement": {}
            },
            "incidental_buildings": {

            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert "original_house" in j
    assert "incidental_buildings" in j
    assert WORKS_LOCATIONS[0][0] in \
        j['original_house']['single_storey_extension']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        j['original_house']['single_storey_extension']['works_location_ids']


def test_extension_proposal_update_basement_work_types(session_client):
    body = json.dumps(
        {
            "original_house": {
                "basement": {
                    "works_type_ids": [
                        BASEMENT_WORKS_TYPES[0][0]
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert "original_house" in j
    assert "incidental_buildings" in j
    assert BASEMENT_WORKS_TYPES[0][0] in \
        j['original_house']['basement']['works_type_ids']


def test_extension_proposal_update_basement_work_locations(session_client):
    body = json.dumps(
        {
            "original_house": {
                "single_storey_extension": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0]
                    ]
                },
                "basement": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0]
                    ]
                }
            },
            "incidental_buildings": {
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert "original_house" in j
    assert "incidental_buildings" in j
    assert WORKS_LOCATIONS[0][0] in \
        j['original_house']['single_storey_extension']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        j['original_house']['single_storey_extension']['works_location_ids']
    assert WORKS_LOCATIONS[0][0] in \
        j['original_house']['basement']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        j['original_house']['basement']['works_location_ids']


def test_extension_proposal_update_roof_work_types(session_client):
    body = json.dumps(
        {
            "original_house": {
                "roof": {
                    "works_type_ids": [
                        ROOF_WORKS_TYPES[0][0]
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert ROOF_WORKS_TYPES[0][0] in \
        result['original_house']['roof']['works_type_ids']


def test_extension_proposal_update_roof_work_locations(session_client):
    body = json.dumps(
        {
            "original_house": {
                "roof": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0]
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert WORKS_LOCATIONS[0][0] in \
        result['original_house']['roof']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        result['original_house']['roof']['works_location_ids']


def test_extension_proposal_update_porch_work_locations(session_client):
    body = json.dumps(
        {
            "original_house": {
                "porch": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0]
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert WORKS_LOCATIONS[0][0] in \
        result['original_house']['porch']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        result['original_house']['porch']['works_location_ids']


def test_extension_proposal_update_balcony_work_locations(session_client):
    body = json.dumps(
        {
            "original_house": {
                "balcony_terrace": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0]
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert WORKS_LOCATIONS[0][0] in \
        result['original_house']['balcony_terrace']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        result['original_house']['balcony_terrace']['works_location_ids']


def test_extension_proposal_update_staircase_work_locations(session_client):
    body = json.dumps(
        {
            "original_house": {
                "staircase": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0]
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert WORKS_LOCATIONS[0][0] in \
        result['original_house']['staircase']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        result['original_house']['staircase']['works_location_ids']


def test_extension_proposal_update_windows_work_locations(session_client):
    body = json.dumps(
        {
            "original_house": {
                "windows_doors": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0],
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert WORKS_LOCATIONS[0][0] in \
        result['original_house']['windows_doors']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        result['original_house']['windows_doors']['works_location_ids']


def test_extension_proposal_update_cladding_work_locations(session_client):
    body = json.dumps(
        {
            "original_house": {
                "cladding": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0]
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert WORKS_LOCATIONS[0][0] in \
        result['original_house']['cladding']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        result['original_house']['cladding']['works_location_ids']


def test_extension_proposal_update_outbuilding_work_locations(session_client):
    body = json.dumps(
        {
            "incidental_buildings": {
                "outbuilding": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0]
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert WORKS_LOCATIONS[0][0] in \
        result['incidental_buildings']['outbuilding']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        result['incidental_buildings']['outbuilding']['works_location_ids']


def test_extension_proposal_update_outbuilding_details(session_client):
    body = json.dumps(
        {
            "incidental_buildings": {
                "removal_or_demolition": True,
                "details": "I'm knocking a shed down."
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['incidental_buildings']['removal_or_demolition'] is True
    assert result['incidental_buildings']['details'] == "I'm knocking a shed down."


def test_extension_proposal_update_gates_fences_walls_types(session_client):
    body = json.dumps(
        {
            "boundaries": {
                "gates_fences_walls": {
                    "works_type_ids": [
                        GATES_FENCES_WALLS_TYPES[0][0]
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert GATES_FENCES_WALLS_TYPES[0][0] in \
        result['boundaries']['gates_fences_walls']['works_type_ids']


def test_extension_proposal_update_gates_fences_walls_locations(session_client):
    body = json.dumps(
        {
            "boundaries": {
                "gates_fences_walls": {
                    "works_location_ids": [
                        WORKS_LOCATIONS[0][0],
                        WORKS_LOCATIONS[1][0]
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert WORKS_LOCATIONS[0][0] in \
        result['boundaries']['gates_fences_walls']['works_location_ids']
    assert WORKS_LOCATIONS[1][0] in \
        result['boundaries']['gates_fences_walls']['works_location_ids']


def test_extension_proposal_update_means_of_access(session_client):
    body = json.dumps(
        {
            "means_of_access": {
                "access_works_scope_id": ACCESS_WORKS_SCOPES[0][0]
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['means_of_access']['access_works_scope_id'] \
        == ACCESS_WORKS_SCOPES[0][0]


def test_extension_proposal_update_means_of_access_subtypes(session_client):
    body = json.dumps(
        {
            "means_of_access": {
                "access_works_scope_id": ACCESS_WORKS_SCOPES[0][0],
                "access_works_sub_type_ids": [
                    ACCESS_WORKS_TYPES[0][0],
                    ACCESS_WORKS_TYPES[1][0]
                ]
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['means_of_access']['access_works_scope_id'] \
        == ACCESS_WORKS_SCOPES[0][0]
    assert ACCESS_WORKS_TYPES[0][0] in \
        result['means_of_access']['access_works_sub_type_ids']
    assert ACCESS_WORKS_TYPES[1][0] in \
        result['means_of_access']['access_works_sub_type_ids']


def test_extension_proposal_update_parking_scope(session_client):
    body = json.dumps(
        {
            "parking": {
                "parking_works_scope_id": PARKING_WORKS_SCOPES[0][0]
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['parking']['parking_works_scope_id'] \
        == PARKING_WORKS_SCOPES[0][0]


def test_extension_proposal_update_parking_counts(session_client):
    body = """
        {
            "parking": {
                "current_car_parking_spaces": 10,
                "planned_car_parking_spaces": 20
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['parking']['current_car_parking_spaces'] == 10
    assert result['parking']['planned_car_parking_spaces'] == 20


def test_extension_proposal_update_bike_parking_counts(session_client):
    body = """
        {
            "parking": {
                "current_bike_parking_spaces": 10,
                "planned_bike_parking_spaces": 20
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['parking']['current_bike_parking_spaces'] == 10
    assert result['parking']['planned_bike_parking_spaces'] == 20


def test_extension_proposal_update_ev_charging_points(session_client):
    body = """
        {
            "parking": {
                "new_ev_charging_points": 10
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['parking']['new_ev_charging_points'] == 10


def test_equipment_proposal_create(session_client):
    global EQUIPMENT_PROPOSAL_ID
    body = json.dumps(
        {
            "application_id": f"{APPLICATION_ID}",
        }
    )
    rv = session_client.post(
        f'/api/v1/equipment-proposals',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['id'] is not None
    assert json_match(result, body)
    EQUIPMENT_PROPOSAL_ID = result['id']


def test_equipment_proposal_update_scope(session_client):
    body = json.dumps(
        {
            "equipment":{
                "equipment_type_ids": [
                    EQUIPMENT_WORKS_TYPES[0][0],
                    EQUIPMENT_WORKS_TYPES[1][0],
                    EQUIPMENT_WORKS_TYPES[2][0]
                ],
                "equipment_conservation_type_ids": [
                    EQUIPMENT_WORKS_CONSERVATION_TYPES[0][0],
                    EQUIPMENT_WORKS_CONSERVATION_TYPES[1][0],
                    EQUIPMENT_WORKS_CONSERVATION_TYPES[2][0]
                ]
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/equipment-proposals/{EQUIPMENT_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert EQUIPMENT_WORKS_TYPES[0][0] in \
        result['equipment']['equipment_type_ids']
    assert EQUIPMENT_WORKS_TYPES[1][0] in \
        result['equipment']['equipment_type_ids']
    assert EQUIPMENT_WORKS_TYPES[2][0] in \
        result['equipment']['equipment_type_ids']
    assert EQUIPMENT_WORKS_CONSERVATION_TYPES[0][0] in \
        result['equipment']['equipment_conservation_type_ids']
    assert EQUIPMENT_WORKS_CONSERVATION_TYPES[1][0] in \
        result['equipment']['equipment_conservation_type_ids']
    assert EQUIPMENT_WORKS_CONSERVATION_TYPES[2][0] in \
        result['equipment']['equipment_conservation_type_ids']


def test_equipment_proposal_update_locations(session_client):
    body = json.dumps(
        {
            "equipment": {
                "equipment_locations": [
                    {
                        "location_ids": [
                            WORKS_LOCATIONS[3][0]
                        ],
                        "equipment_type_id": EQUIPMENT_WORKS_TYPES[0][1]
                    }
                ]
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/equipment-proposals/{EQUIPMENT_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert WORKS_LOCATIONS[3][0] in \
        result['equipment']['equipment_locations'][0]['location_ids']
    assert result['equipment']['equipment_locations'][0]['equipment_type_id'] == \
        EQUIPMENT_WORKS_TYPES[0][1]


def test_extension_proposal_floor_area(session_client):
    body = json.dumps(
        {
            "additional_floor_area": 23.8,
            "additional_floor_area_units_id": AREA_UNITS[1][0]
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert json_match(result, body)


def test_extension_proposal_additional_bedrooms(session_client):
    body = """
        {
            "new_single_bedrooms": 2,
            "new_double_bedrooms": 3
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert json_match(result, body)


def test_extension_proposal_trees(session_client):
    body = """
        {
            "trees": {
                "inside_boundry": true,
                "removed_or_pruned": true,
                "outside_boundry": true
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['trees']['inside_boundry'] is True
    assert result['trees']['removed_or_pruned'] is True
    assert result['trees']['outside_boundry'] is True


def test_extension_proposal_materials_details(session_client):
    body = """
        {
            "materials": {
                "definitions_in_documents": false,
                "definitions_in_form": true,
                "definitions_to_follow": false
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['materials']['definitions_in_documents'] is False
    assert result['materials']['definitions_in_form'] is True
    assert result['materials']['definitions_to_follow'] is False


def test_extension_proposal_materials_roof(session_client):
    body = json.dumps(
        {
            "materials": {
                "roof": {
                    "proposals": [
                        {
                            "material_id": MATERIALS_ROOF[0][0],
                            "colour_and_type": "Some lovely green roof tiles."
                        }
                    ]
                }
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['materials']['roof']['proposals'][0]['material_id'] == \
        MATERIALS_ROOF[0][0]
    assert result['materials']['roof']['proposals'][0]['colour_and_type'] == \
        "Some lovely green roof tiles."


def test_extension_proposal_materials_walls_matches_existing(session_client):
    body = """
        {
            "materials":{
                "walls": {
                    "matches_existing": true,
                    "not_applicable": false
                }
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['materials']['walls']['matches_existing'] is True
    assert result['materials']['walls']['not_applicable'] is False


def test_extension_proposal_materials_windows_not_applicable(session_client):
    body = """
        {
            "materials":{
                "windows": {
                    "matches_existing": false,
                    "not_applicable": true
                }
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert result['materials']['windows']['matches_existing'] is False
    assert result['materials']['windows']['not_applicable'] is True


def test_extension_proposal_other_materials(session_client):
    body = """
        {
            "materials":{
                "other": [
                    "The chimney is made of diamonds",
                    "The path is made of gold."
                ]
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert "The chimney is made of diamonds" in result['materials']['other']
    assert "The path is made of gold." in result['materials']['other']


def test_posted_image_gets_saved(session_client, monkeypatch):
    here = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join('..', here, 'images', 'test-image.png')
    image = open(filepath, 'rb')
    rv = session_client.post(
        f'/api/v1/documents',
        data={
            "application_id": APPLICATION_ID,
            "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
            "existing": ID_STR,
            "proposed": ID_STR
        },
        files={
            "document": image
        },
        headers={
            'content-type': 'image/png',
            "Authorization": f"jwt {TOKEN}"
        }
    )

    assert rv.status == falcon.HTTP_CREATED
    j = json.loads(rv.body)
    assert j['id'] is not None
    assert j['original_name'] == 'test-image.png'
    assert '.png' in j['storage_path']
    assert j['document_size']['name'] == 'A1'
    assert j['document_types_existing'] != []
    assert j['document_types_existing_ids'] != []
    assert j['document_types_proposed'] != []
    assert j['document_types_proposed_ids'] != []


def test_empty_existing_str(session_client, monkeypatch):
    here = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join('..', here, 'images', 'test-image.png')
    image = open(filepath, 'rb')
    rv = session_client.post(
        f'/api/v1/documents',
        data={
            "application_id": APPLICATION_ID,
            "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
            "existing": "",
            "proposed": ID_STR
        },
        files={
            "document": image
        },
        headers={
            'content-type': 'image/png',
            "Authorization": f"jwt {TOKEN}"
        }
    )

    assert rv.status == falcon.HTTP_CREATED
    j = json.loads(rv.body)
    assert j['id'] is not None
    assert j['original_name'] == 'test-image.png'
    assert '.png' in j['storage_path']
    assert j['document_size']['name'] == 'A1'
    assert j['document_types_existing'] == []
    assert j['document_types_existing_ids'] == []
    assert j['document_types_proposed'] != []
    assert j['document_types_proposed_ids'] != []


def test_get_documents_for_application(session_client):
    rv = session_client.get(
        f'/api/v1/applications/{APPLICATION_ID}/documents',
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    print(rv.body)
    for item in j:
        assert item['original_name'] == 'test-image.png'
        assert '.png' in item['storage_path']
        assert item['document_size']['name'] == 'A1'
        assert item['document_types_proposed'] != []
        assert item['document_types_proposed_ids'] != []


def test_delete_document(session_client):
    # upload a new one first
    here = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join('..', here, 'images', 'test-image.png')
    image = open(filepath, 'rb')
    rv = session_client.post(
        f'/api/v1/documents',
        data={
            "application_id": APPLICATION_ID,
            "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
            "existing": ID_STR,
            "proposed": ID_STR
        },
        files={
            "document": image
        },
        headers={
            'content-type': 'image/png',
            "Authorization": f"jwt {TOKEN}"
        }
    )

    assert rv.status == falcon.HTTP_CREATED
    j = json.loads(rv.body)
    assert j['id'] is not None
    document_id = j['id']
    # Now delete it
    rv = session_client.delete(
        f'/api/v1/documents/{document_id}',
        headers={
            "Authorization": f"jwt {TOKEN}"
        }
    )
    assert rv is not None
    console.log(rv)
    assert _document_files.count() == 2


#

####################################################################################################
# Leave this one till last as it outputs our completed application if you pytest -s
####################################################################################################

#


def test_application_get(session_client):
    rv = session_client.get(
        f'/api/v1/applications/{APPLICATION_ID}',
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    print(rv.body)
    assert j['works_started'] is True
    assert j['date_works_started'] == "2018-01-01"
