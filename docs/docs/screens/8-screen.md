# 8. Porch works


### Example - add porch works locations

![](/static/screen10.png)

`PATCH /api/v1/extension-proposals/{id}`

    {
        "original_house": {
            "porch": {
                "works_location_ids": [
                    "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                ]
            }
        }
    }


### Returns

    {
      "id": "1c2acf8d-8cd0-47b7-9af0-6b0c61d44be2",
      "created_at": "2019-06-05T11:46:57.747698",
      "updated_at": "2019-06-05T11:46:57.747740",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-06-05T11:46:57.747982",
        "updated_at": "2019-06-05T11:46:57.748017",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-05T11:46:57.748140",
          "updated_at": "2019-06-05T11:46:57.748174",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e",
            "4e9f51cb-1c24-4993-be9e-350e0d395ecb"
          ],
          "works_locations": null
        },
        "two_storey_extension": null,
        "part_single_part_two_storey_extension": null,
        "basement": {
          "id": null,
          "created_at": "2019-06-05T11:46:57.748410",
          "updated_at": "2019-06-05T11:46:57.748444",
          "works_location_ids": [
            "165c9046-f6f2-4144-b60c-f1ca24c94054",
            "b6b2cc59-f097-48bc-a9ad-14f263e9e036"
          ],
          "works_locations": null,
          "works_type_ids": [
            "06a4181b-41f0-4b3f-9541-3357ff203998"
          ],
          "works_types": null
        },
        "roof": {
          "id": null,
          "created_at": "2019-06-05T11:46:57.748681",
          "updated_at": "2019-06-05T11:46:57.748713",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e",
            "4e9f51cb-1c24-4993-be9e-350e0d395ecb"
          ],
          "works_locations": null,
          "works_type_ids": [
            "19ec661e-4655-4a98-9492-bf8a323607bf"
          ],
          "works_types": null
        },
        "outbuilding": null,
        "porch": {
          "id": null,
          "created_at": "2019-06-05T11:46:57.748959",
          "updated_at": "2019-06-05T11:46:57.748992",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": null,
        "staircase": null,
        "add_replacement_windows_doors": null,
        "cladding": null
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-05T11:46:57.749335",
        "updated_at": "2019-06-05T11:46:57.749368",
        "removal_or_demolition": false,
        "details": null
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null,
      "basement": null,
      "roof": null
    }
