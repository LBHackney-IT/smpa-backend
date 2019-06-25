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
                    ]
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
      "id": "bcaa27fe-e5fa-4269-bc67-1d653b464f85",
      "created_at": "2019-06-12T13:39:17.368124",
      "updated_at": "2019-06-12T13:39:17.368218",
      "application_id": "27388ac2-0880-48cd-8738-e198f86424b7",
      "equipment": {
        "id": null,
        "created_at": "2019-06-12T13:39:17.368499",
        "updated_at": "2019-06-12T13:39:17.368528",
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
            "created_at": "2019-06-12T13:39:17.368762",
            "updated_at": "2019-06-12T13:39:17.368791",
            "location_id": "b36079c1-dc9f-4225-a94d-b7c54c83b86e",
            "location": null,
            "equipment_type_id": "9dc99f40-ac1d-421e-a408-c253d7ead671",
            "equipment_type": null
          }
        ],
        "equipment_conservation_locations": null
      }
    }
