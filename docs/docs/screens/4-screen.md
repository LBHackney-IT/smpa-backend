# 4. About the extension or alteration to the original house

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
