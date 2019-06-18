# 11. Window / Door works


### Example - add window / door works locations

![](/static/screen13.png)

`PATCH /api/v1/extension-proposals/{id}`

    {
        "original_house": {
            "windows_doors": {
                "works_location_ids": [
                    "30d4874f-6570-403d-bfcc-d3c58cafe27e"
                ]
            }
        }
    }


### Returns

     {
      "id": "1c2acf8d-8cd0-47b7-9af0-6b0c61d44be2",
      "created_at": "2019-06-05T12:10:03.220544",
      "updated_at": "2019-06-05T12:10:03.220586",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-06-05T12:10:03.220848",
        "updated_at": "2019-06-05T12:10:03.220883",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-05T12:10:03.221011",
          "updated_at": "2019-06-05T12:10:03.221044",
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
          "created_at": "2019-06-05T12:10:03.221290",
          "updated_at": "2019-06-05T12:10:03.221332",
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
          "created_at": "2019-06-05T12:10:03.221596",
          "updated_at": "2019-06-05T12:10:03.221630",
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
          "created_at": "2019-06-05T12:10:03.222032",
          "updated_at": "2019-06-05T12:10:03.222066",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-05T12:10:03.222244",
          "updated_at": "2019-06-05T12:10:03.222277",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-05T12:10:03.222454",
          "updated_at": "2019-06-05T12:10:03.222486",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-05T12:10:03.222659",
          "updated_at": "2019-06-05T12:10:03.222692",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": null
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-05T12:10:03.223042",
        "updated_at": "2019-06-05T12:10:03.223076",
        "removal_or_demolition": false,
        "details": null
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null,
      "basement": null,
      "roof": null
    }
