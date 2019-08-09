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


## Sign up

Post form-encoded `email`, `password` and `password_confirm` to the `users/create` endpoint. This will create an UNVERIFIED user who is unable to log in until they have completed the verification process. It will also send them an email with the verification link in.

`POST /api/v1/users/create`

### Example

    email: test@example.com
    password: secretpassword
    password_confirm: secretpassword


## Verify

The email that gets sent to the user will contain a verifcation link of the format {BASE_URL}/accounts/verify/{VERIFICATION_TOKEN} where BASE_URL is the URL that the front end application is running at. When the user clicks on that link, the front end should send a `GET` request to the verification endpoint...

`GET /api/v1/users/verify/{VERIFICATION_TOKEN}`

If this is successful, you will receive a similar payload to a login attempt.

    {
      "message": "Account verified and logged in",
      "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiZWYwY2Q5NDktMzFiYS00MjhlLWE3ZTQtMTk0MzczOWIxN2YwIn0sImlhdCI6MTU1NDQ2MDQ0MSwibmJmIjoxNTU0NDYwNDQxLCJleHAiOjE1NTQ1NDY4NDF9.4bIuU99dFXVb3nmEpohvkCl_etOJ0bDm3OT916Suyxo"
    }

Unsuccessful verifications, ie: user is already verified or the token is not valid should return a 400 with an error message...

    {
      "title": "Account already verified"
    }


## Reset password

### Step 1

`POST /api/v1/users/reset-password/`

The payload should be just the email address we want to trigger a reset for.

    {
        "email": "test@example.com"
    }


#### Success Response

    {
      "success": true,
      "message": "Password reset initiated"
    }

This endpoint triggers an email with instructions for resetting a user's password. It will contain a link to `{BASE_URL}/accounts/reset-password/{TOKEN}`

### Step 2

From this URL, send a new `POST` with the details of the password reset...

`POST /api/v1/users/reset-password`

    {
        "token": {TOKEN},
        "password": "secretpassword",
        "password_confirm": "secretpassword"
    }

#### Success Response

    {
      "success": true,
      "message": "Password reset successful"
    }

Both steps will return a `4XX` response if there is anything wrong, with a message about what was wrong.

    {
        "title": "Passwords do not match"
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
      "id": "5a61838d-0fe5-458a-a683-141b5c3d79fa",
      "created_at": "2019-08-09T10:35:48.520000",
      "updated_at": "2019-08-09T10:35:51.048000",
      "status_id": "5aa415fa-9b25-4828-ac06-cb1ab9b000ea",
      "reference": "2019/5000",
      "status": {
        "id": "5aa415fa-9b25-4828-ac06-cb1ab9b000ea",
        "created_at": "2019-08-09T10:35:47.302000",
        "updated_at": null,
        "name": "Submitted"
      },
      "submitted_at": "2019-08-09T10:35:51.019713+00:00",
      "works_started": true,
      "date_works_started": "2018-01-01",
      "works_completed": false,
      "date_works_completed": null,
      "works_description": null,
      "free_text_description": "Praesent commodo cursus magna,\nvel scelerisque nisl consectetur et. Praesent commodo cursus\nmagna, vel scelerisque nisl consectetur et. Donec sed odio dui.\nNullam id dolor id nibh ultricies vehicula ut id elit. Cum sociis\nnatoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n",
      "ownership_declaration": true,
      "reduction_eligible": true,
      "proposalFlow": null,
      "declaration_detail": {
        "id": null,
        "created_at": null,
        "updated_at": null,
        "name": "Sido Jombati",
        "role": "Defender",
        "details": "Everyone's favourite defender"
      },
      "declaration_id": "746b41c8-54b3-4cd6-89d7-2d41d1c55fbe",
      "declaration": {
        "id": "746b41c8-54b3-4cd6-89d7-2d41d1c55fbe",
        "created_at": "2019-08-09T10:35:47.271000",
        "updated_at": null,
        "name": "You are a Hackney Council member of staff"
      },
      "ownership_type_id": "784e54c7-d6da-4613-ac5a-046a27278f4b",
      "ownership_type": {
        "id": "784e54c7-d6da-4613-ac5a-046a27278f4b",
        "created_at": "2019-08-09T10:35:47.286000",
        "updated_at": null,
        "name": "The applicant is the sole owner of the land"
      },
      "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
      "owner": {
        "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "created_at": "2019-08-09T10:35:47.953000",
        "updated_at": "2019-08-09T10:35:51.522000",
        "_id": "5d4d4c835341f36f125953e7",
        "email": "test@example.com",
        "profile_id": "7e5a3176-5b92-4dc0-90d8-b3a96ebe0ed5",
        "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
        "role": {
          "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "created_at": "2019-08-09T10:35:47.137000",
          "updated_at": null,
          "name": "User"
        },
        "profile": {
          "id": "7e5a3176-5b92-4dc0-90d8-b3a96ebe0ed5",
          "created_at": "2019-08-09T10:35:47.950000",
          "updated_at": null,
          "company": null,
          "name": null,
          "email_addresses": null,
          "phone": null
        },
        "verified_at": "2019-08-09T10:35:47.691653+0000",
        "reset_token": null,
        "reset_token_expires": null
      },
      "site_address": {
        "id": "7f217d2c-90d4-445d-b5d0-54ab3c9f2f02",
        "created_at": "2019-08-09T10:35:48.667000",
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
        "application_id": "5a61838d-0fe5-458a-a683-141b5c3d79fa"
      },
      "site_constraints": {
        "id": "c7c461d0-70fe-46f2-80e7-fa3fb71769ba",
        "created_at": "2019-08-09T10:35:48.567000",
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
        "application_id": "5a61838d-0fe5-458a-a683-141b5c3d79fa"
      },
      "proposal_extension": {
        "id": "a850af78-6e6a-4df6-9281-0d22a52fb05f",
        "created_at": "2019-08-09T10:35:48.685000",
        "updated_at": "2019-08-09T10:35:48.688000",
        "application_id": "5a61838d-0fe5-458a-a683-141b5c3d79fa",
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
                "created_at": "2019-08-09T10:35:47.140000",
                "updated_at": null,
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-08-09T10:35:47.143000",
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
                "created_at": "2019-08-09T10:35:47.140000",
                "updated_at": null,
                "name": "Rear"
              },
              {
                "id": "4f464424-ca54-4bc4-b980-c5d957a5ad1a",
                "created_at": "2019-08-09T10:35:47.143000",
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
              "created_at": "2019-08-09T10:35:47.208000",
              "updated_at": null,
              "name": "Addition of a new entrance"
            },
            {
              "id": "679143a9-0ee5-478e-984f-11c990979061",
              "created_at": "2019-08-09T10:35:47.211000",
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
          "created_at": "2019-08-09T10:35:47.056000",
          "updated_at": null,
          "name": "sq metres"
        },
        "new_single_bedrooms": 2,
        "new_double_bedrooms": 3,
        "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "owner": {
          "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
          "created_at": "2019-08-09T10:35:47.953000",
          "updated_at": "2019-08-09T10:35:51.522000",
          "_id": "5d4d4c835341f36f125953e7",
          "email": "test@example.com",
          "profile_id": "7e5a3176-5b92-4dc0-90d8-b3a96ebe0ed5",
          "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "role": {
            "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "created_at": "2019-08-09T10:35:47.137000",
            "updated_at": null,
            "name": "User"
          },
          "profile": {
            "id": "7e5a3176-5b92-4dc0-90d8-b3a96ebe0ed5",
            "created_at": "2019-08-09T10:35:47.950000",
            "updated_at": null,
            "company": null,
            "name": null,
            "email_addresses": null,
            "phone": null
          },
          "verified_at": "2019-08-09T10:35:47.691653+0000",
          "reset_token": null,
          "reset_token_expires": null
        }
      },
      "proposal_equipment": {
        "id": "2cdc2a8d-8bc3-4601-b939-4a1b39513c2d",
        "created_at": "2019-08-09T10:35:49.489000",
        "updated_at": "2019-08-09T10:35:49.499000",
        "application_id": "5a61838d-0fe5-458a-a683-141b5c3d79fa",
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
                  "created_at": "2019-08-09T10:35:47.149000",
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
          "created_at": "2019-08-09T10:35:47.953000",
          "updated_at": "2019-08-09T10:35:51.522000",
          "_id": "5d4d4c835341f36f125953e7",
          "email": "test@example.com",
          "profile_id": "7e5a3176-5b92-4dc0-90d8-b3a96ebe0ed5",
          "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "role": {
            "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "created_at": "2019-08-09T10:35:47.137000",
            "updated_at": null,
            "name": "User"
          },
          "profile": {
            "id": "7e5a3176-5b92-4dc0-90d8-b3a96ebe0ed5",
            "created_at": "2019-08-09T10:35:47.950000",
            "updated_at": null,
            "company": null,
            "name": null,
            "email_addresses": null,
            "phone": null
          },
          "verified_at": "2019-08-09T10:35:47.691653+0000",
          "reset_token": null,
          "reset_token_expires": null
        }
      },
      "document_files": [
        {
          "id": "c1465987-c0c0-4fb6-b0a3-d492028b7ea1",
          "created_at": "2019-08-09T10:35:50.099000",
          "updated_at": "2019-08-09T10:35:50.100000",
          "original_name": "test-image.png",
          "storage_path": "5a61838d-0fe5-458a-a683-141b5c3d79fa/c1465987-c0c0-4fb6-b0a3-d492028b7ea1.png",
          "application_id": "5a61838d-0fe5-458a-a683-141b5c3d79fa",
          "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
          "document_size": {
            "id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
            "created_at": "2019-08-09T10:35:47.079000",
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
              "created_at": "2019-08-09T10:35:47.124000",
              "updated_at": null,
              "name": "Floor plans"
            },
            {
              "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
              "created_at": "2019-08-09T10:35:47.127000",
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
              "created_at": "2019-08-09T10:35:47.124000",
              "updated_at": null,
              "name": "Floor plans"
            },
            {
              "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
              "created_at": "2019-08-09T10:35:47.127000",
              "updated_at": null,
              "name": "Other"
            }
          ]
        },
        {
          "id": "b6248501-2ad2-447c-90e7-400bb71d5994",
          "created_at": "2019-08-09T10:35:50.210000",
          "updated_at": "2019-08-09T10:35:50.210000",
          "original_name": "test-image.png",
          "storage_path": "5a61838d-0fe5-458a-a683-141b5c3d79fa/b6248501-2ad2-447c-90e7-400bb71d5994.png",
          "application_id": "5a61838d-0fe5-458a-a683-141b5c3d79fa",
          "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
          "document_size": {
            "id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
            "created_at": "2019-08-09T10:35:47.079000",
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
              "created_at": "2019-08-09T10:35:47.124000",
              "updated_at": null,
              "name": "Floor plans"
            },
            {
              "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
              "created_at": "2019-08-09T10:35:47.127000",
              "updated_at": null,
              "name": "Other"
            }
          ]
        }
      ],
      "payments": [
        {
          "id": "b06df840-4fde-47ac-b649-2f1edaded3a8",
          "created_at": "2019-08-09T10:35:50.742000",
          "updated_at": "2019-08-09T10:35:50.752000",
          "amount": 1200,
          "description": "Your Service Description",
          "reference": "your-reference",
          "state": {
            "id": null,
            "created_at": null,
            "updated_at": null,
            "status": "created",
            "finished": true,
            "message": "User cancelled the payment",
            "code": "P010"
          },
          "refund_summary": {
            "id": null,
            "created_at": null,
            "updated_at": null,
            "status": "available",
            "amount_available": 100,
            "amount_submitted": 0
          },
          "payment_id": "hu20sqlact5260q2nanm0q8u93",
          "payment_provider": "worldpay",
          "created_date": "2016-01-21T17:15:00+00:00",
          "settlement_summary": {
            "id": null,
            "created_at": null,
            "updated_at": null,
            "capture_submit_time": "2016-01-21T17:15:00+00:00",
            "captured_date": "2016-01-21"
          },
          "delayed_capture": false,
          "return_url": "http://your.service.domain/your-reference",
          "next_url": "https://www.payments.service.gov.uk/secure/SOME_UUID",
          "email": "your email",
          "language": "en",
          "corporate_card_surcharge": 250,
          "total_amount": 1450,
          "fee": 5,
          "net_amount": 1195,
          "provider_id": "reference-from-payment-gateway",
          "card_brand": "Visa",
          "card_details": {
            "id": null,
            "created_at": null,
            "updated_at": null,
            "last_digits_card_number": "1234",
            "first_digits_card_number": "123456",
            "cardholder_name": "Mr. Card holder",
            "expiry_date": "12/20",
            "billing_address": {
              "id": null,
              "created_at": null,
              "updated_at": null,
              "line1": "address line 1",
              "line2": "address line 2",
              "postcode": "AB1 2CD",
              "city": "address city",
              "country": "GB"
            },
            "card_brand": "Visa"
          },
          "metadata": "{\"property1\": \"string\", \"property2\": \"string\"}",
          "_links": "{\"self\": {\"href\": \"https://an.example.link/from/payment/platform\", \"method\": \"GET\"}, \"next_url\": {\"href\": \"https://an.example.link/from/payment/platform\", \"method\": \"GET\"}, \"next_url_post\": {\"type\": \"application/x-www-form-urlencoded\", \"params\": {\"description\": \"This is a value for a parameter called description\"}, \"href\": \"https://an.example.link/from/payment/platform\", \"method\": \"POST\"}, \"events\": {\"href\": \"https://an.example.link/from/payment/platform\", \"method\": \"GET\"}, \"refunds\": {\"href\": \"https://an.example.link/from/payment/platform\", \"method\": \"GET\"}, \"cancel\": {\"type\": \"application/x-www-form-urlencoded\", \"params\": {\"description\": \"This is a value for a parameter called description\"}, \"href\": \"https://an.example.link/from/payment/platform\", \"method\": \"POST\"}, \"capture\": {\"type\": \"application/x-www-form-urlencoded\", \"params\": {\"description\": \"This is a value for a parameter called description\"}, \"href\": \"https://an.example.link/from/payment/platform\", \"method\": \"POST\"}}",
          "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
          "owner": {
            "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
            "created_at": "2019-08-09T10:35:47.953000",
            "updated_at": "2019-08-09T10:35:51.522000",
            "_id": "5d4d4c835341f36f125953e7",
            "email": "test@example.com",
            "profile_id": "7e5a3176-5b92-4dc0-90d8-b3a96ebe0ed5",
            "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "role": {
              "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
              "created_at": "2019-08-09T10:35:47.137000",
              "updated_at": null,
              "name": "User"
            },
            "profile": {
              "id": "7e5a3176-5b92-4dc0-90d8-b3a96ebe0ed5",
              "created_at": "2019-08-09T10:35:47.950000",
              "updated_at": null,
              "company": null,
              "name": null,
              "email_addresses": null,
              "phone": null
            },
            "verified_at": "2019-08-09T10:35:47.691653+0000",
            "reset_token": null,
            "reset_token_expires": null
          },
          "application_id": "5a61838d-0fe5-458a-a683-141b5c3d79fa"
        },
        {
          "id": "8792a6e9-35c8-4b1b-bb4f-d4444eaa55d1",
          "created_at": "2019-08-09T10:35:50.851000",
          "updated_at": "2019-08-09T10:35:50.851000",
          "amount": null,
          "description": "Submit my Planning Application payment",
          "reference": null,
          "state": null,
          "refund_summary": null,
          "payment_id": null,
          "payment_provider": null,
          "created_date": null,
          "settlement_summary": null,
          "delayed_capture": false,
          "return_url": null,
          "next_url": null,
          "email": null,
          "language": null,
          "corporate_card_surcharge": null,
          "total_amount": null,
          "fee": null,
          "net_amount": null,
          "provider_id": null,
          "card_brand": null,
          "card_details": null,
          "metadata": null,
          "_links": null,
          "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
          "owner": {
            "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
            "created_at": "2019-08-09T10:35:47.953000",
            "updated_at": "2019-08-09T10:35:51.522000",
            "_id": "5d4d4c835341f36f125953e7",
            "email": "test@example.com",
            "profile_id": "7e5a3176-5b92-4dc0-90d8-b3a96ebe0ed5",
            "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "role": {
              "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
              "created_at": "2019-08-09T10:35:47.137000",
              "updated_at": null,
              "name": "User"
            },
            "profile": {
              "id": "7e5a3176-5b92-4dc0-90d8-b3a96ebe0ed5",
              "created_at": "2019-08-09T10:35:47.950000",
              "updated_at": null,
              "company": null,
              "name": null,
              "email_addresses": null,
              "phone": null
            },
            "verified_at": "2019-08-09T10:35:47.691653+0000",
            "reset_token": null,
            "reset_token_expires": null
          },
          "application_id": "5a61838d-0fe5-458a-a683-141b5c3d79fa"
        }
      ]
    }
