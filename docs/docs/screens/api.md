# SmPA API

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
    /api/v1/equipment-works-types
    /api/v1/equipment-works-conservation
    /api/v1/area-units
    /api/v1/linear-units
    /api/v1/document-sizes
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


## Starting the works

![](/static/screen1.png)

`POST /api/v1/applications`

    works_started: bool
    date_works_started: date
    works_completed: bool
    date_works_completed: date
    works_description: str

### Returns
    application: json

    {
      "id": "f83db82f-36cd-4d57-a14c-381b0886a97d",
      "created_at": "2019-04-04T14:38:37.844316",
      "updated_at": "2019-04-04T14:38:37.844356",
      "works_started": false,
      "date_works_started": null,
      "works_completed": false,
      "date_works_completed": null,
      "works_description": null,
      "owner_id": null,
      "owner": null,
      "site_address": null
    }


## About the works

![](/static/screen2.png)

`POST /api/v1/extension-proposals`

    application_id: str

### Returns
    extension-proposal: json

    {
      "id": "fb104ff2-eece-4f26-ab2a-1bc8c666ab67",
      "created_at": "2019-04-04T14:21:18.795839",
      "updated_at": "2019-04-04T14:21:18.795879",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": null,
      "incidental_buildings": null,
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null
    }

`POST /api/v1/equipment-proposals`

    application_id: str

### Returns
    equipment-proposal: json



## About the extension or alteration

![](/static/screen3.png)

`PATCH /api/v1/extension-proposals/{id}`

    original_house: json
    incidental_buildings: json
    gates_fences_etc: json
    means_of_access_to_site: json
    car_bike_spaces: json

For each option that the user has checked, send an empty json object {}

## Example

    {
        "original_house": {},
        "incidental_buildings": {}
    }

### Returns

This returns an extension proposal object. You'll need the ID from this for future calls to update the proposal.

    {
      "id": "fb104ff2-eece-4f26-ab2a-1bc8c666ab67",
      "created_at": "2019-04-04T14:47:32.608333",
      "updated_at": "2019-04-04T14:47:32.608385",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-04-04T14:47:32.608544",
        "updated_at": "2019-04-04T14:47:32.608577",
        "single_storey_extension": null,
        "two_storey_extension": null,
        "part_single_part_two_storey_extension": null,
        "basement": null,
        "roof_works": null,
        "outbuilding": null,
        "porch": null,
        "balcony_terrace": null,
        "staircase": null,
        "add_replacement_windows_doors": null,
        "cladding": null
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-04-04T14:47:32.608974",
        "updated_at": "2019-04-04T14:47:32.609007",
        "removal_or_demolition": false,
        "details": null
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null
    }

## About the extension or alteration to the original house

![](/static/screen4.png)

`PATCH /api/v1/extension-proposals/{id}`

    single_storey_extension: json
    two_storey_extension: json
    part_single_part_two_storey_extension: json
    basement: json
    roof_works: json
    outbuilding: json
    porch: json
    balcony_terrace: json
    staircase: json
    add_replacement_windows_doors: json
    cladding: json

Again, you can send empty json for each item checked

### Example

    {
        "original_house": {
            "single_storey_extension": {},
            "basement": {}
        },
        "incidental_buildings": {

        }
    }

### Returns

    {
      "id": "fb104ff2-eece-4f26-ab2a-1bc8c666ab67",
      "created_at": "2019-04-04T14:54:20.930509",
      "updated_at": "2019-04-04T14:54:20.930548",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-04-04T14:54:20.930720",
        "updated_at": "2019-04-04T14:54:20.930752",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-04-04T14:54:20.930873",
          "updated_at": "2019-04-04T14:54:20.930905",
          "works_location_ids": null
        },
        "two_storey_extension": null,
        "part_single_part_two_storey_extension": null,
        "basement": {
          "id": null,
          "created_at": "2019-04-04T14:54:20.931109",
          "updated_at": "2019-04-04T14:54:20.931141",
          "works_location_ids": null,
          "basement_works_location_ids": null
        },
        "roof_works": null,
        "outbuilding": null,
        "porch": null,
        "balcony_terrace": null,
        "staircase": null,
        "add_replacement_windows_doors": null,
        "cladding": null
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-04-04T14:54:20.931492",
        "updated_at": "2019-04-04T14:54:20.931525",
        "removal_or_demolition": false,
        "details": null
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null
    }

## About the Single storey extension

![](/static/screen4.png)

On load of this page, or at the start of the app, you should make a request to get the list of works location IDs.

`GET /api/v1/works-locations`

### Returns

    [
      {
        "id": "0eee199e-5324-4180-b7a0-8100cb880a4f",
        "created_at": "2019-04-04T18:17:27.777210",
        "updated_at": "2019-04-04T18:17:27.777248",
        "name": "Rear / side wrap-around"
      },
      {
        "id": "a8ea6581-1a7f-4d86-b28e-160320f32156",
        "created_at": "2019-04-04T18:17:27.777393",
        "updated_at": "2019-04-04T18:17:27.777424",
        "name": "Side"
      },
      {
        "id": "2263b74c-5c76-45d8-bb99-28b4172a59d8",
        "created_at": "2019-04-04T18:17:27.777574",
        "updated_at": "2019-04-04T18:17:27.777605",
        "name": "Front"
      },
      {
        "id": "53798c23-b806-41e3-85be-f26e78364f51",
        "created_at": "2019-04-04T18:17:27.777738",
        "updated_at": "2019-04-04T18:17:27.777769",
        "name": "Rear"
      }
    ]


`GET /api/v1/basement-works-types`

### Returns

    [
      {
        "id": "3b76431b-2254-4e24-aee1-dbb70a501999",
        "created_at": "2019-04-04T18:22:03.450561",
        "updated_at": "2019-04-04T18:22:03.450601",
        "name": "Enlargement of an existing basement"
      },
      {
        "id": "22ca10ac-fecf-4eee-a060-46f2d768fcb5",
        "created_at": "2019-04-04T18:22:03.450758",
        "updated_at": "2019-04-04T18:22:03.450789",
        "name": "Other alterations to the appearance of the house"
      },
      {
        "id": "cc060a9f-3c32-47a8-b963-aae04798f329",
        "created_at": "2019-04-04T18:22:03.450926",
        "updated_at": "2019-04-04T18:22:03.450957",
        "name": "Addition of lightwell(s)"
      },
      {
        "id": "3f16dceb-1a93-41e6-9692-95c6ca7f2fc1",
        "created_at": "2019-04-04T18:22:03.451090",
        "updated_at": "2019-04-04T18:22:03.451120",
        "name": "Excavation of a new basement"
      }
    ]

Once you have these IDs, you can patch the proposal again

`PATCH /api/v1/extension-proposals/{id}`

### Example

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

### Returns

    {
      "id": "fb104ff2-eece-4f26-ab2a-1bc8c666ab67",
      "created_at": "2019-04-04T18:38:27.102059",
      "updated_at": "2019-04-04T18:38:27.102097",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-04-04T18:38:27.102250",
        "updated_at": "2019-04-04T18:38:27.102299",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-04-04T18:38:27.102433",
          "updated_at": "2019-04-04T18:38:27.102463",
          "works_location_ids": [
            "0eee199e-5324-4180-b7a0-8100cb880a4f",
            "2263b74c-5c76-45d8-bb99-28b4172a59d8"
          ],
          "works_locations": null
        },
        "two_storey_extension": null,
        "part_single_part_two_storey_extension": null,
        "basement": {
          "id": null,
          "created_at": "2019-04-04T18:38:27.102734",
          "updated_at": "2019-04-04T18:38:27.102766",
          "works_location_ids": null,
          "works_locations": null
        },
        "roof_works": null,
        "outbuilding": null,
        "porch": null,
        "balcony_terrace": null,
        "staircase": null,
        "add_replacement_windows_doors": null,
        "cladding": null
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-04-04T18:38:27.103078",
        "updated_at": "2019-04-04T18:38:27.103111",
        "removal_or_demolition": false,
        "details": null
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null
    }

> **NOTE:** We're in a loop at this point and we just keep patching the extension proposal

For the basement, we ask two questions. What type of work is it and where is it.

#### Basement works type

![](/static/screen6.png)

Again though, we're just patching the extension proposal object.

`PATCH /api/v1/extension-proposals/{id}`

### Example - add basement works type

    {
        "original_house": {
            "basement": {
                "works_type_ids": [
                    "06a4181b-41f0-4b3f-9541-3357ff203998"
                ]
            }
        }
    }


### Returns

    {
      "id": "f8fe08bc-a29f-4004-b74b-7755e86a5edd",
      "created_at": "2019-05-30T14:53:20.353930",
      "updated_at": "2019-05-30T14:53:20.353979",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-05-30T14:53:20.354554",
        "updated_at": "2019-05-30T14:53:20.354597",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-05-30T14:53:20.354903",
          "updated_at": "2019-05-30T14:53:20.354976",
          "works_location_ids": [
            "165c9046-f6f2-4144-b60c-f1ca24c94054",
            "b6b2cc59-f097-48bc-a9ad-14f263e9e036"
          ],
          "works_locations": null
        },
        "two_storey_extension": null,
        "part_single_part_two_storey_extension": null,
        "basement": {
          "id": null,
          "created_at": "2019-05-30T14:53:20.355275",
          "updated_at": "2019-05-30T14:53:20.355309",
          "works_location_ids": null,
          "works_locations": null,
          "works_type_ids": [
            "06a4181b-41f0-4b3f-9541-3357ff203998"
          ],
          "works_types": null
        },
        "roof_works": null,
        "outbuilding": null,
        "porch": null,
        "balcony_terrace": null,
        "staircase": null,
        "add_replacement_windows_doors": null,
        "cladding": null
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-05-30T14:53:20.355788",
        "updated_at": "2019-05-30T14:53:20.355821",
        "removal_or_demolition": false,
        "details": null
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null,
      "basement": null
    }

### Example - add basement works locations

![](/static/screen7.png)

    {
        "original_house": {
            "basement": {
                "works_location_ids": [
                    "165c9046-f6f2-4144-b60c-f1ca24c94054",
                    "b6b2cc59-f097-48bc-a9ad-14f263e9e036"
                ]
            }
        }
    }


### Returns

    {
      "id": "f8fe08bc-a29f-4004-b74b-7755e86a5edd",
      "created_at": "2019-05-30T14:53:20.353930",
      "updated_at": "2019-05-30T14:53:20.353979",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-05-30T14:53:20.354554",
        "updated_at": "2019-05-30T14:53:20.354597",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-05-30T14:53:20.354903",
          "updated_at": "2019-05-30T14:53:20.354976",
          "works_location_ids": [
            "165c9046-f6f2-4144-b60c-f1ca24c94054",
            "b6b2cc59-f097-48bc-a9ad-14f263e9e036"
          ],
          "works_locations": null
        },
        "two_storey_extension": null,
        "part_single_part_two_storey_extension": null,
        "basement": {
          "id": null,
          "created_at": "2019-05-30T14:53:20.355275",
          "updated_at": "2019-05-30T14:53:20.355309",
          "works_location_ids": null,
          "works_locations": null,
          "works_type_ids": [
            "06a4181b-41f0-4b3f-9541-3357ff203998"
          ],
          "works_types": null
        },
        "roof_works": null,
        "outbuilding": null,
        "porch": null,
        "balcony_terrace": null,
        "staircase": null,
        "add_replacement_windows_doors": null,
        "cladding": null
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-05-30T14:53:20.355788",
        "updated_at": "2019-05-30T14:53:20.355821",
        "removal_or_demolition": false,
        "details": null
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null,
      "basement": null
    }

