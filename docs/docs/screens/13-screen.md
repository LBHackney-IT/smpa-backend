# 13. Outbuilding works


> **NOTE**: We're now submitting to the `incidental_buildings` key of an extension proposal.


### Example - add outbuilding works locations

![](/static/screen15.png)

`PATCH /api/v1/extension-proposals/{id}`

    {
        "incidental_buildings": {
            "outbuilding": {
                "works_location_ids": [
                    "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                ]
            }
        }
    }


### Returns

    {
      "id": "1c2acf8d-8cd0-47b7-9af0-6b0c61d44be2",
      "created_at": "2019-06-05T12:45:00.615350",
      "updated_at": "2019-06-05T12:45:00.615462",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-06-05T12:45:00.615806",
        "updated_at": "2019-06-05T12:45:00.615859",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-05T12:45:00.616026",
          "updated_at": "2019-06-05T12:45:00.616052",
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
          "created_at": "2019-06-05T12:45:00.616442",
          "updated_at": "2019-06-05T12:45:00.616483",
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
          "created_at": "2019-06-05T12:45:00.616755",
          "updated_at": "2019-06-05T12:45:00.616791",
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
        "porch": {
          "id": null,
          "created_at": "2019-06-05T12:45:00.617073",
          "updated_at": "2019-06-05T12:45:00.617109",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-05T12:45:00.617325",
          "updated_at": "2019-06-05T12:45:00.617361",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-05T12:45:00.617548",
          "updated_at": "2019-06-05T12:45:00.617583",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-05T12:45:00.617805",
          "updated_at": "2019-06-05T12:45:00.617922",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-05T12:45:00.618176",
          "updated_at": "2019-06-05T12:45:00.618210",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-05T12:45:00.618544",
        "updated_at": "2019-06-05T12:45:00.618578",
        "removal_or_demolition": false,
        "details": null,
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-05T12:45:00.618722",
          "updated_at": "2019-06-05T12:45:00.618756",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null
    }
