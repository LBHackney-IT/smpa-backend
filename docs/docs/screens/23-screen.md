# 23. About the equipment

### Default Data

Default data can be retrieved from...

`GET /api/v1/equipment-works-conservation-types`

    [
      {
        "id": "4b2aa4a1-e01e-49ff-aedc-ddd638695839",
        "created_at": "2019-06-12T11:09:30.199124",
        "updated_at": "2019-06-12T11:09:30.199177",
        "name": "CCTV"
      },
      {
        "id": "9f9390fa-f175-4d7a-8599-48c40644f0c3",
        "created_at": "2019-06-12T11:09:30.199327",
        "updated_at": "2019-06-12T11:09:30.199359",
        "name": "Solar panel or other sustainable energy equipment"
      },
      {
        "id": "510e6d41-168d-45e6-ad7e-329a578961d2",
        "created_at": "2019-06-12T11:09:30.199495",
        "updated_at": "2019-06-12T11:09:30.199526",
        "name": "Security alarm"
      }
    ]

And...

`GET /api/v1/equipment-works-types`

    [
      {
        "id": "b36079c1-dc9f-4225-a94d-b7c54c83b86e",
        "created_at": "2019-06-12T11:07:51.601420",
        "updated_at": "2019-06-12T11:07:51.601469",
        "name": "Tank"
      },
      {
        "id": "cc70f42f-dc59-4a03-bf7e-fbb2e7ff3b5b",
        "created_at": "2019-06-12T11:07:51.601633",
        "updated_at": "2019-06-12T11:07:51.601666",
        "name": "Air conditioning unit"
      },
      {
        "id": "fa6f8957-a775-4dc0-adfc-4c3ddfd42698",
        "created_at": "2019-06-12T11:07:51.601812",
        "updated_at": "2019-06-12T11:07:51.601845",
        "name": "Satellite dish or antenna"
      }
    ]


> **NOTE**: We now need to create (or update if we created it earlier) an EquipmentProposal object, tied to our Application ID.


#### Create an equipment proposal

`POST /api/v1/equipment-proposals`

    {
        "application_id": "27388ac2-0880-48cd-8738-e198f86424b7"
    }

##### Returns

    {
      "id": "1f434858-da53-4e83-b40f-dffb8c39115f",
      "created_at": "2019-06-12T11:36:32.590246",
      "updated_at": "2019-06-12T11:36:32.590287",
      "application_id": "27388ac2-0880-48cd-8738-e198f86424b7"
    }


### Update an equipment proposal

We can now update our equipment proposal with the types of equipment being installed.

![](/static/screen25.png)

`PATCH /api/v1/equipment-proposals/{id}`

    {
        "equipment":{
            "equipment_type_ids": [
                "b36079c1-dc9f-4225-a94d-b7c54c83b86e",
                "cc70f42f-dc59-4a03-bf7e-fbb2e7ff3b5b",
                "fa6f8957-a775-4dc0-adfc-4c3ddfd42698"
            ],
            "equipment_conservation_type_ids": [
                "4b2aa4a1-e01e-49ff-aedc-ddd638695839",
                "9f9390fa-f175-4d7a-8599-48c40644f0c3",
                "510e6d41-168d-45e6-ad7e-329a578961d2"
            ]
        }
    }


### Returns

    {
      "id": "1f434858-da53-4e83-b40f-dffb8c39115f",
      "created_at": "2019-06-12T11:49:57.980020",
      "updated_at": "2019-06-12T11:49:57.980061",
      "application_id": "27388ac2-0880-48cd-8738-e198f86424b7",
      "equipment": {
        "id": null,
        "created_at": "2019-06-12T11:49:57.980288",
        "updated_at": "2019-06-12T11:49:57.980321",
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
        "equipment_conservation_types": null
      }
    }
