# 28. About materials

We're patching the extension proposal just to add where materials questions will be answered.


![](/static/screen30.png)


> **NOTE**: As the user should only pick one option, but they may change their mind in a future edit, we should send a value for all three options to override any previously saved answer.


`PATCH /api/v1/extension-proposals/{id}`

    {
        "materials_definitions_in_documents": false,
        "materials_definitions_in_form": true,
        "materials_definitions_to_follow": false
    }

### Returns

    {
      "id": "d3ffff51-8f6a-4ca5-b9d1-00b57d9cb43b",
      "created_at": "2019-06-12T15:12:51.290914",
      "updated_at": "2019-06-12T15:12:51.290954",
      "application_id": "27388ac2-0880-48cd-8738-e198f86424b7",
      "original_house": {
        "id": null,
        "created_at": "2019-06-12T15:12:51.291191",
        "updated_at": "2019-06-12T15:12:51.291225",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-12T15:12:51.291345",
          "updated_at": "2019-06-12T15:12:51.291378",
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
          "created_at": "2019-06-12T15:12:51.291605",
          "updated_at": "2019-06-12T15:12:51.291638",
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
          "created_at": "2019-06-12T15:12:51.291869",
          "updated_at": "2019-06-12T15:12:51.291901",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e",
            "4e9f51cb-1c24-4993-be9e-350e0d395ecb"
          ],
          "works_locations": null,
          "works_type_ids": [
            "19ec661e-4655-4a98-9492-bf8a323607bf"
          ],
          "works_types": null,
          "materials_ids": null,
          "materials_other_ids": null,
          "materials": null
        },
        "porch": {
          "id": null,
          "created_at": "2019-06-12T15:12:51.292175",
          "updated_at": "2019-06-12T15:12:51.292208",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-12T15:12:51.292376",
          "updated_at": "2019-06-12T15:12:51.292409",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-12T15:12:51.292576",
          "updated_at": "2019-06-12T15:12:51.292609",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-12T15:12:51.292780",
          "updated_at": "2019-06-12T15:12:51.292812",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-12T15:12:51.292981",
          "updated_at": "2019-06-12T15:12:51.293013",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-12T15:12:51.293279",
        "updated_at": "2019-06-12T15:12:51.293312",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-12T15:12:51.293584",
          "updated_at": "2019-06-12T15:12:51.293617",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-12T15:12:51.293867",
        "updated_at": "2019-06-12T15:12:51.293901",
        "gates_fences_walls": {
          "id": null,
          "created_at": "2019-06-12T15:12:51.294008",
          "updated_at": "2019-06-12T15:12:51.294041",
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
        "created_at": "2019-06-12T15:12:51.294362",
        "updated_at": "2019-06-12T15:12:51.294395",
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
        "created_at": "2019-06-12T15:12:51.294656",
        "updated_at": "2019-06-12T15:12:51.294689",
        "parking_works_scope_id": "d17dea6b-20d8-46df-87d0-b41fc5ec08c3",
        "parking_works_scope": null,
        "parking_works_sub_type_ids": null,
        "current_car_parking_spaces": 10,
        "planned_car_parking_spaces": 20,
        "current_bike_parking_spaces": 10,
        "planned_bike_parking_spaces": 20,
        "new_ev_charging_points": 10
      },
      "trees": {
        "id": null,
        "created_at": "2019-06-12T15:12:51.294967",
        "updated_at": "2019-06-12T15:12:51.294999",
        "inside_boundry": true,
        "removed_or_pruned": true,
        "outside_boundry": true
      },
      "additional_floor_area": 23.8,
      "additional_floor_area_units_id": "095bd097-f66e-4c66-bc1e-3521a0358e8d",
      "new_single_bedrooms": 2,
      "new_double_bedrooms": 3,
      "materials_definitions_in_documents": false,
      "materials_definitions_in_form": true,
      "materials_definitions_to_follow": false
    }
