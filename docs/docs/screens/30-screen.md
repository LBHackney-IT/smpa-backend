# 30. Other materials options

The user is allowed to select "This is not applicable" or "Material and finish match the existing" on each of the materials screens. These can be sent as booleans `not_applicable` and `matches_existing`.

![](/static/screen32.png)

### Example

Save the newly created material object(s) against the correct key in the extension proposal.

`PATCH /api/v1/extension-proposals/{id}`

    {
        "materials":{
            "walls": {
                "matches_existing": true,
                "not_applicable": false
            }
        }
    }

### Returns

    {
      "id": "3deb35c8-b128-4d54-b76d-063945a88f13",
      "created_at": "2019-06-26T14:19:34.211133",
      "updated_at": "2019-06-26T14:19:34.211175",
      "application_id": "00ce2e25-709c-42fb-96bf-cb97e7694e36",
      "original_house": {
        "id": null,
        "created_at": "2019-06-26T14:19:34.211342",
        "updated_at": "2019-06-26T14:19:34.211379",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-26T14:19:34.211672",
          "updated_at": "2019-06-26T14:19:34.211710",
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
          "created_at": "2019-06-26T14:19:34.211978",
          "updated_at": "2019-06-26T14:19:34.212011",
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
          "created_at": "2019-06-26T14:19:34.212406",
          "updated_at": "2019-06-26T14:19:34.212446",
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
          "created_at": "2019-06-26T14:19:34.212792",
          "updated_at": "2019-06-26T14:19:34.212833",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-26T14:19:34.213022",
          "updated_at": "2019-06-26T14:19:34.213055",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-26T14:19:34.213231",
          "updated_at": "2019-06-26T14:19:34.213264",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-26T14:19:34.213445",
          "updated_at": "2019-06-26T14:19:34.213478",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-26T14:19:34.213672",
          "updated_at": "2019-06-26T14:19:34.213706",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-26T14:19:34.213959",
        "updated_at": "2019-06-26T14:19:34.213995",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-26T14:19:34.214140",
          "updated_at": "2019-06-26T14:19:34.214173",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-26T14:19:34.214399",
        "updated_at": "2019-06-26T14:19:34.214441",
        "gates_fences_walls": {
          "id": null,
          "created_at": "2019-06-26T14:19:34.214555",
          "updated_at": "2019-06-26T14:19:34.214594",
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
        "created_at": "2019-06-26T14:19:34.214908",
        "updated_at": "2019-06-26T14:19:34.214942",
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
        "created_at": "2019-06-26T14:19:34.215176",
        "updated_at": "2019-06-26T14:19:34.215209",
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
        "created_at": "2019-06-26T14:19:34.215467",
        "updated_at": "2019-06-26T14:19:34.215500",
        "inside_boundry": true,
        "removed_or_pruned": true,
        "outside_boundry": true
      },
      "materials": {
        "id": null,
        "created_at": "2019-06-26T14:19:34.215675",
        "updated_at": "2019-06-26T14:19:34.215713",
        "definitions_in_documents": false,
        "definitions_in_form": true,
        "definitions_to_follow": false,
        "roof": {
          "id": null,
          "created_at": "2019-06-26T14:19:34.215851",
          "updated_at": "2019-06-26T14:19:34.215886",
          "proposals": [
            {
              "id": null,
              "created_at": "2019-06-26T14:19:34.216005",
              "updated_at": "2019-06-26T14:19:34.216042",
              "colour_and_type": "Some lovely green roof tiles.",
              "material_id": "d470020f-984f-4acf-9e75-387f58db4604"
            }
          ],
          "matches_existing": false,
          "not_applicable": false
        },
        "walls": {
          "id": null,
          "created_at": "2019-06-26T14:19:34.216263",
          "updated_at": "2019-06-26T14:19:34.216296",
          "proposals": null,
          "matches_existing": true,
          "not_applicable": false
        },
        "windows": null,
        "doors": null
      },
      "additional_floor_area": 23.8,
      "additional_floor_area_units_id": "095bd097-f66e-4c66-bc1e-3521a0358e8d",
      "new_single_bedrooms": 2,
      "new_double_bedrooms": 3
    }
