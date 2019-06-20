# 30. Other materials options

The user is allowed to select "This is not applicable" or "You're proposing a new material to be used" on each of the materials screens. In these cases, we just want to patch the extension-proposal.

![](/static/screen32.png)

### Example

Save the newly created material object(s) against the correct key in the extension proposal.

`PATCH /api/v1/extension-proposals/{id}`

    {
        "original_house": {
            "wall": {
                "materials_ids": [
                    "57d072b7-fe54-486c-bee0-7f8aad74bdcf"
                ]
            }
        }
    }

### Returns

    {
      "id": "d387e56e-9e8f-4298-8184-c1bf39bf6849",
      "created_at": "2019-06-18T20:18:58.052571",
      "updated_at": "2019-06-18T20:18:58.052614",
      "application_id": "35a9f1af-a643-44d7-9de8-96be9b351abb",
      "original_house": {
        "id": null,
        "created_at": "2019-06-18T20:18:58.052913",
        "updated_at": "2019-06-18T20:18:58.052946",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-18T20:18:58.053081",
          "updated_at": "2019-06-18T20:18:58.053114",
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
          "created_at": "2019-06-18T20:18:58.053350",
          "updated_at": "2019-06-18T20:18:58.053384",
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
          "created_at": "2019-06-18T20:18:58.053617",
          "updated_at": "2019-06-18T20:18:58.053650",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e",
            "4e9f51cb-1c24-4993-be9e-350e0d395ecb"
          ],
          "works_locations": null,
          "works_type_ids": [
            "19ec661e-4655-4a98-9492-bf8a323607bf"
          ],
          "works_types": null,
          "materials_ids": [
            "57d072b7-fe54-486c-bee0-7f8aad74bdcf"
          ],
          "materials_other_ids": null,
          "materials": null
        },
        "porch": {
          "id": null,
          "created_at": "2019-06-18T20:18:58.053939",
          "updated_at": "2019-06-18T20:18:58.053971",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-18T20:18:58.054144",
          "updated_at": "2019-06-18T20:18:58.054176",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-18T20:18:58.054349",
          "updated_at": "2019-06-18T20:18:58.054381",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-18T20:18:58.054560",
          "updated_at": "2019-06-18T20:18:58.054593",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-18T20:18:58.054769",
          "updated_at": "2019-06-18T20:18:58.054801",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-18T20:18:58.055348",
        "updated_at": "2019-06-18T20:18:58.055402",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-18T20:18:58.055553",
          "updated_at": "2019-06-18T20:18:58.055586",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-18T20:18:58.055869",
        "updated_at": "2019-06-18T20:18:58.055902",
        "gates_fences_walls": {
          "id": null,
          "created_at": "2019-06-18T20:18:58.056016",
          "updated_at": "2019-06-18T20:18:58.056049",
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
        "created_at": "2019-06-18T20:18:58.056383",
        "updated_at": "2019-06-18T20:18:58.056416",
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
        "created_at": "2019-06-18T20:18:58.056696",
        "updated_at": "2019-06-18T20:18:58.056730",
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
        "created_at": "2019-06-18T20:18:58.057165",
        "updated_at": "2019-06-18T20:18:58.057207",
        "inside_boundry": true,
        "removed_or_pruned": true,
        "outside_boundry": true
      },
      "additional_floor_area": 23.8,
      "additional_floor_area_units_id": "095bd097-f66e-4c66-bc1e-3521a0358e8d",
      "new_single_bedrooms": 2,
      "new_double_bedrooms": 3,
      "materials_definitions_in_documents": false,
      "materials_definitions_in_form": false,
      "materials_definitions_to_follow": false
    }
