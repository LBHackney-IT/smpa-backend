# 20. About car parking spaces


> **NOTE**: We're now submitting to the `parking` key of an extension proposal.


### Example - set the spaces counts

![](/static/screen22.png)

`PATCH /api/v1/extension-proposals/{id}`

    {
        "parking": {
            "current_car_parking_spaces": 10,
            "planned_car_parking_spaces": 20
        }
    }


### Returns

    {
      "id": "d3ffff51-8f6a-4ca5-b9d1-00b57d9cb43b",
      "created_at": "2019-06-12T10:00:02.345383",
      "updated_at": "2019-06-12T10:00:02.345435",
      "application_id": "27388ac2-0880-48cd-8738-e198f86424b7",
      "original_house": {
        "id": null,
        "created_at": "2019-06-12T10:00:02.345627",
        "updated_at": "2019-06-12T10:00:02.345663",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-12T10:00:02.345792",
          "updated_at": "2019-06-12T10:00:02.345826",
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
          "created_at": "2019-06-12T10:00:02.346266",
          "updated_at": "2019-06-12T10:00:02.346304",
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
          "created_at": "2019-06-12T10:00:02.346661",
          "updated_at": "2019-06-12T10:00:02.346705",
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
          "created_at": "2019-06-12T10:00:02.346993",
          "updated_at": "2019-06-12T10:00:02.347037",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-12T10:00:02.347245",
          "updated_at": "2019-06-12T10:00:02.347279",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-12T10:00:02.347462",
          "updated_at": "2019-06-12T10:00:02.347495",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-12T10:00:02.347676",
          "updated_at": "2019-06-12T10:00:02.347710",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-12T10:00:02.347890",
          "updated_at": "2019-06-12T10:00:02.347924",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-12T10:00:02.348165",
        "updated_at": "2019-06-12T10:00:02.348199",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-12T10:00:02.348330",
          "updated_at": "2019-06-12T10:00:02.348364",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-12T10:00:02.348580",
        "updated_at": "2019-06-12T10:00:02.348614",
        "gates_fences_walls": {
          "id": null,
          "created_at": "2019-06-12T10:00:02.348727",
          "updated_at": "2019-06-12T10:00:02.348761",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null,
          "works_type_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_types": null
        },
        "border_works_type_ids": null,
        "border_works_types": null
      },
      "means_of_access": {
        "id": null,
        "created_at": "2019-06-12T10:00:02.349051",
        "updated_at": "2019-06-12T10:00:02.349085",
        "access_works_scope_id": "4c75ce90-4616-4dd0-b70a-de5ca530a37d",
        "access_works_scope": null,
        "access_works_sub_type_ids": [
          "590a7e3d-87ab-4b44-8406-fe0fb369aa81",
          "181deec8-d26f-4796-a036-c66528536de9"
        ],
        "access_works_sub_types": null
      },
      "parking": {
        "id": null,
        "created_at": "2019-06-12T10:00:02.349314",
        "updated_at": "2019-06-12T10:00:02.349348",
        "parking_works_scope_id": "d17dea6b-20d8-46df-87d0-b41fc5ec08c3",
        "parking_works_scope": null,
        "parking_works_sub_type_ids": null,
        "current_car_parking_spaces": 10,
        "planned_car_parking_spaces": 20,
        "current_bike_parking_spaces": 0,
        "planned_bike_parking_spaces": 0,
        "new_ev_charging_points": 0
      }
    }
