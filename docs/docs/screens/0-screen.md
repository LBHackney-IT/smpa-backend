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
      "id": "e7c134ed-16d7-4df7-a7e2-ee02ec16d0c5",
      "created_at": "2019-07-04T10:06:57.037074",
      "updated_at": "2019-07-04T10:06:57.037114",
      "works_started": true,
      "date_works_started": "2018-01-01",
      "works_completed": false,
      "date_works_completed": null,
      "works_description": null,
      "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
      "owner": {
        "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "created_at": "2019-07-04T10:07:21.646454",
        "updated_at": "2019-07-04T10:07:21.646476",
        "email": "test@example.com",
        "profile_id": "4de4485a-dac8-486d-bf2c-817314df39df",
        "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
        "role": {
          "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "created_at": "2019-07-04T10:07:21.700707",
          "updated_at": "2019-07-04T10:07:21.700747",
          "name": "User"
        },
        "profile": {
          "id": "4de4485a-dac8-486d-bf2c-817314df39df",
          "created_at": "2019-07-04T10:07:21.675728",
          "updated_at": "2019-07-04T10:07:21.675767",
          "name": null,
          "preferred_contact_method": null,
          "email_addresses": null,
          "primary_email_id": null,
          "primary_phone_id": null
        }
      },
      "site_address": {
        "id": "fd7593b5-e161-4047-8866-9ff6195eb33a",
        "created_at": "2019-07-04T10:07:21.492670",
        "updated_at": "2019-07-04T10:07:21.492718",
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
        "application_id": "e7c134ed-16d7-4df7-a7e2-ee02ec16d0c5"
      },
      "site_constraints": null,
      "proposal_extension": {
        "id": "4c9aede3-2af8-4619-8938-96107def5daa",
        "created_at": "2019-07-04T10:06:58.161362",
        "updated_at": "2019-07-04T10:06:58.161389",
        "application_id": "e7c134ed-16d7-4df7-a7e2-ee02ec16d0c5",
        "original_house": {
          "id": null,
          "created_at": "2019-07-04T10:07:21.577135",
          "updated_at": "2019-07-04T10:07:21.577169",
          "single_storey_extension": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.577276",
            "updated_at": "2019-07-04T10:07:21.577306",
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-07-04T10:07:21.725033",
                "updated_at": "2019-07-04T10:07:21.725067",
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-07-04T10:07:21.755490",
                "updated_at": "2019-07-04T10:07:21.755517",
                "name": "Side"
              }
            ]
          },
          "two_storey_extension": null,
          "part_single_part_two_storey_extension": null,
          "basement": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.577493",
            "updated_at": "2019-07-04T10:07:21.577523",
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-07-04T10:07:21.776162",
                "updated_at": "2019-07-04T10:07:21.776200",
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-07-04T10:07:21.800683",
                "updated_at": "2019-07-04T10:07:21.800723",
                "name": "Side"
              }
            ],
            "works_type_ids": [
              "c1d2ba2b-78d3-4826-80e1-517a90b448fd"
            ],
            "works_types": [
              {
                "id": "c1d2ba2b-78d3-4826-80e1-517a90b448fd",
                "created_at": "2019-07-04T10:07:21.823816",
                "updated_at": "2019-07-04T10:07:21.823848",
                "name": "Excavation of a new basement"
              }
            ]
          },
          "roof": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.577691",
            "updated_at": "2019-07-04T10:07:21.577720",
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-07-04T10:07:21.846241",
                "updated_at": "2019-07-04T10:07:21.846275",
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-07-04T10:07:21.866644",
                "updated_at": "2019-07-04T10:07:21.866679",
                "name": "Side"
              }
            ],
            "works_type_ids": [
              "f7adf884-760a-4896-9202-0f36394c191c"
            ],
            "works_types": [
              {
                "id": "f7adf884-760a-4896-9202-0f36394c191c",
                "created_at": "2019-07-04T10:07:21.888240",
                "updated_at": "2019-07-04T10:07:21.888274",
                "name": "Addition of a dormer extension"
              }
            ]
          },
          "porch": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.577886",
            "updated_at": "2019-07-04T10:07:21.577916",
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-07-04T10:07:21.908439",
                "updated_at": "2019-07-04T10:07:21.908471",
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-07-04T10:07:21.928424",
                "updated_at": "2019-07-04T10:07:21.928457",
                "name": "Side"
              }
            ]
          },
          "balcony_terrace": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.578055",
            "updated_at": "2019-07-04T10:07:21.578085",
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-07-04T10:07:21.949400",
                "updated_at": "2019-07-04T10:07:21.949434",
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-07-04T10:07:21.969727",
                "updated_at": "2019-07-04T10:07:21.969761",
                "name": "Side"
              }
            ]
          },
          "staircase": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.578222",
            "updated_at": "2019-07-04T10:07:21.578252",
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-07-04T10:07:21.990479",
                "updated_at": "2019-07-04T10:07:21.990511",
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-07-04T10:07:22.010685",
                "updated_at": "2019-07-04T10:07:22.010717",
                "name": "Side"
              }
            ]
          },
          "windows_doors": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.578390",
            "updated_at": "2019-07-04T10:07:21.578420",
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-07-04T10:07:22.032025",
                "updated_at": "2019-07-04T10:07:22.032058",
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-07-04T10:07:22.059599",
                "updated_at": "2019-07-04T10:07:22.059633",
                "name": "Side"
              }
            ]
          },
          "cladding": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.578557",
            "updated_at": "2019-07-04T10:07:21.578587",
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-07-04T10:07:22.083340",
                "updated_at": "2019-07-04T10:07:22.083380",
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-07-04T10:07:22.106370",
                "updated_at": "2019-07-04T10:07:22.106403",
                "name": "Side"
              }
            ]
          }
        },
        "incidental_buildings": {
          "id": null,
          "created_at": "2019-07-04T10:07:21.578775",
          "updated_at": "2019-07-04T10:07:21.578805",
          "removal_or_demolition": true,
          "details": "I'm knocking a shed down.",
          "outbuilding": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.578917",
            "updated_at": "2019-07-04T10:07:21.578947",
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-07-04T10:07:22.128415",
                "updated_at": "2019-07-04T10:07:22.128448",
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-07-04T10:07:22.149778",
                "updated_at": "2019-07-04T10:07:22.149813",
                "name": "Side"
              }
            ]
          }
        },
        "boundaries": {
          "id": null,
          "created_at": "2019-07-04T10:07:21.579115",
          "updated_at": "2019-07-04T10:07:21.579145",
          "gates_fences_walls": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.579242",
            "updated_at": "2019-07-04T10:07:21.579271",
            "works_location_ids": [
              "66d1b304-5729-4654-91df-d6306e249e54",
              "4f464424-ca54-4bc4-b980-c5d957a5ad1a"
            ],
            "works_locations": [
              {
                "id": "66d1b304-5729-4654-91df-d6306e249e54",
                "created_at": "2019-07-04T10:07:22.176342",
                "updated_at": "2019-07-04T10:07:22.176379",
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-07-04T10:07:22.197889",
                "updated_at": "2019-07-04T10:07:22.197924",
                "name": "Side"
              }
            ],
            "works_type_ids": [
              "3f583868-33bb-4296-b924-2903f4d6ec1b"
            ],
            "works_types": [
              {
                "id": "3f583868-33bb-4296-b924-2903f4d6ec1b",
                "created_at": "2019-07-04T10:07:22.219916",
                "updated_at": "2019-07-04T10:07:22.219957",
                "name": "Addition of a new gate"
              }
            ]
          },
          "border_works_type_ids": [],
          "border_works_types": []
        },
        "means_of_access": {
          "id": null,
          "created_at": "2019-07-04T10:07:21.579488",
          "updated_at": "2019-07-04T10:07:21.579517",
          "access_works_scope_id": "44c566ba-95dc-4cff-b0a9-53de934d309e",
          "access_works_scope": null,
          "access_works_sub_type_ids": [
            "f09b702e-c3c6-4db4-9faa-b70288176cac",
            "679143a9-0ee5-478e-984f-11c990979061"
          ],
          "access_works_sub_types": [
            {
              "id": "f09b702e-c3c6-4db4-9faa-b70288176cac",
              "created_at": "2019-07-04T10:07:22.270783",
              "updated_at": "2019-07-04T10:07:22.270817",
              "name": "Addition of a new entrance"
            },
            {
              "id": "679143a9-0ee5-478e-984f-11c990979061",
              "created_at": "2019-07-04T10:07:22.292078",
              "updated_at": "2019-07-04T10:07:22.292112",
              "name": "Removal of an entrance"
            }
          ]
        },
        "parking": {
          "id": null,
          "created_at": "2019-07-04T10:07:21.579689",
          "updated_at": "2019-07-04T10:07:21.579719",
          "parking_works_scope_id": "c4358d0e-c649-4b48-9a05-405d6ee90c0c",
          "parking_works_scope": null,
          "current_car_parking_spaces": 10,
          "planned_car_parking_spaces": 20,
          "current_bike_parking_spaces": 10,
          "planned_bike_parking_spaces": 20,
          "new_ev_charging_points": 10
        },
        "trees": {
          "id": null,
          "created_at": "2019-07-04T10:07:21.579911",
          "updated_at": "2019-07-04T10:07:21.579941",
          "inside_boundry": true,
          "removed_or_pruned": true,
          "outside_boundry": true
        },
        "materials": {
          "id": null,
          "created_at": "2019-07-04T10:07:21.580095",
          "updated_at": "2019-07-04T10:07:21.580125",
          "definitions_in_documents": false,
          "definitions_in_form": true,
          "definitions_to_follow": false,
          "roof": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.580535",
            "updated_at": "2019-07-04T10:07:21.580566",
            "proposals": [
              {
                "id": null,
                "created_at": "2019-07-04T10:07:21.580679",
                "updated_at": "2019-07-04T10:07:21.580709",
                "colour_and_type": "Some lovely green roof tiles.",
                "material_id": "d470020f-984f-4acf-9e75-387f58db4604",
                "material": {
                  "id": "d470020f-984f-4acf-9e75-387f58db4604",
                  "created_at": "2019-07-04T10:07:22.341402",
                  "updated_at": "2019-07-04T10:07:22.341440",
                  "name": "Tiles"
                }
              }
            ],
            "matches_existing": false,
            "not_applicable": false
          },
          "walls": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.580910",
            "updated_at": "2019-07-04T10:07:21.580940",
            "proposals": null,
            "matches_existing": true,
            "not_applicable": false
          },
          "windows": {
            "id": null,
            "created_at": "2019-07-04T10:07:21.581093",
            "updated_at": "2019-07-04T10:07:21.581123",
            "proposals": null,
            "matches_existing": false,
            "not_applicable": true
          },
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
          "created_at": "2019-07-04T10:07:22.365581",
          "updated_at": "2019-07-04T10:07:22.365616",
          "name": "sq metres"
        },
        "new_single_bedrooms": 2,
        "new_double_bedrooms": 3,
        "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "owner": {
          "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
          "created_at": "2019-07-04T10:07:22.386475",
          "updated_at": "2019-07-04T10:07:22.386509",
          "email": "test@example.com",
          "profile_id": "4de4485a-dac8-486d-bf2c-817314df39df",
          "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "role": {
            "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "created_at": "2019-07-04T10:07:22.426890",
            "updated_at": "2019-07-04T10:07:22.426923",
            "name": "User"
          },
          "profile": {
            "id": "4de4485a-dac8-486d-bf2c-817314df39df",
            "created_at": "2019-07-04T10:07:22.407112",
            "updated_at": "2019-07-04T10:07:22.407146",
            "name": null,
            "preferred_contact_method": null,
            "email_addresses": null,
            "primary_email_id": null,
            "primary_phone_id": null
          }
        }
      },
      "proposal_equipment": {
        "id": "01c478b8-445e-4a75-b868-2d56a18688a4",
        "created_at": "2019-07-04T10:07:12.465808",
        "updated_at": "2019-07-04T10:07:12.465848",
        "application_id": "e7c134ed-16d7-4df7-a7e2-ee02ec16d0c5",
        "equipment": {
          "id": null,
          "created_at": "2019-07-04T10:07:21.622281",
          "updated_at": "2019-07-04T10:07:21.622316",
          "equipment_type_ids": [
            "fa6f8957-a775-4dc0-adfc-4c3ddfd42698",
            "cc70f42f-dc59-4a03-bf7e-fbb2e7ff3b5b",
            "b36079c1-dc9f-4225-a94d-b7c54c83b86e"
          ],
          "equipment_types": [
            {
              "id": "fa6f8957-a775-4dc0-adfc-4c3ddfd42698",
              "created_at": "2019-07-04T10:07:22.448744",
              "updated_at": "2019-07-04T10:07:22.448770",
              "name": "Satellite dish or antenna"
            },
            {
              "id": "cc70f42f-dc59-4a03-bf7e-fbb2e7ff3b5b",
              "created_at": "2019-07-04T10:07:22.471248",
              "updated_at": "2019-07-04T10:07:22.471287",
              "name": "Air conditioning unit"
            },
            {
              "id": "b36079c1-dc9f-4225-a94d-b7c54c83b86e",
              "created_at": "2019-07-04T10:07:22.496336",
              "updated_at": "2019-07-04T10:07:22.496379",
              "name": "Tank"
            }
          ],
          "equipment_conservation_type_ids": [
            "4b2aa4a1-e01e-49ff-aedc-ddd638695839",
            "510e6d41-168d-45e6-ad7e-329a578961d2",
            "9f9390fa-f175-4d7a-8599-48c40644f0c3"
          ],
          "equipment_conservation_types": [
            {
              "id": "4b2aa4a1-e01e-49ff-aedc-ddd638695839",
              "created_at": "2019-07-04T10:07:22.520522",
              "updated_at": "2019-07-04T10:07:22.520573",
              "name": "CCTV"
            },
            {
              "id": "510e6d41-168d-45e6-ad7e-329a578961d2",
              "created_at": "2019-07-04T10:07:22.542016",
              "updated_at": "2019-07-04T10:07:22.542042",
              "name": "Security alarm"
            },
            {
              "id": "9f9390fa-f175-4d7a-8599-48c40644f0c3",
              "created_at": "2019-07-04T10:07:22.563026",
              "updated_at": "2019-07-04T10:07:22.563060",
              "name": "Solar panel or other sustainable energy equipment"
            }
          ],
          "equipment_locations": [
            {
              "id": null,
              "created_at": "2019-07-04T10:07:21.622484",
              "updated_at": "2019-07-04T10:07:21.622515",
              "location_ids": [
                "9dc99f40-ac1d-421e-a408-c253d7ead671"
              ],
              "locations": [
                {
                  "id": "9dc99f40-ac1d-421e-a408-c253d7ead671",
                  "created_at": "2019-07-04T10:07:22.584320",
                  "updated_at": "2019-07-04T10:07:22.584353",
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
          "created_at": "2019-07-04T10:07:22.629054",
          "updated_at": "2019-07-04T10:07:22.629094",
          "email": "test@example.com",
          "profile_id": "4de4485a-dac8-486d-bf2c-817314df39df",
          "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "role": {
            "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "created_at": "2019-07-04T10:07:22.674242",
            "updated_at": "2019-07-04T10:07:22.674280",
            "name": "User"
          },
          "profile": {
            "id": "4de4485a-dac8-486d-bf2c-817314df39df",
            "created_at": "2019-07-04T10:07:22.651505",
            "updated_at": "2019-07-04T10:07:22.651540",
            "name": null,
            "preferred_contact_method": null,
            "email_addresses": null,
            "primary_email_id": null,
            "primary_phone_id": null
          }
        }
      }
    }
