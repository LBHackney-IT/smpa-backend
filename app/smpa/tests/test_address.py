import simplejson as json
import falcon
import pytest
from smpa.services.address import _addresses, _site_addresses
from .util import purger


SITE_ADDRESS_UUID = 'dcde565b-ff0b-4177-9c0b-f3d8d131ce02'


def test_address_fixture(address):
    assert address.number == "42"


def test_address_validates(address):
    assert address.validate() is None


####################################################################################################
# Test the address service
#
# Some of these are marked as slow just because they access the database.
#
####################################################################################################

@pytest.mark.slow
def test_address_save_and_get(address):
    a = _addresses.save(address)
    assert _addresses.count() == 1
    assert a.id is not None
    assert _addresses.get(a.id) is not None
    _addresses._purge()
    assert _addresses.count() == 0


@pytest.mark.slow
@purger(_addresses)
def test_address_find(address):
    a = _addresses.save(address)
    assert len(_addresses.find(number='42')) > 0
    _addresses.delete(a)
    assert _addresses.count() == 0


@purger(_addresses)
def test_new(address):
    a = _addresses.new(
        number="23",
        property_name="The Big Building",
        address_line_1="A Street",
        address_line_2="Some district",
        address_line_3="Something else",
        town_city="London",
        postcode="N1 1NN"
    )
    assert a.validate() is None


@pytest.mark.slow
def test_first():
    sa = _site_addresses.first(postcode='W1T 1AH')
    assert sa is not None
    assert sa.town_city == 'London'


@purger(_addresses)
def test_get_value_error():
    with pytest.raises(ValueError):
        _addresses.get(id=None)


@purger(_addresses)
def test_get_stringify_id():
    site_address = _site_addresses.get_or_create(
        id='dcde565b-ff0b-4177-9c0b-f3d8d131ce02'
    )

    assert site_address is not None
    site_address.address_line_1 = "12 Stephen Mews"
    site_address.town_city = "London"
    site_address.postcode = "W1T 1AH"
    site_address.description = "Hactar Towers"
    _site_addresses.save(site_address)

    import uuid
    id = uuid.UUID(SITE_ADDRESS_UUID)
    uuid_address = _site_addresses.get(id=id)
    str_address = _site_addresses.get(id=str(id))
    assert str_address is not None
    assert uuid_address is not None


@purger(_addresses)
def test_get_or_404_good():
    assert _site_addresses.get_or_404(SITE_ADDRESS_UUID) is not None


@purger(_addresses)
def test_get_or_404_bad():
    with pytest.raises(falcon.HTTPError) as e:
        res = _site_addresses.get_or_404(id='a3c09c6f-3774-4c2a-b425-3f300bc6b287')


@purger(_addresses)
def test_first_or_404_good():
    assert _site_addresses.first_or_404(SITE_ADDRESS_UUID) is not None


@purger(_addresses)
def test_first_or_404_bad():
    with pytest.raises(falcon.HTTPError) as e:
        res = _site_addresses.first_or_404(id='a3c09c6f-3774-4c2a-b425-3f300bc6b287')


@purger(_addresses)
def test_create():
    a = _addresses.create(postcode='N1 1NN')
    assert a is not None
    b = _addresses.first(postcode='N1 1NN')
    assert b is not None


@purger(_addresses)
def test_create_from_json():
    a = _addresses.create(json="""
        {
            "postcode": "N2 2NN"
        }
    """)
    assert a is not None
    b = _addresses.first(postcode='N2 2NN')
    assert b is not None


@purger(_addresses)
def test_create_multiple_from_json():
    a = _addresses.create(json="""
        [
            {
                "postcode": "N2 2NN"
            },
            {
                "postcode": "N3 3NN"
            }
        ]
    """)
    assert a is not None
    b = _addresses.first(postcode='N2 2NN')
    c = _addresses.first(postcode='N3 3NN')
    assert b is not None
    assert c is not None


@purger(_addresses)
def test_find_with_limit():
    rv = _addresses.create(json="""
        [
            {
                "property_name": "1 name",
                "postcode": "N2 2NN"
            },
            {
                "property_name": "3 name",
                "postcode": "N2 2NN"
            },
            {
                "property_name": "2 name",
                "postcode": "N2 2NN"
            }
        ]
    """)
    assert rv is not None
    a = _addresses.first(property_name='1 name')
    b = _addresses.first(property_name='2 name')
    c = _addresses.first(property_name='3 name')
    assert a is not None
    assert b is not None
    assert c is not None
    rv2 = _addresses.find(limit=1, postcode="N2 2NN")
    assert rv2 is not None
    rv3 = _addresses.find(limit=2, postcode="N2 2NN")
    assert len(rv3) == 2


@purger(_addresses)
def test_find_with_order():
    rv = _addresses.create(json="""
        [
            {
                "property_name": "1 name",
                "postcode": "N2 2NN"
            },
            {
                "property_name": "3 name",
                "postcode": "N2 2NN"
            },
            {
                "property_name": "2 name",
                "postcode": "N2 2NN"
            }
        ]
    """)
    assert rv is not None
    a = _addresses.first(property_name='1 name')
    b = _addresses.first(property_name='2 name')
    c = _addresses.first(property_name='3 name')
    assert a is not None
    assert b is not None
    assert c is not None
    rv2 = _addresses.find(order_by="property_name", postcode="N2 2NN")
    assert rv2[0].id == a.id
    assert rv2[1].id == b.id
    assert rv2[2].id == c.id


@purger(_addresses)
def test_all_with_limit():
    rv = _addresses.create(json="""
        [
            {
                "property_name": "1 name",
                "postcode": "N2 2NN"
            },
            {
                "property_name": "3 name",
                "postcode": "N2 2NN"
            },
            {
                "property_name": "2 name",
                "postcode": "N2 2NN"
            }
        ]
    """)
    assert rv is not None
    a = _addresses.first(property_name='1 name')
    b = _addresses.first(property_name='2 name')
    c = _addresses.first(property_name='3 name')
    assert a is not None
    assert b is not None
    assert c is not None
    rv2 = _addresses.all(limit=1)
    assert rv2 is not None
    rv3 = _addresses.all(limit=2)
    assert len(rv3) == 2


@purger(_addresses)
def test_all_with_order():
    rv = _addresses.create(json="""
        [
            {
                "property_name": "1 name",
                "postcode": "N2 2NN"
            },
            {
                "property_name": "3 name",
                "postcode": "N2 2NN"
            },
            {
                "property_name": "2 name",
                "postcode": "N2 2NN"
            }
        ]
    """)
    assert rv is not None
    a = _addresses.first(property_name='1 name')
    b = _addresses.first(property_name='2 name')
    c = _addresses.first(property_name='3 name')
    assert a is not None
    assert b is not None
    assert c is not None
    rv2 = _addresses.all(order_by="property_name")
    assert rv2[0].id == a.id
    assert rv2[1].id == b.id
    assert rv2[2].id == c.id


@purger(_addresses)
def test_all_with_order_reversed():
    rv = _addresses.create(json="""
        [
            {
                "property_name": "1 name",
                "postcode": "N2 2NN"
            },
            {
                "property_name": "3 name",
                "postcode": "N2 2NN"
            },
            {
                "property_name": "2 name",
                "postcode": "N2 2NN"
            }
        ]
    """)
    assert rv is not None
    a = _addresses.first(property_name='1 name')
    b = _addresses.first(property_name='2 name')
    c = _addresses.first(property_name='3 name')
    assert a is not None
    assert b is not None
    assert c is not None
    rv2 = _addresses.all(order_by=">property_name")
    assert rv2[0].id == c.id
    assert rv2[1].id == b.id
    assert rv2[2].id == a.id


@purger(_addresses)
def test_get_or_create():
    a = _addresses.first(postcode='N1 1NN')
    assert a is None
    b = _addresses.get_or_create(postcode='N1 1NN')
    assert b is not None
    rv = _addresses.find(postcode='N1 1NN')
    assert len(rv) == 1
    # c should return the address created in b
    c = _addresses.get_or_create(postcode='N1 1NN')
    assert c is not None
    rv2 = _addresses.find(postcode='N1 1NN')
    assert len(rv2) == 1


@purger(_addresses)
def test_update():
    a = _addresses.get_or_create(
        postcode='N1 1NN'
    )
    assert a is not None
    _addresses.update(id=a.id, postcode='N9 9NN')
    b = _addresses.get(a.id)
    assert b is not None
    assert b.postcode == 'N9 9NN'


@purger(_addresses)
def test_update_with_no_changes():
    a = _addresses.get_or_create(
        postcode='N1 1NN'
    )
    assert a is not None
    _addresses.update(id=a.id, postcode='N1 1NN')
    b = _addresses.get(a.id)
    assert b is not None
    assert b.postcode == 'N1 1NN'


@purger(_addresses)
def test_bad_limit_exception():
    with pytest.raises(ValueError):
        a = _addresses.get_or_create(
            postcode='N1 1NN'
        )
        _addresses.all(limit='no')


@purger(_addresses)
def test_address_geojson(site_address):
    geo = """
        {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "id": "lu_blpu_planning_constraint.100021065242",
              "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      -0.04593036,
                      51.543539
                    ],
                    [
                      -0.04596475,
                      51.54352948
                    ],
                    [
                      -0.04606828,
                      51.54350083
                    ],
                    [
                      -0.04607099,
                      51.54350492
                    ],
                    [
                      -0.04609884,
                      51.54354495
                    ],
                    [
                      -0.04603026,
                      51.54356359
                    ],
                    [
                      -0.04600761,
                      51.54357041
                    ],
                    [
                      -0.04596092,
                      51.54358312
                    ],
                    [
                      -0.04589232,
                      51.54360221
                    ],
                    [
                      -0.04585953,
                      51.54361021
                    ],
                    [
                      -0.0458274,
                      51.54361956
                    ],
                    [
                      -0.04579682,
                      51.54357589
                    ],
                    [
                      -0.04582893,
                      51.54356698
                    ],
                    [
                      -0.04593036,
                      51.543539
                    ]
                  ]
                ]
              },
              "geometry_name": "geom",
              "properties": {
                "uprn": 100021065242,
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
                "is_floodzone_3b": "0"
              }
            }
          ],
          "totalFeatures": 1,
          "numberMatched": 1,
          "numberReturned": 1,
          "timeStamp": "2019-07-05T14:10:20.720Z",
          "crs": {
            "type": "name",
            "properties": {
              "name": "urn:ogc:def:crs:EPSG::4326"
            }
          }
        }
    """
    site_address.siteGeoJson = json.loads(geo)
    _site_addresses.save(site_address)
    assert site_address.siteGeoJson is not None
    assert site_address.siteGeoJson.crs.type == 'name'


# def test_first_and_last():
#     a = _addresses.create(postcode='FIRST')
#     b = _addresses.create(postcode='LAST')
#     assert _addresses.count() == 2
#     assert _addresses.last() == b
#     assert _addresses.first() == a
