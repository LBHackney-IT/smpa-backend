# 1. Starting the works

![](/static/screen1.png)

`POST /api/v1/applications`

    works_started: bool
    date_works_started: date
    works_completed: bool
    date_works_completed: date
    works_description: str

### Returns

    application: json

    {
      "id": "f83db82f-36cd-4d57-a14c-381b0886a97d",
      "created_at": "2019-04-04T14:38:37.844316",
      "updated_at": "2019-04-04T14:38:37.844356",
      "works_started": false,
      "date_works_started": null,
      "works_completed": false,
      "date_works_completed": null,
      "works_description": null,
      "owner_id": null,
      "owner": null,
      "site_address": null
    }
