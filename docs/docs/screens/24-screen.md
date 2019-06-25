# 24. Equipment locations


### Add an equipment location

We can now update our equipment proposal with the locations of equipment being installed. For each one, we append to the equipment locations list.

![](/static/screen26.png)

`PATCH /api/v1/equipment-proposals/{id}`

    {
        "equipment": {
            "equipment_locations": [
                {
                    "location_ids": [
                        "b36079c1-dc9f-4225-a94d-b7c54c83b86e"
                    ],
                    "equipment_type_id": "9dc99f40-ac1d-421e-a408-c253d7ead671"
                }
            ]
        }
    }


> **NOTE**: Adding equipment locations replaces the saved data, so to update the list you need to include the previous data too. So adding a second equipment location would look like...

    {
        "equipment": {
            "equipment_locations": [
                {
                    "location_ids": [
                        "b36079c1-dc9f-4225-a94d-b7c54c83b86e"
                    ]
                    "equipment_type_id": "9dc99f40-ac1d-421e-a408-c253d7ead671"
                },
                {
                    "location_ids": [
                        "b36079c1-dc9f-4225-a94d-b7c54c83b86e"
                    ]
                    "equipment_type_id": "cc70f42f-dc59-4a03-bf7e-fbb2e7ff3b5b"
                }
            ]
        }
    }

### Returns

    {
      "id": "f8d0d582-7b27-42e3-8015-93ed9988bd51",
      "created_at": "2019-06-25T21:06:42.510825",
      "updated_at": "2019-06-25T21:06:42.510875",
      "application_id": "430ea7c1-7d94-49c8-bcef-773e9f4bf209",
      "equipment": {
        "id": null,
        "created_at": "2019-06-25T21:06:42.511058",
        "updated_at": "2019-06-25T21:06:42.511102",
        "equipment_type_ids": [
          "b36079c1-dc9f-4225-a94d-b7c54c83b86e",
          "cc70f42f-dc59-4a03-bf7e-fbb2e7ff3b5b",
          "fa6f8957-a775-4dc0-adfc-4c3ddfd42698"
        ],
        "equipment_types": null,
        "equipment_conservation_type_ids": [
          "4b2aa4a1-e01e-49ff-aedc-ddd638695839",
          "9f9390fa-f175-4d7a-8599-48c40644f0c3",
          "510e6d41-168d-45e6-ad7e-329a578961d2"
        ],
        "equipment_conservation_types": null,
        "equipment_locations": [
          {
            "id": null,
            "created_at": "2019-06-25T21:06:42.511351",
            "updated_at": "2019-06-25T21:06:42.511385",
            "location_ids": [
              "b36079c1-dc9f-4225-a94d-b7c54c83b86e"
            ],
            "locations": null,
            "equipment_type_id": "9dc99f40-ac1d-421e-a408-c253d7ead671",
            "equipment_type": null
          }
        ],
        "equipment_conservation_locations": null
      }
    }
