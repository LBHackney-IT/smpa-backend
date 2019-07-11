# User Endpoints

## Get one user

Fetch one user from the backend...

`GET /api/v1/users/{id}`

### Returns

    {
      "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
      "created_at": "2019-07-11T13:18:04.516536",
      "updated_at": "2019-07-11T13:18:04.516577",
      "email": "test@example.com",
      "profile_id": "5abc2971-9903-45db-801b-31366d6ce923",
      "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
      "role": {
        "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
        "created_at": "2019-07-11T13:18:04.587963",
        "updated_at": "2019-07-11T13:18:04.588004",
        "name": "User"
      },
      "profile": {
        "id": "5abc2971-9903-45db-801b-31366d6ce923",
        "created_at": "2019-07-11T13:18:04.552355",
        "updated_at": "2019-07-11T13:18:04.552403",
        "company": {
          "id": null,
          "created_at": "2019-07-11T13:18:04.552553",
          "updated_at": "2019-07-11T13:18:04.552584",
          "company_name": "Acme Architecture",
          "address_line_1": "1 Some Street",
          "address_line_2": "Hackney",
          "city": "London",
          "postcode": "E8 1AA",
          "phone": "02071234567",
          "email": {
            "id": null,
            "created_at": "2019-07-11T13:18:04.552746",
            "updated_at": "2019-07-11T13:18:04.552778",
            "email_address": "test4@example.com",
            "verified": false
          }
        },
        "name": null,
        "email_addresses": null,
        "phone": null
      },
      "verified_at": null
    }


## Update Profile

Update a user's profile...

`PATCH /api/v1/user-profiles/{id}`

**NOTE**: This is a user profile id we send in the URL.

    {
      "id": "5abc2971-9903-45db-801b-31366d6ce923",
      "created_at": "2019-07-11T12:44:58.046853",
      "updated_at": "2019-07-11T12:44:58.046895",
      "company": {
        "id": null,
        "created_at": "2019-07-11T12:44:58.047035",
        "updated_at": "2019-07-11T12:44:58.047057",
        "company_name": "Acme Architecture",
        "address_line_1": "1 Some Street",
        "address_line_2": "Hackney",
        "city": "London",
        "postcode": "E8 1AA",
        "phone": "02071234567",
        "email": {
          "id": null,
          "created_at": "2019-07-11T12:44:58.047242",
          "updated_at": "2019-07-11T12:44:58.047265",
          "email_address": "test4@example.com",
          "verified": false
        }
      },
      "name": null,
      "email_addresses": null,
      "phone": null
    }
