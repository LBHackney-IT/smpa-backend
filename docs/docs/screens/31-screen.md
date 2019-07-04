# 31. Other materials

Other materials can be sent as a list of strings.

![](/static/screen33.png)

### Example

`PATCH /api/v1/extension-proposals/{id}`

    {
        "materials":{
            "other": [
                "The chimney is made of diamonds",
                "The path is made of gold."
            ]
        }
    }

### Returns

    {
      "id": "542141ce-3e5f-492a-ba4a-aef66308e970",
      "created_at": "2019-06-26T14:39:31.181086",
      "updated_at": "2019-06-26T14:39:31.181129",
      "application_id": "9d843fe2-79c3-4133-9741-25375943c986",
      "original_house": {
        "id": null,
        "created_at": "2019-06-26T14:39:31.181310",
        "updated_at": "2019-06-26T14:39:31.181344",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-26T14:39:31.181473",
          "updated_at": "2019-06-26T14:39:31.181506",
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
          "created_at": "2019-06-26T14:39:31.181769",
          "updated_at": "2019-06-26T14:39:31.181802",
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
          "created_at": "2019-06-26T14:39:31.182035",
          "updated_at": "2019-06-26T14:39:31.182067",
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
          "created_at": "2019-06-26T14:39:31.182357",
          "updated_at": "2019-06-26T14:39:31.182389",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-26T14:39:31.182561",
          "updated_at": "2019-06-26T14:39:31.182594",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-26T14:39:31.182763",
          "updated_at": "2019-06-26T14:39:31.182796",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-26T14:39:31.182964",
          "updated_at": "2019-06-26T14:39:31.182997",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-26T14:39:31.183166",
          "updated_at": "2019-06-26T14:39:31.183198",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-26T14:39:31.183424",
        "updated_at": "2019-06-26T14:39:31.183456",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-26T14:39:31.183578",
          "updated_at": "2019-06-26T14:39:31.183611",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-26T14:39:31.183810",
        "updated_at": "2019-06-26T14:39:31.183842",
        "gates_fences_walls": {
          "id": null,
          "created_at": "2019-06-26T14:39:31.183946",
          "updated_at": "2019-06-26T14:39:31.183979",
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
        "created_at": "2019-06-26T14:39:31.184250",
        "updated_at": "2019-06-26T14:39:31.184283",
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
        "created_at": "2019-06-26T14:39:31.184504",
        "updated_at": "2019-06-26T14:39:31.184537",
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
        "created_at": "2019-06-26T14:39:31.184769",
        "updated_at": "2019-06-26T14:39:31.184802",
        "inside_boundry": true,
        "removed_or_pruned": true,
        "outside_boundry": true
      },
      "materials": {
        "id": null,
        "created_at": "2019-06-26T14:39:31.184971",
        "updated_at": "2019-06-26T14:39:31.185004",
        "definitions_in_documents": false,
        "definitions_in_form": true,
        "definitions_to_follow": false,
        "roof": {
          "id": null,
          "created_at": "2019-06-26T14:39:31.185135",
          "updated_at": "2019-06-26T14:39:31.185168",
          "proposals": [
            {
              "id": null,
              "created_at": "2019-06-26T14:39:31.185283",
              "updated_at": "2019-06-26T14:39:31.185315",
              "colour_and_type": "Some lovely green roof tiles.",
              "material_id": "d470020f-984f-4acf-9e75-387f58db4604"
            }
          ],
          "matches_existing": false,
          "not_applicable": false
        },
        "walls": {
          "id": null,
          "created_at": "2019-06-26T14:39:31.185522",
          "updated_at": "2019-06-26T14:39:31.185554",
          "proposals": null,
          "matches_existing": true,
          "not_applicable": false
        },
        "windows": {
          "id": null,
          "created_at": "2019-06-26T14:39:31.185807",
          "updated_at": "2019-06-26T14:39:31.185837",
          "proposals": null,
          "matches_existing": false,
          "not_applicable": true
        },
        "doors": null,
        "other": [
          "The chimney is made of diamonds",
          "The path is made of gold."
        ]
      },
      "additional_floor_area": 23.8,
      "additional_floor_area_units_id": "095bd097-f66e-4c66-bc1e-3521a0358e8d",
      "new_single_bedrooms": 2,
      "new_double_bedrooms": 3
    }
