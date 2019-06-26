# 29. Specifying materials

For each of the materials types, we can patch a list of objects to the extension proposal's `materials` key.

There are four, materials specification keys we can patch to. `roof`, `walls`, `windows`, and `doors`.


`PATCH /api/v1/extension-proposals/{id}`

    {
        "materials":{
            "roof": {
                "proposals": [
                    {
                        "material_id": "d470020f-984f-4acf-9e75-387f58db4604",
                        "colour_and_type": "Some lovely green roof tiles."
                    }
                ]
            }
        }
    }


### Returns

    {
      "id": "b2f70564-dbcf-4eb3-be31-f9c3261bbfb2",
      "created_at": "2019-06-26T13:55:30.654207",
      "updated_at": "2019-06-26T13:55:30.654243",
      "application_id": "a4a16477-9f93-4e48-a293-00f89fa5b406",
      "original_house": {
        "id": null,
        "created_at": "2019-06-26T13:55:30.654378",
        "updated_at": "2019-06-26T13:55:30.654406",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-26T13:55:30.654504",
          "updated_at": "2019-06-26T13:55:30.654532",
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
          "created_at": "2019-06-26T13:55:30.654722",
          "updated_at": "2019-06-26T13:55:30.654750",
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
          "created_at": "2019-06-26T13:55:30.654982",
          "updated_at": "2019-06-26T13:55:30.655010",
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
          "created_at": "2019-06-26T13:55:30.655277",
          "updated_at": "2019-06-26T13:55:30.655315",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-26T13:55:30.655461",
          "updated_at": "2019-06-26T13:55:30.655488",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-26T13:55:30.655631",
          "updated_at": "2019-06-26T13:55:30.655658",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-26T13:55:30.655800",
          "updated_at": "2019-06-26T13:55:30.655827",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-26T13:55:30.655968",
          "updated_at": "2019-06-26T13:55:30.655995",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-26T13:55:30.656181",
        "updated_at": "2019-06-26T13:55:30.656209",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-26T13:55:30.656310",
          "updated_at": "2019-06-26T13:55:30.656338",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-26T13:55:30.656505",
        "updated_at": "2019-06-26T13:55:30.656533",
        "gates_fences_walls": {
          "id": null,
          "created_at": "2019-06-26T13:55:30.656622",
          "updated_at": "2019-06-26T13:55:30.656650",
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
        "created_at": "2019-06-26T13:55:30.656880",
        "updated_at": "2019-06-26T13:55:30.656907",
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
        "created_at": "2019-06-26T13:55:30.657091",
        "updated_at": "2019-06-26T13:55:30.657119",
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
        "created_at": "2019-06-26T13:55:30.657318",
        "updated_at": "2019-06-26T13:55:30.657345",
        "inside_boundry": true,
        "removed_or_pruned": true,
        "outside_boundry": true
      },
      "materials": {
        "id": null,
        "created_at": "2019-06-26T13:55:30.657484",
        "updated_at": "2019-06-26T13:55:30.657511",
        "definitions_in_documents": false,
        "definitions_in_form": true,
        "definitions_to_follow": false,
        "roof": {
          "id": null,
          "created_at": "2019-06-26T13:55:30.657623",
          "updated_at": "2019-06-26T13:55:30.657650",
          "proposals": [
            {
              "id": null,
              "created_at": "2019-06-26T13:55:30.657748",
              "updated_at": "2019-06-26T13:55:30.657776",
              "colour_and_type": "Some lovely green roof tiles.",
              "material_id": "d470020f-984f-4acf-9e75-387f58db4604"
            }
          ],
          "matches_existing": false,
          "not_applicable": false
        },
        "walls": null,
        "windows": null,
        "doors": null
      },
      "additional_floor_area": 23.8,
      "additional_floor_area_units_id": "095bd097-f66e-4c66-bc1e-3521a0358e8d",
      "new_single_bedrooms": 2,
      "new_double_bedrooms": 3
    }
