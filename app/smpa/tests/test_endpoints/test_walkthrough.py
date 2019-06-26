"""
    Test a walk through of hitting each endpoint in order.
"""

import simplejson as json
import falcon
from .test_auth import get_token
from ..util import json_match

from smpa.helpers.console import console


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

APPLICATION_ID = None
EXTENSION_PROPOSAL_ID = None
EQUIPMENT_PROPOSAL_ID = None
SITE_ADDRESS_ID = None
TOKEN = None


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


def test_walkthrough(session_client):
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
    body = """
        {
            "original_house": {},
            "incidental_buildings": {}
        }
    """
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
    body = """
        {
            "original_house": {
                "single_storey_extension": {
                    "works_location_ids": [
                        "0eee199e-5324-4180-b7a0-8100cb880a4f",
                        "2263b74c-5c76-45d8-bb99-28b4172a59d8"
                    ]
                },
                "basement": {}
            },
            "incidental_buildings": {

            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert "original_house" in j
    assert "incidental_buildings" in j


def test_extension_proposal_update_basement_work_types(session_client):
    body = """
        {
            "original_house": {
                "basement": {
                    "works_type_ids": [
                        "06a4181b-41f0-4b3f-9541-3357ff203998"
                    ]
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
    j = json.loads(rv.body)
    assert "original_house" in j
    assert "incidental_buildings" in j


def test_extension_proposal_update_basement_work_locations(session_client):
    body = """
        {
            "original_house": {
                "single_storey_extension": {
                    "works_location_ids": [
                        "165c9046-f6f2-4144-b60c-f1ca24c94054",
                        "b6b2cc59-f097-48bc-a9ad-14f263e9e036"
                    ]
                },
                "basement": {
                    "works_location_ids": [
                        "165c9046-f6f2-4144-b60c-f1ca24c94054",
                        "b6b2cc59-f097-48bc-a9ad-14f263e9e036"
                    ]
                }
            },
            "incidental_buildings": {
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/extension-proposals/{EXTENSION_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert "original_house" in j
    assert "incidental_buildings" in j


def test_extension_proposal_update_roof_work_types(session_client):
    body = """
        {
            "original_house": {
                "roof": {
                    "works_type_ids": [
                        "19ec661e-4655-4a98-9492-bf8a323607bf"
                    ]
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
    assert "19ec661e-4655-4a98-9492-bf8a323607bf" in \
        result['original_house']['roof']['works_type_ids']


def test_extension_proposal_update_roof_work_locations(session_client):
    body = """
        {
            "original_house": {
                "roof": {
                    "works_location_ids": [
                        "30d4874f-6570-403d-bfcc-d3c58cafe27e",
                        "4e9f51cb-1c24-4993-be9e-350e0d395ecb"
                    ]
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
    assert "30d4874f-6570-403d-bfcc-d3c58cafe27e" in \
        result['original_house']['roof']['works_location_ids']
    assert "4e9f51cb-1c24-4993-be9e-350e0d395ecb" in \
        result['original_house']['roof']['works_location_ids']


def test_extension_proposal_update_porch_work_locations(session_client):
    body = """
        {
            "original_house": {
                "porch": {
                    "works_location_ids": [
                        "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                    ]
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
    assert "30d4874f-6570-403d-bfcc-d3c58cafe27e" in \
        result['original_house']['porch']['works_location_ids']


def test_extension_proposal_update_balcony_work_locations(session_client):
    body = """
        {
            "original_house": {
                "balcony_terrace": {
                    "works_location_ids": [
                        "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                    ]
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
    assert "30d4874f-6570-403d-bfcc-d3c58cafe27e" in \
        result['original_house']['balcony_terrace']['works_location_ids']


def test_extension_proposal_update_staircase_work_locations(session_client):
    body = """
        {
            "original_house": {
                "staircase": {
                    "works_location_ids": [
                        "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                    ]
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
    assert "30d4874f-6570-403d-bfcc-d3c58cafe27e" in \
        result['original_house']['staircase']['works_location_ids']


def test_extension_proposal_update_windows_work_locations(session_client):
    body = """
        {
            "original_house": {
                "windows_doors": {
                    "works_location_ids": [
                        "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                    ]
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
    assert "30d4874f-6570-403d-bfcc-d3c58cafe27e" in \
        result['original_house']['windows_doors']['works_location_ids']


def test_extension_proposal_update_cladding_work_locations(session_client):
    body = """
        {
            "original_house": {
                "cladding": {
                    "works_location_ids": [
                        "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                    ]
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
    assert "30d4874f-6570-403d-bfcc-d3c58cafe27e" in \
        result['original_house']['cladding']['works_location_ids']


def test_extension_proposal_update_outbuilding_work_locations(session_client):
    body = """
        {
            "incidental_buildings": {
                "outbuilding": {
                    "works_location_ids": [
                        "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                    ]
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
    assert "30d4874f-6570-403d-bfcc-d3c58cafe27e" in \
        result['incidental_buildings']['outbuilding']['works_location_ids']


def test_extension_proposal_update_outbuilding_details(session_client):
    body = """
        {
            "incidental_buildings": {
                "removal_or_demolition": true,
                "details": "I'm knocking a shed down."
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
    assert result['incidental_buildings']['removal_or_demolition'] is True
    assert result['incidental_buildings']['details'] == "I'm knocking a shed down."


def test_extension_proposal_update_gates_fences_walls_types(session_client):
    body = """
        {
            "boundaries": {
                "gates_fences_walls": {
                    "works_type_ids": [
                        "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                    ]
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
    assert "30d4874f-6570-403d-bfcc-d3c58cafe27e" in \
        result['boundaries']['gates_fences_walls']['works_type_ids']


def test_extension_proposal_update_gates_fences_walls_locations(session_client):
    body = """
        {
            "boundaries": {
                "gates_fences_walls": {
                    "works_location_ids": [
                        "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                    ]
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
    assert "30d4874f-6570-403d-bfcc-d3c58cafe27e" in \
        result['boundaries']['gates_fences_walls']['works_location_ids']


def test_extension_proposal_update_means_of_access(session_client):
    body = """
        {
            "means_of_access": {
                "access_works_scope_id": "4c75ce90-4616-4dd0-b70a-de5ca530a37d"
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
    assert result['means_of_access']['access_works_scope_id'] \
        == "4c75ce90-4616-4dd0-b70a-de5ca530a37d"


def test_extension_proposal_update_means_of_access_subtypes(session_client):
    body = """
        {
            "means_of_access": {
                "access_works_sub_type_ids": [
                    "590a7e3d-87ab-4b44-8406-fe0fb369aa81",
                    "181deec8-d26f-4796-a036-c66528536de9"
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
    assert result['means_of_access']['access_works_scope_id'] \
        == "4c75ce90-4616-4dd0-b70a-de5ca530a37d"
    assert "590a7e3d-87ab-4b44-8406-fe0fb369aa81" in \
        result['means_of_access']['access_works_sub_type_ids']
    assert "181deec8-d26f-4796-a036-c66528536de9" in \
        result['means_of_access']['access_works_sub_type_ids']


def test_extension_proposal_update_parking_scope(session_client):
    body = """
        {
            "parking": {
                "parking_works_scope_id": "d17dea6b-20d8-46df-87d0-b41fc5ec08c3"
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
    assert result['parking']['parking_works_scope_id'] \
        == "d17dea6b-20d8-46df-87d0-b41fc5ec08c3"


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
    body = """
        {
            "equipment":{
                "equipment_type_ids": [
                    "b36079c1-dc9f-4225-a94d-b7c54c83b86e",
                    "cc70f42f-dc59-4a03-bf7e-fbb2e7ff3b5b",
                    "fa6f8957-a775-4dc0-adfc-4c3ddfd42698"
                ],
                "equipment_conservation_type_ids": [
                    "4b2aa4a1-e01e-49ff-aedc-ddd638695839",
                    "9f9390fa-f175-4d7a-8599-48c40644f0c3",
                    "510e6d41-168d-45e6-ad7e-329a578961d2"
                ]
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/equipment-proposals/{EQUIPMENT_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert "b36079c1-dc9f-4225-a94d-b7c54c83b86e" in \
        result['equipment']['equipment_type_ids']
    assert "cc70f42f-dc59-4a03-bf7e-fbb2e7ff3b5b" in \
        result['equipment']['equipment_type_ids']
    assert "fa6f8957-a775-4dc0-adfc-4c3ddfd42698" in \
        result['equipment']['equipment_type_ids']
    assert "4b2aa4a1-e01e-49ff-aedc-ddd638695839" in \
        result['equipment']['equipment_conservation_type_ids']
    assert "9f9390fa-f175-4d7a-8599-48c40644f0c3" in \
        result['equipment']['equipment_conservation_type_ids']
    assert "510e6d41-168d-45e6-ad7e-329a578961d2" in \
        result['equipment']['equipment_conservation_type_ids']


def test_equipment_proposal_update_locations(session_client):
    body = """
        {
            "equipment": {
                "equipment_locations": [
                    {
                        "location_ids": [
                            "b36079c1-dc9f-4225-a94d-b7c54c83b86e"
                        ],
                        "equipment_type_id": "9dc99f40-ac1d-421e-a408-c253d7ead671"
                    }
                ]
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/equipment-proposals/{EQUIPMENT_PROPOSAL_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    result = json.loads(rv.body)
    assert "b36079c1-dc9f-4225-a94d-b7c54c83b86e" in \
        result['equipment']['equipment_locations'][0]['location_ids']


def test_extension_proposal_floor_area(session_client):
    body = """
        {
            "additional_floor_area": 23.8,
            "additional_floor_area_units_id": "095bd097-f66e-4c66-bc1e-3521a0358e8d"
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
    body = """
        {
            "materials":{
                "roof": {
                    "proposals": [
                        {
                            "material_id": "d470020f-984f-4acf-9e75-387f58db4604",
                            "colour_and_type": "Some lovely green roof tiles."
                        }
                    ]
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
    print(rv.body)
    assert result['materials']['roof']['proposals'][0]['material_id'] == \
        "d470020f-984f-4acf-9e75-387f58db4604"
    assert result['materials']['roof']['proposals'][0]['colour_and_type'] == \
        "Some lovely green roof tiles."
