# Introduction

## Authentication

Post form-encoded `email` and `password` to the auth endpoint and receive a JSON Web Token back.

`POST /api/v1/auth`

### Example

    email: test@example.com
    password: secretpassword

### Returns

    {
      "message": "login successful!",
      "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiZWYwY2Q5NDktMzFiYS00MjhlLWE3ZTQtMTk0MzczOWIxN2YwIn0sImlhdCI6MTU1NDQ2MDQ0MSwibmJmIjoxNTU0NDYwNDQxLCJleHAiOjE1NTQ1NDY4NDF9.4bIuU99dFXVb3nmEpohvkCl_etOJ0bDm3OT916Suyxo"
    }




## Default data

There are a bunch of endpoints that you can use to grab default data and associated ids.

```
GET /api/v1/roof-works-types
    /api/v1/works-locations
    /api/v1/basement-works-types
    /api/v1/border-works-types
    /api/v1/access-works-scopes
    /api/v1/access-works-types
    /api/v1/parking-works-scopes
    /api/v1//gate-fences-walls-types
    /api/v1/equipment-works-types
    /api/v1/equipment-works-conservation-types
    /api/v1/area-units
    /api/v1/linear-units
    /api/v1/document-sizes
    /api/v1/materials/options/roof
    /api/v1/materials/options/wall
    /api/v1/materials/options/door
    /api/v1/materials/options/window
    /api/v1/declarations
```

These all return a list along the lines of...

`GET /api/v1/border-works-types`

    [
      {
        "id": "3f1509c9-bced-41e3-b893-421b10b8c1c4",
        "created_at": "2019-04-04T20:01:02.022959",
        "updated_at": "2019-04-04T20:01:02.023000",
        "name": "Replacement and/or repair of pillar caps"
      },
      {
        "id": "e6fe2e49-db1e-481a-903c-5e133c4b8e6a",
        "created_at": "2019-04-04T20:01:02.023155",
        "updated_at": "2019-04-04T20:01:02.023187",
        "name": "Removal of an entrance"
      },
      {
        "id": "28216f89-c1a0-49ca-85b6-ac5a6cccfd0c",
        "created_at": "2019-04-04T20:01:02.023328",
        "updated_at": "2019-04-04T20:01:02.023360",
        "name": "Addition of a new entrance"
      },
      {
        "id": "ab0a8bef-1fca-43c1-97f4-70703d839f97",
        "created_at": "2019-04-04T20:01:02.023497",
        "updated_at": "2019-04-04T20:01:02.023529",
        "name": "Replacement and/or repair of wall"
      }
    ]

## Completed application output

A GET for a completed application currently returns JSON like this...

    {
      "id": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d",
      "created_at": "2019-08-05T10:41:50.294000",
      "updated_at": "2019-08-05T10:41:50.307000",
      "works_started": true,
      "date_works_started": "2018-01-01",
      "works_completed": false,
      "date_works_completed": null,
      "works_description": null,
      "free_text_description": "Praesent commodo cursus magna,\nvel scelerisque nisl consectetur et. Praesent commodo cursus\nmagna, vel scelerisque nisl consectetur et. Donec sed odio dui.\nNullam id dolor id nibh ultricies vehicula ut id elit. Cum sociis\nnatoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n",
      "ownership_declaration": true,
      "reduction_eligible": true,
      "proposalFlow": null,
      "declaration_id": "e0bbf434-9c28-4fe8-b4ae-892b3e359479",
      "declaration": {
        "id": "e0bbf434-9c28-4fe8-b4ae-892b3e359479",
        "created_at": "2019-08-05T10:41:49.094000",
        "updated_at": null,
        "name": "None of the above"
      },
      "ownership_type_id": "784e54c7-d6da-4613-ac5a-046a27278f4b",
      "ownership_type": {
        "id": "784e54c7-d6da-4613-ac5a-046a27278f4b",
        "created_at": "2019-08-05T10:41:49.097000",
        "updated_at": null,
        "name": "The applicant is the sole owner of the land"
      },
      "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
      "owner": {
        "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "created_at": "2019-08-05T10:41:49.738000",
        "updated_at": "2019-08-05T10:41:50.281000",
        "_id": "5d4807ed4d4739c881c2ac29",
        "email": "test@example.com",
        "profile_id": "ac863647-7220-4d04-b326-2c4129959b12",
        "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
        "role": {
          "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "created_at": "2019-08-05T10:41:48.937000",
          "updated_at": null,
          "name": "User"
        },
        "profile": {
          "id": "ac863647-7220-4d04-b326-2c4129959b12",
          "created_at": "2019-08-05T10:41:49.736000",
          "updated_at": null,
          "company": null,
          "name": null,
          "email_addresses": null,
          "phone": null
        },
        "verified_at": null
      },
      "site_address": {
        "id": "e53541b3-0922-4a01-8f11-78de7e3c0022",
        "created_at": "2019-08-05T10:41:50.427000",
        "updated_at": null,
        "number": null,
        "property_name": null,
        "address_line_1": "12 Stephen Mews",
        "address_line_2": null,
        "address_line_3": null,
        "town_city": "London",
        "postcode": "W1T 1AH",
        "easting": null,
        "northing": null,
        "ward": null,
        "bplu": null,
        "uprn": null,
        "property_type": null,
        "description": "Hactar Towers",
        "siteGeoJson": null,
        "application_id": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d"
      },
      "site_constraints": {
        "id": "fd14c557-bb21-4080-b4a7-793939855a31",
        "created_at": "2019-08-05T10:41:50.337000",
        "updated_at": null,
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
        "geom": null,
        "uprn": 10008300829,
        "application_id": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d"
      },
      "proposal_extension": {
        "id": "3c02fc0a-38e5-44ef-8767-f3d7b559fc84",
        "created_at": "2019-08-05T10:41:50.447000",
        "updated_at": "2019-08-05T10:41:50.451000",
        "application_id": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d",
        "original_house": {
          "id": null,
          "created_at": null,
          "updated_at": null,
          "single_storey_extension": null,
          "two_storey_extension": null,
          "part_single_part_two_storey_extension": null,
          "basement": null,
          "roof": null,
          "porch": null,
          "balcony_terrace": null,
          "staircase": null,
          "windows_doors": null,
          "cladding": {
            "id": null,
            "created_at": null,
            "updated_at": null,
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-08-05T10:41:48.940000",
                "updated_at": null,
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-08-05T10:41:48.944000",
                "updated_at": null,
                "name": "Side"
              }
            ]
          }
        },
        "incidental_buildings": {
          "id": null,
          "created_at": null,
          "updated_at": null,
          "removal_or_demolition": true,
          "details": "I'm knocking a shed down.",
          "outbuilding": null
        },
        "boundaries": {
          "id": null,
          "created_at": null,
          "updated_at": null,
          "gates_fences_walls": {
            "id": null,
            "created_at": null,
            "updated_at": null,
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-08-05T10:41:48.940000",
                "updated_at": null,
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-08-05T10:41:48.944000",
                "updated_at": null,
                "name": "Side"
              }
            ],
            "works_type_ids": [],
            "works_types": []
          },
          "border_works_type_ids": [],
          "border_works_types": []
        },
        "means_of_access": {
          "id": null,
          "created_at": null,
          "updated_at": null,
          "access_works_scope_id": "44c566ba-95dc-4cff-b0a9-53de934d309e",
          "access_works_scope": null,
          "access_works_sub_type_ids": [
            "f09b702e-c3c6-4db4-9faa-b70288176cac",
            "679143a9-0ee5-478e-984f-11c990979061"
          ],
          "access_works_sub_types": [
            {
              "id": "f09b702e-c3c6-4db4-9faa-b70288176cac",
              "created_at": "2019-08-05T10:41:49.017000",
              "updated_at": null,
              "name": "Addition of a new entrance"
            },
            {
              "id": "679143a9-0ee5-478e-984f-11c990979061",
              "created_at": "2019-08-05T10:41:49.021000",
              "updated_at": null,
              "name": "Removal of an entrance"
            }
          ]
        },
        "parking": {
          "id": null,
          "created_at": null,
          "updated_at": null,
          "parking_works_scope_id": null,
          "parking_works_scope": null,
          "current_car_parking_spaces": 0,
          "planned_car_parking_spaces": 0,
          "current_bike_parking_spaces": 0,
          "planned_bike_parking_spaces": 0,
          "new_ev_charging_points": 10
        },
        "trees": {
          "id": null,
          "created_at": null,
          "updated_at": null,
          "inside_boundry": true,
          "removed_or_pruned": true,
          "outside_boundry": true
        },
        "materials": {
          "id": null,
          "created_at": null,
          "updated_at": null,
          "definitions_in_documents": false,
          "definitions_in_form": false,
          "definitions_to_follow": false,
          "roof": null,
          "walls": null,
          "windows": null,
          "doors": null,
          "other": [
            "The chimney is made of diamonds",
            "The path is made of gold."
          ]
        },
        "additional_floor_area": 23.8,
        "additional_floor_area_units_id": "095bd097-f66e-4c66-bc1e-3521a0358e8d",
        "additional_floor_area_units": {
          "id": "095bd097-f66e-4c66-bc1e-3521a0358e8d",
          "created_at": "2019-08-05T10:41:48.846000",
          "updated_at": null,
          "name": "sq metres"
        },
        "new_single_bedrooms": 2,
        "new_double_bedrooms": 3,
        "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "owner": {
          "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
          "created_at": "2019-08-05T10:41:49.738000",
          "updated_at": "2019-08-05T10:41:50.281000",
          "_id": "5d4807ed4d4739c881c2ac29",
          "email": "test@example.com",
          "profile_id": "ac863647-7220-4d04-b326-2c4129959b12",
          "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "role": {
            "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "created_at": "2019-08-05T10:41:48.937000",
            "updated_at": null,
            "name": "User"
          },
          "profile": {
            "id": "ac863647-7220-4d04-b326-2c4129959b12",
            "created_at": "2019-08-05T10:41:49.736000",
            "updated_at": null,
            "company": null,
            "name": null,
            "email_addresses": null,
            "phone": null
          },
          "verified_at": null
        }
      },
      "proposal_equipment": {
        "id": "a0ad9926-20a1-486c-8a62-5a039f3f6b91",
        "created_at": "2019-08-05T10:41:51.228000",
        "updated_at": "2019-08-05T10:41:51.231000",
        "application_id": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d",
        "equipment": {
          "id": null,
          "created_at": null,
          "updated_at": null,
          "equipment_type_ids": [],
          "equipment_types": [],
          "equipment_conservation_type_ids": [],
          "equipment_conservation_types": [],
          "equipment_locations": [
            {
              "id": null,
              "created_at": null,
              "updated_at": null,
              "location_ids": [
                "9dc99f40-ac1d-421e-a408-c253d7ead671"
              ],
              "locations": [
                {
                  "id": "9dc99f40-ac1d-421e-a408-c253d7ead671",
                  "created_at": "2019-08-05T10:41:48.952000",
                  "updated_at": null,
                  "name": "Rear / side wrap-around"
                }
              ],
              "equipment_type_id": "Satellite dish or antenna",
              "equipment_type": null
            }
          ],
          "equipment_conservation_locations": null
        },
        "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "owner": {
          "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
          "created_at": "2019-08-05T10:41:49.738000",
          "updated_at": "2019-08-05T10:41:50.281000",
          "_id": "5d4807ed4d4739c881c2ac29",
          "email": "test@example.com",
          "profile_id": "ac863647-7220-4d04-b326-2c4129959b12",
          "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "role": {
            "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "created_at": "2019-08-05T10:41:48.937000",
            "updated_at": null,
            "name": "User"
          },
          "profile": {
            "id": "ac863647-7220-4d04-b326-2c4129959b12",
            "created_at": "2019-08-05T10:41:49.736000",
            "updated_at": null,
            "company": null,
            "name": null,
            "email_addresses": null,
            "phone": null
          },
          "verified_at": null
        }
      },
      "document_files": [
        {
          "id": "09305508-bafc-4a36-a904-b9017606075e",
          "created_at": "2019-08-05T10:41:51.785000",
          "updated_at": "2019-08-05T10:41:51.785000",
          "original_name": "test-image.png",
          "storage_path": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d/09305508-bafc-4a36-a904-b9017606075e.png",
          "application_id": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d",
          "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
          "document_size": {
            "id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
            "created_at": "2019-08-05T10:41:48.873000",
            "updated_at": null,
            "name": "A1"
          },
          "document_types_existing_ids": [
            "cbddcfc8-d062-4202-b350-f875c04c6aa0",
            "f1ff39d9-aab3-46e3-8749-dad11c04e3b8"
          ],
          "document_types_existing": [
            {
              "id": "cbddcfc8-d062-4202-b350-f875c04c6aa0",
              "created_at": "2019-08-05T10:41:48.922000",
              "updated_at": null,
              "name": "Floor plans"
            },
            {
              "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
              "created_at": "2019-08-05T10:41:48.925000",
              "updated_at": null,
              "name": "Other"
            }
          ],
          "document_types_proposed_ids": [
            "cbddcfc8-d062-4202-b350-f875c04c6aa0",
            "f1ff39d9-aab3-46e3-8749-dad11c04e3b8"
          ],
          "document_types_proposed": [
            {
              "id": "cbddcfc8-d062-4202-b350-f875c04c6aa0",
              "created_at": "2019-08-05T10:41:48.922000",
              "updated_at": null,
              "name": "Floor plans"
            },
            {
              "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
              "created_at": "2019-08-05T10:41:48.925000",
              "updated_at": null,
              "name": "Other"
            }
          ]
        },
        {
          "id": "73112739-6771-42ec-833b-1ef8a5274706",
          "created_at": "2019-08-05T10:41:51.905000",
          "updated_at": "2019-08-05T10:41:51.905000",
          "original_name": "test-image.png",
          "storage_path": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d/73112739-6771-42ec-833b-1ef8a5274706.png",
          "application_id": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d",
          "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
          "document_size": {
            "id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
            "created_at": "2019-08-05T10:41:48.873000",
            "updated_at": null,
            "name": "A1"
          },
          "document_types_existing_ids": [],
          "document_types_existing": [],
          "document_types_proposed_ids": [
            "cbddcfc8-d062-4202-b350-f875c04c6aa0",
            "f1ff39d9-aab3-46e3-8749-dad11c04e3b8"
          ],
          "document_types_proposed": [
            {
              "id": "cbddcfc8-d062-4202-b350-f875c04c6aa0",
              "created_at": "2019-08-05T10:41:48.922000",
              "updated_at": null,
              "name": "Floor plans"
            },
            {
              "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
              "created_at": "2019-08-05T10:41:48.925000",
              "updated_at": null,
              "name": "Other"
            }
          ]
        }
      ],
      "payments": [
        {
          "id": "f6591ad1-2c6c-4001-bc5c-0ff4ca55078d",
          "created_at": "2019-08-05T10:41:52.403000",
          "updated_at": "2019-08-05T10:41:52.403000",
          "amount": 10000,
          "description": "SmPA test",
          "reference": "2019/1234",
          "state": {
            "id": null,
            "created_at": null,
            "updated_at": null,
            "status": "created",
            "finished": false
          },
          "refund_summary": {
            "id": null,
            "created_at": null,
            "updated_at": null,
            "status": "pending",
            "amount_available": 10000,
            "amount_submitted": 0
          },
          "payment_id": "PID",
          "payment_provider": "sandbox",
          "created_date": "2019-07-29T15:34:21.541000+00:00",
          "settlement_summary": {
            "id": null,
            "created_at": null,
            "updated_at": null,
            "capture_submit_time": null,
            "captured_date": null
          },
          "delayed_capture": false,
          "return_url": "http://0.0.0.0:5000",
          "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
          "owner": {
            "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
            "created_at": "2019-08-05T10:41:49.738000",
            "updated_at": "2019-08-05T10:41:50.281000",
            "_id": "5d4807ed4d4739c881c2ac29",
            "email": "test@example.com",
            "profile_id": "ac863647-7220-4d04-b326-2c4129959b12",
            "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "role": {
              "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
              "created_at": "2019-08-05T10:41:48.937000",
              "updated_at": null,
              "name": "User"
            },
            "profile": {
              "id": "ac863647-7220-4d04-b326-2c4129959b12",
              "created_at": "2019-08-05T10:41:49.736000",
              "updated_at": null,
              "company": null,
              "name": null,
              "email_addresses": null,
              "phone": null
            },
            "verified_at": null
          },
          "application_id": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d"
        }
      ]
}
