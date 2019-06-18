# 27. About the trees and hedges

> **NOTE**: We're still patching the extension proposal


![](/static/screen29.png)


`PATCH /api/v1/extension-proposals/{id}`

    {
        "trees": {
            "inside_boundry": true,
            "removed_or_pruned": true,
            "outside_boundry": true
        }
    }

### Returns

    {
      "id": "d3ffff51-8f6a-4ca5-b9d1-00b57d9cb43b",
      "created_at": "2019-06-12T14:25:29.095229",
      "updated_at": "2019-06-12T14:25:29.095270",
      "application_id": "27388ac2-0880-48cd-8738-e198f86424b7",
      "original_house": {
        "id": null,
        "created_at": "2019-06-12T14:25:29.095521",
        "updated_at": "2019-06-12T14:25:29.095554",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-12T14:25:29.095679",
          "updated_at": "2019-06-12T14:25:29.095712",
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
          "created_at": "2019-06-12T14:25:29.095945",
          "updated_at": "2019-06-12T14:25:29.095979",
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
          "created_at": "2019-06-12T14:25:29.096212",
          "updated_at": "2019-06-12T14:25:29.096245",
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
          "created_at": "2019-06-12T14:25:29.096477",
          "updated_at": "2019-06-12T14:25:29.096510",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-12T14:25:29.096684",
          "updated_at": "2019-06-12T14:25:29.096716",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-12T14:25:29.096888",
          "updated_at": "2019-06-12T14:25:29.096920",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-12T14:25:29.097092",
          "updated_at": "2019-06-12T14:25:29.097124",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-12T14:25:29.097297",
          "updated_at": "2019-06-12T14:25:29.097330",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-12T14:25:29.097604",
        "updated_at": "2019-06-12T14:25:29.097636",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-12T14:25:29.097763",
          "updated_at": "2019-06-12T14:25:29.097795",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-12T14:25:29.098040",
        "updated_at": "2019-06-12T14:25:29.098073",
        "gates_fences_walls": {
          "id": null,
          "created_at": "2019-06-12T14:25:29.098180",
          "updated_at": "2019-06-12T14:25:29.098213",
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
        "created_at": "2019-06-12T14:25:29.098675",
        "updated_at": "2019-06-12T14:25:29.098709",
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
        "created_at": "2019-06-12T14:25:29.098978",
        "updated_at": "2019-06-12T14:25:29.099011",
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
        "created_at": "2019-06-12T14:25:29.099294",
        "updated_at": "2019-06-12T14:25:29.099327",
        "inside_boundry": true,
        "removed_or_pruned": true,
        "outside_boundry": true
      },
      "additional_floor_area": 23.8,
      "additional_floor_area_units_id": "095bd097-f66e-4c66-bc1e-3521a0358e8d",
      "new_single_bedrooms": 2,
      "new_double_bedrooms": 3
    }
