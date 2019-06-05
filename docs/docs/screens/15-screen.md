# 15. Changes to fences, gates, walls


> **NOTE**: We're now submitting to the `boundaries` key of an extension proposal.


### Example - add gates/fences/walls works type

![](/static/screen17.png)

`PATCH /api/v1/extension-proposals/{id}`

    {
        "boundaries": {
            "gates_fences_walls_type_ids": [
                "30d4874f-6570-403d-bfcc-d3c58cafe27e"
            ]
        }
    }


### Returns

    {
      "id": "1c2acf8d-8cd0-47b7-9af0-6b0c61d44be2",
      "created_at": "2019-06-05T13:40:35.563281",
      "updated_at": "2019-06-05T13:40:35.563406",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-06-05T13:40:35.563699",
        "updated_at": "2019-06-05T13:40:35.563724",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-05T13:40:35.563855",
          "updated_at": "2019-06-05T13:40:35.563888",
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
          "created_at": "2019-06-05T13:40:35.564148",
          "updated_at": "2019-06-05T13:40:35.564182",
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
          "created_at": "2019-06-05T13:40:35.564416",
          "updated_at": "2019-06-05T13:40:35.564449",
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
          "created_at": "2019-06-05T13:40:35.564674",
          "updated_at": "2019-06-05T13:40:35.564707",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-05T13:40:35.564879",
          "updated_at": "2019-06-05T13:40:35.564912",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-05T13:40:35.565089",
          "updated_at": "2019-06-05T13:40:35.565122",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-05T13:40:35.565297",
          "updated_at": "2019-06-05T13:40:35.565330",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-05T13:40:35.565501",
          "updated_at": "2019-06-05T13:40:35.565533",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-05T13:40:35.565854",
        "updated_at": "2019-06-05T13:40:35.565887",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-05T13:40:35.566038",
          "updated_at": "2019-06-05T13:40:35.566069",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-05T13:40:35.566304",
        "updated_at": "2019-06-05T13:40:35.566327",
        "border_works_type_ids": null,
        "border_works_types": null,
        "gates_fences_walls_type_ids": [
          "30d4874f-6570-403d-bfcc-d3c58cafe27e"
        ],
        "gates_fences_walls_types": null
      },
      "means_of_access": null,
      "parking": null
    }
