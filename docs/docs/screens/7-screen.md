# 7. Roof works


### Example - add roof works type

![](/static/screen8.png)

`PATCH /api/v1/extension-proposals/{id}`

    {
        "original_house": {
            "roof": {
                "works_type_ids": [
                    "19ec661e-4655-4a98-9492-bf8a323607bf"
                ]
            }
        }
    }


### Returns

    {
      "id": "1c2acf8d-8cd0-47b7-9af0-6b0c61d44be2",
      "created_at": "2019-06-05T11:12:00.786798",
      "updated_at": "2019-06-05T11:12:00.786842",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-06-05T11:12:00.787091",
        "updated_at": "2019-06-05T11:12:00.787125",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-05T11:12:00.787248",
          "updated_at": "2019-06-05T11:12:00.787281",
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
          "created_at": "2019-06-05T11:12:00.787521",
          "updated_at": "2019-06-05T11:12:00.787555",
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
          "created_at": "2019-06-05T11:12:00.787795",
          "updated_at": "2019-06-05T11:12:00.787829",
          "works_location_ids": null,
          "works_locations": null,
          "works_type_ids": [
            "19ec661e-4655-4a98-9492-bf8a323607bf"
          ],
          "works_types": null
        },
        "outbuilding": null,
        "porch": null,
        "balcony_terrace": null,
        "staircase": null,
        "add_replacement_windows_doors": null,
        "cladding": null
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-05T11:12:00.788225",
        "updated_at": "2019-06-05T11:12:00.788258",
        "removal_or_demolition": false,
        "details": null
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null,
      "basement": null,
      "roof": null
    }

### Example - add roof works locations

![](/static/screen9.png)

`PATCH /api/v1/extension-proposals/{id}`

    {
        "original_house": {
            "roof": {
                "works_location_ids": [
                    "30d4874f-6570-403d-bfcc-d3c58cafe27e",
                    "4e9f51cb-1c24-4993-be9e-350e0d395ecb"
                ]
            }
        }
    }


### Returns

    {
      "id": "1c2acf8d-8cd0-47b7-9af0-6b0c61d44be2",
      "created_at": "2019-06-05T11:17:16.637444",
      "updated_at": "2019-06-05T11:17:16.637489",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-06-05T11:17:16.637795",
        "updated_at": "2019-06-05T11:17:16.637834",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-05T11:17:16.638084",
          "updated_at": "2019-06-05T11:17:16.638155",
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
          "created_at": "2019-06-05T11:17:16.638835",
          "updated_at": "2019-06-05T11:17:16.638877",
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
          "created_at": "2019-06-05T11:17:16.639372",
          "updated_at": "2019-06-05T11:17:16.639409",
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
        "porch": null,
        "balcony_terrace": null,
        "staircase": null,
        "add_replacement_windows_doors": null,
        "cladding": null
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-05T11:17:16.639827",
        "updated_at": "2019-06-05T11:17:16.639863",
        "removal_or_demolition": false,
        "details": null
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null,
      "basement": null,
      "roof": null
    }

