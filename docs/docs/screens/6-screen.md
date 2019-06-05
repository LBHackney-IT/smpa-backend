# 6. Basement works


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

`PATCH /api/v1/extension-proposals/{id}`

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
