# 29. Specifying materials

For each of the materials types, we can patch a list of objects to the extension proposal's `materials` key.

`PATCH /api/v1/extension-proposals/{id}`

    {
        "materials":{
            "roof": [
                {
                    "material_id": "d470020f-984f-4acf-9e75-387f58db4604",
                    "colour_and_type": "Some lovely green roof tiles."
                }
            ]
        }
    }


### Returns

    {
      "id": "44dd34ee-ce66-40ec-bf3b-65b59bc9cdfa",
      "created_at": "2019-06-26T13:03:14.062964",
      "updated_at": "2019-06-26T13:03:14.063007",
      "application_id": "02c66b79-77f7-4c1c-b69f-8a811ea1c6b3",
      "original_house": {
        "id": null,
        "created_at": "2019-06-26T13:03:14.063170",
        "updated_at": "2019-06-26T13:03:14.063203",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-26T13:03:14.063317",
          "updated_at": "2019-06-26T13:03:14.063350",
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
          "created_at": "2019-06-26T13:03:14.063581",
          "updated_at": "2019-06-26T13:03:14.063613",
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
          "created_at": "2019-06-26T13:03:14.063845",
          "updated_at": "2019-06-26T13:03:14.063877",
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
          "created_at": "2019-06-26T13:03:14.064169",
          "updated_at": "2019-06-26T13:03:14.064202",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-26T13:03:14.064371",
          "updated_at": "2019-06-26T13:03:14.064403",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-26T13:03:14.064573",
          "updated_at": "2019-06-26T13:03:14.064606",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-26T13:03:14.064775",
          "updated_at": "2019-06-26T13:03:14.064808",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-26T13:03:14.064976",
          "updated_at": "2019-06-26T13:03:14.065008",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-26T13:03:14.065228",
        "updated_at": "2019-06-26T13:03:14.065260",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-26T13:03:14.065381",
          "updated_at": "2019-06-26T13:03:14.065413",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-26T13:03:14.065612",
        "updated_at": "2019-06-26T13:03:14.065645",
        "gates_fences_walls": {
          "id": null,
          "created_at": "2019-06-26T13:03:14.065749",
          "updated_at": "2019-06-26T13:03:14.065781",
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
        "created_at": "2019-06-26T13:03:14.066060",
        "updated_at": "2019-06-26T13:03:14.066092",
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
        "created_at": "2019-06-26T13:03:14.066312",
        "updated_at": "2019-06-26T13:03:14.066345",
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
        "created_at": "2019-06-26T13:03:14.066574",
        "updated_at": "2019-06-26T13:03:14.066607",
        "inside_boundry": true,
        "removed_or_pruned": true,
        "outside_boundry": true
      },
      "materials": {
        "id": null,
        "created_at": "2019-06-26T13:03:14.066769",
        "updated_at": "2019-06-26T13:03:14.066802",
        "definitions_in_documents": false,
        "definitions_in_form": true,
        "definitions_to_follow": false,
        "roof": [
          {
            "id": null,
            "created_at": "2019-06-26T13:03:14.066937",
            "updated_at": "2019-06-26T13:03:14.066970",
            "colour_and_type": "Some lovely green roof tiles.",
            "material_id": "d470020f-984f-4acf-9e75-387f58db4604"
          }
        ],
        "walls": null,
        "windows": null,
        "doors": null
      },
      "additional_floor_area": 23.8,
      "additional_floor_area_units_id": "095bd097-f66e-4c66-bc1e-3521a0358e8d",
      "new_single_bedrooms": 2,
      "new_double_bedrooms": 3
    }
