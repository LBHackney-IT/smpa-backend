# 14. Outbuilding details


> **NOTE**: We're now submitting to the `incidental_buildings` key of an extension proposal.


### Example - add outbuilding works locations

![](/static/screen16.png)

`PATCH /api/v1/extension-proposals/{id}`

    {
        "incidental_buildings": {
            "removal_or_demolition": true,
            "details": "I'm knocking a shed down."
        }
    }


### Returns

    {
      "id": "1c2acf8d-8cd0-47b7-9af0-6b0c61d44be2",
      "created_at": "2019-06-05T12:51:48.228914",
      "updated_at": "2019-06-05T12:51:48.228955",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-06-05T12:51:48.229133",
        "updated_at": "2019-06-05T12:51:48.229167",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-05T12:51:48.229502",
          "updated_at": "2019-06-05T12:51:48.229536",
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
          "created_at": "2019-06-05T12:51:48.229771",
          "updated_at": "2019-06-05T12:51:48.229805",
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
          "created_at": "2019-06-05T12:51:48.230160",
          "updated_at": "2019-06-05T12:51:48.230195",
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
          "created_at": "2019-06-05T12:51:48.230424",
          "updated_at": "2019-06-05T12:51:48.230458",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-05T12:51:48.230633",
          "updated_at": "2019-06-05T12:51:48.230667",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-05T12:51:48.230839",
          "updated_at": "2019-06-05T12:51:48.230871",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-05T12:51:48.231046",
          "updated_at": "2019-06-05T12:51:48.231079",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-05T12:51:48.231250",
          "updated_at": "2019-06-05T12:51:48.231283",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-05T12:51:48.231511",
        "updated_at": "2019-06-05T12:51:48.231544",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-05T12:51:48.231669",
          "updated_at": "2019-06-05T12:51:48.231702",
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
