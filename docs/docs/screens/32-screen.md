# 32. Document uploads

Document uploads are a multipart form POST

### Example

`POST /api/v1/documents`

Post vars:

`document_size_id` : str - the id of a document size
`application_id` : str - the application id this should belong to
`proposed` : str - a comma separated list of document type ids for "proposed"
`existing` : str - a comma separated list of document type ids for "existing"
`document` : file - the document file we're uploading


### Returns

    {
      "id": "b31beadf-d88d-49a0-8a9d-6eaf4b4fba5f",
      "created_at": "2019-07-25T08:38:51.561517",
      "updated_at": "2019-07-25T08:38:51.561546",
      "original_name": "IMG_3035.jpeg",
      "storage_path": "3f61dcfb-2c67-40f6-abb8-de9dabf9a091/b31beadf-d88d-49a0-8a9d-6eaf4b4fba5f.jpg",
      "application_id": "3f61dcfb-2c67-40f6-abb8-de9dabf9a091",
      "document_size_id": "1b3b842c-70e7-413c-b6c7-4503b12dd417",
      "document_size": {
        "id": "1b3b842c-70e7-413c-b6c7-4503b12dd417",
        "created_at": "2019-07-25T08:38:51.723786",
        "updated_at": "2019-07-25T08:38:51.723816",
        "name": "A4"
      },
      "document_types_existing_ids": [
        "cbddcfc8-d062-4202-b350-f875c04c6aa0",
        "f1ff39d9-aab3-46e3-8749-dad11c04e3b8"
      ],
      "document_types_existing": [
        {
          "id": "cbddcfc8-d062-4202-b350-f875c04c6aa0",
          "created_at": "2019-07-25T08:38:51.748103",
          "updated_at": "2019-07-25T08:38:51.748135",
          "name": "Floor plans"
        },
        {
          "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
          "created_at": "2019-07-25T08:38:51.768639",
          "updated_at": "2019-07-25T08:38:51.768671",
          "name": "Other"
        }
      ],
      "document_types_proposed_ids": [
        "cbddcfc8-d062-4202-b350-f875c04c6aa0",
        "f1ff39d9-aab3-46e3-8749-dad11c04e3b8"
      ],
      "document_types_proposed": [
        {
          "id": "cbddcfc8-d062-4202-b350-f875c04c6aa0",
          "created_at": "2019-07-25T08:38:51.789476",
          "updated_at": "2019-07-25T08:38:51.789509",
          "name": "Floor plans"
        },
        {
          "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
          "created_at": "2019-07-25T08:38:51.809508",
          "updated_at": "2019-07-25T08:38:51.809540",
          "name": "Other"
        }
      ]
    }


## Fetch documents for an application

### Example

`GET /api/v1/applications/{application_id}/documents`

### Returns


    [
      {
        "id": "17c03191-f8a5-45eb-be68-c1f694d757cb",
        "created_at": "2019-08-02T09:56:38.009000",
        "updated_at": "2019-08-02T09:56:38.009000",
        "original_name": "test-image.png",
        "storage_path": "602c59c4-c8c5-41c9-b525-ad316fe9c136/17c03191-f8a5-45eb-be68-c1f694d757cb.png",
        "application_id": "602c59c4-c8c5-41c9-b525-ad316fe9c136",
        "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
        "document_size": {
          "id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
          "created_at": "2019-08-02T09:56:35.153000",
          "updated_at": null,
          "name": "A1"
        },
        "document_types_existing_ids": [
          "cbddcfc8-d062-4202-b350-f875c04c6aa0",
          "f1ff39d9-aab3-46e3-8749-dad11c04e3b8"
        ],
        "document_types_existing": [
          {
            "id": "cbddcfc8-d062-4202-b350-f875c04c6aa0",
            "created_at": "2019-08-02T09:56:35.226000",
            "updated_at": null,
            "name": "Floor plans"
          },
          {
            "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
            "created_at": "2019-08-02T09:56:35.229000",
            "updated_at": null,
            "name": "Other"
          }
        ],
        "document_types_proposed_ids": [
          "cbddcfc8-d062-4202-b350-f875c04c6aa0",
          "f1ff39d9-aab3-46e3-8749-dad11c04e3b8"
        ],
        "document_types_proposed": [
          {
            "id": "cbddcfc8-d062-4202-b350-f875c04c6aa0",
            "created_at": "2019-08-02T09:56:35.226000",
            "updated_at": null,
            "name": "Floor plans"
          },
          {
            "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
            "created_at": "2019-08-02T09:56:35.229000",
            "updated_at": null,
            "name": "Other"
          }
        ]
      },
      {
        "id": "bcd2a3a3-1986-4de4-8b00-a2a96538984f",
        "created_at": "2019-08-02T09:56:38.122000",
        "updated_at": "2019-08-02T09:56:38.122000",
        "original_name": "test-image.png",
        "storage_path": "602c59c4-c8c5-41c9-b525-ad316fe9c136/bcd2a3a3-1986-4de4-8b00-a2a96538984f.png",
        "application_id": "602c59c4-c8c5-41c9-b525-ad316fe9c136",
        "document_size_id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
        "document_size": {
          "id": "a3ec6180-a863-43e9-8f6c-de7a171ce489",
          "created_at": "2019-08-02T09:56:35.153000",
          "updated_at": null,
          "name": "A1"
        },
        "document_types_existing_ids": [],
        "document_types_existing": [],
        "document_types_proposed_ids": [
          "cbddcfc8-d062-4202-b350-f875c04c6aa0",
          "f1ff39d9-aab3-46e3-8749-dad11c04e3b8"
        ],
        "document_types_proposed": [
          {
            "id": "cbddcfc8-d062-4202-b350-f875c04c6aa0",
            "created_at": "2019-08-02T09:56:35.226000",
            "updated_at": null,
            "name": "Floor plans"
          },
          {
            "id": "f1ff39d9-aab3-46e3-8749-dad11c04e3b8",
            "created_at": "2019-08-02T09:56:35.229000",
            "updated_at": null,
            "name": "Other"
          }
        ]
      }
    ]


## Delete a document

`DELETE /api/v1/documents/{document_id}`

## Returns

    {
      "success": true,
      "message": "Deleted 1"
    }

If the document_id does not exist it will raise a 404.
