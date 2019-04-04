# Starting the works

POST /api/v1/applications

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


# About the works

POST /api/v1/extension-proposals

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

POST /api/v1/equipment-proposals

    application_id: str

### Returns
    equipment-proposal: json



# About the extension or alteration

PATCH /api/v1/extension-proposals/{id}

    original_house: json
    incidental_buildings: json
    gates_fences_etc: json
    means_of_access_to_site: json
    car_bike_spaces: json

For each option that the user has checked, send an empty json object {}

### Example

    {
        "original_house": {},
        "incidental_buildings": {}
    }

### Returns

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

# About the extension or alteration to the original house

PATCH /api/v1/extension-proposals/{id}

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

# About the Single storey extension

On load of this page, or at the start of the app, you should make a request to get the list of works location IDs.

GET /api/v1/works-locations

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


GET /api/v1/basement-works-locations

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

PATCH /api/v1/extension-proposals/{id}
