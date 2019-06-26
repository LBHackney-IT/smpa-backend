# 28. About materials

We're patching the extension proposal just to add where materials questions will be answered.


![](/static/screen30.png)


> **NOTE**: As the user should only pick one option, but they may change their mind in a future edit, we should send a value for all three options to override any previously saved answer.


`PATCH /api/v1/extension-proposals/{id}`

    {
        "materials": {
            "definitions_in_documents": false,
            "definitions_in_form": true,
            "definitions_to_follow": false
        }
    }

### Returns

    {
      "id": "7cdf0578-270c-4c04-8e10-5b4396fcefed",
      "created_at": "2019-06-26T12:50:09.719434",
      "updated_at": "2019-06-26T12:50:09.719477",
      "application_id": "a7855c97-185f-4f43-9588-8c69e644f653",
      "original_house": {
        "id": null,
        "created_at": "2019-06-26T12:50:09.719651",
        "updated_at": "2019-06-26T12:50:09.719687",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-26T12:50:09.719823",
          "updated_at": "2019-06-26T12:50:09.719860",
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
          "created_at": "2019-06-26T12:50:09.720092",
          "updated_at": "2019-06-26T12:50:09.720125",
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
          "created_at": "2019-06-26T12:50:09.720388",
          "updated_at": "2019-06-26T12:50:09.720422",
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
          "materials": null,
          "materials_not_applicable": false,
          "materials_match_existing": false
        },
        "porch": {
          "id": null,
          "created_at": "2019-06-26T12:50:09.720735",
          "updated_at": "2019-06-26T12:50:09.720782",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-26T12:50:09.721016",
          "updated_at": "2019-06-26T12:50:09.721051",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-26T12:50:09.721250",
          "updated_at": "2019-06-26T12:50:09.721282",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-26T12:50:09.721491",
          "updated_at": "2019-06-26T12:50:09.721525",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-26T12:50:09.721715",
          "updated_at": "2019-06-26T12:50:09.721748",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-26T12:50:09.722020",
        "updated_at": "2019-06-26T12:50:09.722053",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-26T12:50:09.722202",
          "updated_at": "2019-06-26T12:50:09.722235",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-26T12:50:09.722443",
        "updated_at": "2019-06-26T12:50:09.722476",
        "gates_fences_walls": {
          "id": null,
          "created_at": "2019-06-26T12:50:09.722584",
          "updated_at": "2019-06-26T12:50:09.722616",
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
        "created_at": "2019-06-26T12:50:09.722897",
        "updated_at": "2019-06-26T12:50:09.722930",
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
        "created_at": "2019-06-26T12:50:09.723156",
        "updated_at": "2019-06-26T12:50:09.723191",
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
        "created_at": "2019-06-26T12:50:09.723434",
        "updated_at": "2019-06-26T12:50:09.723464",
        "inside_boundry": true,
        "removed_or_pruned": true,
        "outside_boundry": true
      },
      "materials": {
        "id": null,
        "created_at": "2019-06-26T12:50:09.723739",
        "updated_at": "2019-06-26T12:50:09.723775",
        "definitions_in_documents": false,
        "definitions_in_form": true,
        "definitions_to_follow": false,
        "roof": null,
        "walls": null,
        "windows": null,
        "doors": null
      },
      "additional_floor_area": 23.8,
      "additional_floor_area_units_id": "095bd097-f66e-4c66-bc1e-3521a0358e8d",
      "new_single_bedrooms": 2,
      "new_double_bedrooms": 3
    }
