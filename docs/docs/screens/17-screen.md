# 17. About the site access - scope


> **NOTE**: We're now submitting to the `means_of_access` key of an extension proposal.


### Example - set the scope

![](/static/screen19.png)

`PATCH /api/v1/extension-proposals/{id}`

    {
        "means_of_access": {
            "access_works_scope_id": "4c75ce90-4616-4dd0-b70a-de5ca530a37d"
        }
    }


### Returns

    {
      "id": "1c2acf8d-8cd0-47b7-9af0-6b0c61d44be2",
      "created_at": "2019-06-05T14:14:35.373612",
      "updated_at": "2019-06-05T14:14:35.373657",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-06-05T14:14:35.373877",
        "updated_at": "2019-06-05T14:14:35.373911",
        "single_storey_extension": {
          "id": null,
          "created_at": "2019-06-05T14:14:35.374031",
          "updated_at": "2019-06-05T14:14:35.374064",
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
          "created_at": "2019-06-05T14:14:35.374333",
          "updated_at": "2019-06-05T14:14:35.374366",
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
          "created_at": "2019-06-05T14:14:35.374597",
          "updated_at": "2019-06-05T14:14:35.374629",
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
          "created_at": "2019-06-05T14:14:35.375297",
          "updated_at": "2019-06-05T14:14:35.375332",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "balcony_terrace": {
          "id": null,
          "created_at": "2019-06-05T14:14:35.375510",
          "updated_at": "2019-06-05T14:14:35.375543",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "staircase": {
          "id": null,
          "created_at": "2019-06-05T14:14:35.375717",
          "updated_at": "2019-06-05T14:14:35.375750",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "windows_doors": {
          "id": null,
          "created_at": "2019-06-05T14:14:35.375924",
          "updated_at": "2019-06-05T14:14:35.375957",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        },
        "cladding": {
          "id": null,
          "created_at": "2019-06-05T14:14:35.376129",
          "updated_at": "2019-06-05T14:14:35.376162",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-06-05T14:14:35.376388",
        "updated_at": "2019-06-05T14:14:35.376421",
        "removal_or_demolition": true,
        "details": "I'm knocking a shed down.",
        "outbuilding": {
          "id": null,
          "created_at": "2019-06-05T14:14:35.376546",
          "updated_at": "2019-06-05T14:14:35.376578",
          "works_location_ids": [
            "30d4874f-6570-403d-bfcc-d3c58cafe27e"
          ],
          "works_locations": null
        }
      },
      "boundaries": {
        "id": null,
        "created_at": "2019-06-05T14:37:29.212186",
        "updated_at": "2019-06-05T14:37:29.212218",
        "gates_fences_walls": {
          "id": null,
          "created_at": "2019-06-05T14:37:29.212457",
          "updated_at": "2019-06-05T14:37:29.212488",
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
        "created_at": "2019-06-05T14:37:29.212795",
        "updated_at": "2019-06-05T14:37:29.212823",
        "access_works_scope_id": "4c75ce90-4616-4dd0-b70a-de5ca530a37d",
        "access_works_sub_type_ids": null
      },
      "parking": null
    }
