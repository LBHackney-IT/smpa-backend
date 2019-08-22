"""
    Test a walk through of hitting each endpoint in order.
"""

import re
import os
import arrow
import pytest
import responses

from schematics.exceptions import DataError
import simplejson as json
import falcon

from .test_auth import get_token
from ..util import json_match, reset_test_user

from smpa.services.document import _document_files
from smpa.services.application import _applications
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
    SUPERADMIN_USERS,
    DECLARATIONS,
    OWNERSHIP_TYPES,
    APPLICATION_STATUSES
)

TEXT_BLOB = """Praesent commodo cursus magna,
vel scelerisque nisl consectetur et. Praesent commodo cursus
magna, vel scelerisque nisl consectetur et. Donec sed odio dui.
Nullam id dolor id nibh ultricies vehicula ut id elit. Cum sociis
natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
"""

CHECK_PAYMENT_RESPONSE = {
    'amount': 1200,
    'description': 'Your Service Description',
    'reference': 'your-reference',
    'language': 'en',
    'metadata': {
        'property1': 'string',
        'property2': 'string'
    },
    'email': 'your email',
    'state': {
        'status': 'created',
        'finished': True,
        'message': 'User cancelled the payment',
        'code': 'P010'
    },
    'payment_id': 'hu20sqlact5260q2nanm0q8u93',
    'payment_provider': 'worldpay',
    'created_date': '2016-01-21T17:15:000Z',
    'refund_summary': {
        'status': 'available',
        'amount_available': 100,
        'amount_submitted': 0
    },
    'settlement_summary': {
        'capture_submit_time': '2016-01-21T17:15:000Z',
        'captured_date': '2016-01-21'
    },
    'card_details': {
        'last_digits_card_number': '1234',
        'first_digits_card_number': '123456',
        'cardholder_name': 'Mr. Card holder',
        'expiry_date': '12/20',
        'billing_address': {
            'line1': 'address line 1',
            'line2': 'address line 2',
            'postcode': 'AB1 2CD',
            'city': 'address city',
            'country': 'GB'
        },
        'card_brand': 'Visa'
    },
    'delayed_capture': False,
    'corporate_card_surcharge': 250,
    'total_amount': 1450,
    'fee': 5,
    'net_amount': 1195,
    'provider_id': 'reference-from-payment-gateway',
    'return_url': 'http://your.service.domain/your-reference',
    '_links': {
        'self': {
            'href': 'https://an.example.link/from/payment/platform',
            'method': 'GET'
        },
        'next_url': {
            'href': 'https://an.example.link/from/payment/platform',
            'method': 'GET'
        },
        'next_url_post': {
            'type': 'application/x-www-form-urlencoded',
            'params': {
                'description':
                'This is a value for a parameter called description'
            },
            'href': 'https://an.example.link/from/payment/platform',
            'method': 'POST'
        },
        'events': {
            'href': 'https://an.example.link/from/payment/platform',
            'method': 'GET'
        },
        'refunds': {
            'href': 'https://an.example.link/from/payment/platform',
            'method': 'GET'
        },
        'cancel': {
            'type': 'application/x-www-form-urlencoded',
            'params': {
                'description':
                'This is a value for a parameter called description'
            },
            'href': 'https://an.example.link/from/payment/platform',
            'method': 'POST'
        },
        'capture': {
            'type': 'application/x-www-form-urlencoded',
            'params': {
                'description':
                'This is a value for a parameter called description'
            },
            'href': 'https://an.example.link/from/payment/platform',
            'method': 'POST'
        }
    },
    'card_brand': 'Visa'
}

CREATE_PAYMENT_FAILURE_RESPONSE = {
    "field": "amount",
    "code": "P0102",
    "description": "Invalid attribute value: amount. Must be less than or equal to 10000000"
}

CREATE_PAYMENT_SUCCESS_RESPONSE = {
    'amount': 10000,
    'description': 'SmPA test',
    'reference': '2019/1234',
    'language': 'en',
    'state': {
        'status': 'created',
        'finished': False
    },
    'payment_id': 'PID',
    'payment_provider': 'sandbox',
    'created_date': '2019-07-29T15:34:21.541Z',
    'refund_summary': {
        'status': 'pending',
        'amount_available': 10000,
        'amount_submitted': 0
    },
    'settlement_summary': {},
    'delayed_capture': False,
    'return_url': 'http://0.0.0.0:5000',
    '_links': {
        'self': {
            'href': 'https://publicapi.payments.service.gov.uk/v1/payments/PID',
            'method': 'GET'
        },
        'next_url': {
            'href': 'https://www.payments.service.gov.uk/secure/SOME_UUID',
            'method': 'GET'
        },
        'next_url_post': {
            'type': 'application/x-www-form-urlencoded',
            'params': {
                'chargeTokenId': 'b7d609cc-1ebb-42cf-bd27-e9b0ef227d8a'
            },
            'href': 'https://www.payments.service.gov.uk/secure',
            'method': 'POST'
        },
        'events': {
            'href': 'https://publicapi.payments.service.gov.uk/v1/payments/PID/events',
            'method': 'GET'
        },
        'refunds': {
            'href': 'https://publicapi.payments.service.gov.uk/v1/payments/PID/refunds',
            'method': 'GET'
        },
        'cancel': {
            'href': 'https://publicapi.payments.service.gov.uk/v1/payments/PID/cancel',
            'method': 'POST'
        }
    }
}

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
    "/api/v1/application-statuses",
]

ID_STR = "cbddcfc8-d062-4202-b350-f875c04c6aa0,f1ff39d9-aab3-46e3-8749-dad11c04e3b8"
APPLICATION_ID = None
ADMIN_APPLICATION_ID = None
EXTENSION_PROPOSAL_ID = None
EQUIPMENT_PROPOSAL_ID = None
SITE_ADDRESS_ID = None
TOKEN = None
PAYMENT_ID = None


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


def test_application_update_bad_date(session_client):
    with pytest.raises(DataError):
        body = """
            {
                "works_started": true,
                "date_works_started": "118-13-01"
            }
        """
        rv = session_client.patch(
            f'/api/v1/applications/{APPLICATION_ID}',
            body,
            headers={"Authorization": f"jwt {TOKEN}"}
        )


def test_bad_date_is_not_saved(session_client):
    rv = session_client.get(
        f'/api/v1/applications/{APPLICATION_ID}',
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
            "equipment": {
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


def test_equipment_proposal_update_scope_anas_payload(session_client):
    body = json.dumps(
        {
            "equipment": {
                "equipment_type_ids": [
                    "fa6f8957-a775-4dc0-adfc-4c3ddfd42698"
                ],
                "equipment_conservation_type_ids": [
                    "4b2aa4a1-e01e-49ff-aedc-ddd638695839"
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
    assert result['equipment']['equipment_type_ids'] == ["fa6f8957-a775-4dc0-adfc-4c3ddfd42698"]
    assert result['equipment']['equipment_conservation_type_ids'] == \
        ["4b2aa4a1-e01e-49ff-aedc-ddd638695839"]


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
                "inside_boundary": true,
                "removed_or_pruned": true,
                "outside_boundary": true
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
    assert result['trees']['inside_boundary'] is True
    assert result['trees']['removed_or_pruned'] is True
    assert result['trees']['outside_boundary'] is True


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


def test_application_update_declaration(session_client):
    body = """
        {
            "declaration_id": "e0bbf434-9c28-4fe8-b4ae-892b3e359479"
        }
    """
    rv = session_client.patch(
        f'/api/v1/applications/{APPLICATION_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['declaration_id'] == "e0bbf434-9c28-4fe8-b4ae-892b3e359479"
    assert j['declaration'] is not None
    assert j['declaration']['name'] == "None of the above"


def test_application_update_declaration_with_details(session_client):
    body = """
        {
            "declaration_id": "746b41c8-54b3-4cd6-89d7-2d41d1c55fbe",
            "declaration_detail": {
                "name": "Sido Jombati",
                "role": "Defender",
                "details": "Everyone's favourite defender"
            }
        }
    """
    rv = session_client.patch(
        f'/api/v1/applications/{APPLICATION_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['declaration_id'] == "746b41c8-54b3-4cd6-89d7-2d41d1c55fbe"
    assert j['declaration'] is not None
    assert j['declaration']['name'] == "You are a Hackney Council member of staff"
    assert j['declaration_detail']['name'] == 'Sido Jombati'
    assert j['declaration_detail']['role'] == 'Defender'
    assert j['declaration_detail']['details'] == "Everyone's favourite defender"


def test_application_update_ownership(session_client):
    body = """
        {
            "ownership_type_id": "784e54c7-d6da-4613-ac5a-046a27278f4b"
        }
    """
    rv = session_client.patch(
        f'/api/v1/applications/{APPLICATION_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['ownership_type_id'] == "784e54c7-d6da-4613-ac5a-046a27278f4b"
    assert j['ownership_type'] is not None
    assert j['ownership_type']['name'] == "The applicant is the sole owner of the land"


def test_application_update_ownership_declaration(session_client):
    body = json.dumps(
        {
            "ownership_declaration": True
        }
    )
    rv = session_client.patch(
        f'/api/v1/applications/{APPLICATION_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['ownership_declaration'] is True


def test_add_agent(session_client):
    body = json.dumps(
        {
            "agent": {
                "full_name": "Mr Secret Agent",
                "company": "CIA",
                "address_line_1": "1 Some Street",
                "address_line_2": "",
                "town_city": "London",
                "postcode": "N1 1NN",
                "phone": "01234567890",
                "email": "agent@example.com"
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/applications/{APPLICATION_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['agent'] is not None
    assert j['agent']["full_name"] == "Mr Secret Agent"
    assert j['agent']["company"] == "CIA"
    assert j['agent']["address_line_1"] == "1 Some Street"
    assert j['agent']["address_line_2"] == ""
    assert j['agent']["town_city"] == "London"
    assert j['agent']["postcode"] == "N1 1NN"
    assert j['agent']["phone"] == "01234567890"
    assert j['agent']["email"] == "agent@example.com"


def test_add_applicant(session_client):
    body = json.dumps(
        {
            "applicant": {
                "full_name": "Mr A Plicant",
                "company": "Hactar",
                "address_line_1": "1 Some Street",
                "address_line_2": "",
                "town_city": "London",
                "postcode": "N1 1NN",
                "phone": "01234567890",
                "email": "applicant@example.com"
            }
        }
    )
    rv = session_client.patch(
        f'/api/v1/applications/{APPLICATION_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['applicant'] is not None
    assert j['applicant']["full_name"] == "Mr A Plicant"
    assert j['applicant']["company"] == "Hactar"
    assert j['applicant']["address_line_1"] == "1 Some Street"
    assert j['applicant']["address_line_2"] == ""
    assert j['applicant']["town_city"] == "London"
    assert j['applicant']["postcode"] == "N1 1NN"
    assert j['applicant']["phone"] == "01234567890"
    assert j['applicant']["email"] == "applicant@example.com"


def test_application_update_reduction_eligible(session_client):
    body = json.dumps(
        {
            "reduction_eligible": True
        }
    )
    rv = session_client.patch(
        f'/api/v1/applications/{APPLICATION_ID}',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['reduction_eligible'] is True


@responses.activate
def test_create_payment(session_client):
    from smpa.services import _applications
    global PAYMENT_ID
    responses.add(
        responses.POST,
        'https://publicapi.payments.service.gov.uk/v1/payments',
        json=CREATE_PAYMENT_SUCCESS_RESPONSE,
        status=201
    )
    rv = session_client.post(
        f'/api/v1/applications/{APPLICATION_ID}/payments',
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_CREATED
    j = json.loads(rv.body)
    assert j['id'] is not None
    PAYMENT_ID = j['id']
    assert j['application_id'] is not None
    assert j['owner_id'] is not None
    assert j['owner']['email'] == 'test@example.com'
    assert j['next_url'] == 'https://www.payments.service.gov.uk/secure/SOME_UUID'
    a = _applications.get(j['application_id'])
    assert 'DRAFT' not in a.reference


@responses.activate
def test_create_payment_failure(session_client):
    responses.add(
        responses.POST,
        'https://publicapi.payments.service.gov.uk/v1/payments',
        json=CREATE_PAYMENT_FAILURE_RESPONSE,
        status=401
    )
    rv = session_client.post(
        f'/api/v1/applications/{APPLICATION_ID}/payments',
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status != falcon.HTTP_CREATED
    j = json.loads(rv.body)
    assert j['title']['success'] is False
    assert j['title']['message'] == CREATE_PAYMENT_FAILURE_RESPONSE['description']
    assert j['title']['code'] == CREATE_PAYMENT_FAILURE_RESPONSE['code']


def test_get_payments(session_client):
    rv = session_client.get(
        f'/api/v1/payments',
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j is not None
    assert j[0]['id'] is not None
    assert j[0]['application_id'] is not None
    assert j[0]['owner_id'] is not None
    assert j[0]['owner']['email'] == 'test@example.com'
    assert j[0]['next_url'] == 'https://www.payments.service.gov.uk/secure/SOME_UUID'


def test_get_payments_for_application(session_client):
    rv = session_client.get(
        f'/api/v1/applications/{APPLICATION_ID}/payments',
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j is not None
    assert j[0]['id'] is not None
    assert j[0]['application_id'] is not None
    assert j[0]['owner_id'] is not None
    assert j[0]['owner']['email'] == 'test@example.com'
    assert j[0]['next_url'] == 'https://www.payments.service.gov.uk/secure/SOME_UUID'


@responses.activate
def test_check_payment_status(session_client):
    comp = re.compile(r'^https://publicapi.payments.service.gov.uk/v1/payments/[a-zA-Z0-9]*$')
    responses.add(
        responses.GET,
        comp,
        json=CHECK_PAYMENT_RESPONSE,
        status=200
    )
    rv = session_client.get(
        f'/api/v1/payments/{PAYMENT_ID}/check',
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['id'] is not None
    assert j['application_id'] is not None
    assert j['owner_id'] is not None
    assert j['owner']['email'] == 'test@example.com'
    assert j['state']['finished'] is True


@responses.activate
def test_submit_application(session_client):
    from .test_auth import SEND_VERIFICATION_EMAIL_RESPONSE
    responses.add(
        responses.POST,
        'https://api.notifications.service.gov.uk/v2/notifications/email',
        json=SEND_VERIFICATION_EMAIL_RESPONSE,
        status=200
    )
    body = json.dumps(
        {
            "submitted": True
        }
    )
    rv = session_client.patch(
        f'/api/v1/applications/{APPLICATION_ID}/submit',
        body,
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['submitted_at'] is not None


RESET_TOKEN = None


@responses.activate
def test_trigger_password_reset(session_client):
    global RESET_TOKEN
    from .test_auth import SEND_VERIFICATION_EMAIL_RESPONSE
    from smpa.services.user import _users
    responses.add(
        responses.POST,
        'https://api.notifications.service.gov.uk/v2/notifications/email',
        json=SEND_VERIFICATION_EMAIL_RESPONSE,
        status=200
    )
    body = json.dumps(
        {
            "email": "test@example.com"
        }
    )
    rv = session_client.post(
        f'/api/v1/users/reset-password',
        body
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['message'] == 'Password reset initiated'
    u = _users.first(email='test@example.com')
    assert u.reset_token is not None
    assert arrow.get(u.reset_token_expires) > arrow.now()
    RESET_TOKEN = str(u.reset_token)


def test_confirm_reset_password_mismatched(session_client):
    from smpa.services.user import _users
    global RESET_TOKEN
    body = json.dumps(
        {
            "token": str(RESET_TOKEN),
            "password": "newpassword",
            "password_confirm": "mismatched"
        }
    )
    rv = session_client.post(
        f'/api/v1/users/reset-password',
        body
    )
    assert rv.status == falcon.HTTP_422
    j = json.loads(rv.body)
    assert j['title'] == 'Passwords do not match'
    u = _users.first(email='test@example.com')
    assert u.reset_token is not None
    assert u.reset_token_expires is not None


def test_confirm_reset_password(session_client):
    from smpa.services.user import _users
    global RESET_TOKEN
    body = json.dumps(
        {
            "token": str(RESET_TOKEN),
            "password": "newpassword",
            "password_confirm": "newpassword"
        }
    )
    rv = session_client.post(
        f'/api/v1/users/reset-password',
        body
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert j['message'] == 'Password reset successful'
    u = _users.first(email='test@example.com')
    assert u.reset_token is None
    assert u.reset_token_expires is None


def test_login_with_new_password(session_client):
    rv = session_client.post(
        '/api/v1/auth',
        {
            'email': 'test@example.com',
            'password': 'newpassword'
        }
    )
    assert rv.status == falcon.HTTP_OK


def test_create_as_different_user(session_client):
    global ADMIN_APPLICATION_ID
    token = get_token(email='systems@hactar.is')
    rv = session_client.post(
        '/api/v1/applications',
        "{}",
        headers={"Authorization": f"jwt {token}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    ADMIN_APPLICATION_ID = j['id']
    assert ADMIN_APPLICATION_ID is not None
    assert j['owner_id'] is not None


def test_get_applications_not_admin(session_client):
    rv = session_client.get(
        '/api/v1/applications',
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert len(j) == 2
    assert ADMIN_APPLICATION_ID not in j


def test_get_applications_admin(session_client):
    token = get_token(email='systems@hactar.is')
    rv = session_client.get(
        '/api/v1/applications',
        headers={"Authorization": f"jwt {token}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert len(j) == 3
    assert ADMIN_APPLICATION_ID not in j

#

#####################################################################################
# Leave this one till last as it outputs our completed application if you pytest -s #
#####################################################################################

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


def test_deleting_an_application_doesnt_give_404s(session_client):
    init_count = _applications.count()
    _applications.delete_by_id(ADMIN_APPLICATION_ID)
    assert _applications.count() == init_count - 1
    # GET them as an admin user
    token = get_token(email='systems@hactar.is')
    rv = session_client.get(
        '/api/v1/applications',
        headers={"Authorization": f"jwt {token}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert len(j) == init_count - 1
    rv = session_client.get(
        '/api/v1/applications',
        headers={"Authorization": f"jwt {TOKEN}"}
    )
    assert rv.status == falcon.HTTP_OK
    j = json.loads(rv.body)
    assert len(j) == init_count - 1
