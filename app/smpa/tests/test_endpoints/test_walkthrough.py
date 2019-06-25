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
