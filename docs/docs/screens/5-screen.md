# 5. About the Single storey extension

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
