# 34. Payments

## Create a Payment

![](/static/screen38.png)

### Example

`POST /api/v1/applications/{application_id}/payments`

    {}


### Returns

    {
      "id": "f6591ad1-2c6c-4001-bc5c-0ff4ca55078d",
      "created_at": "2019-08-05T10:41:52.403000",
      "updated_at": "2019-08-05T10:41:52.403000",
      "amount": 10000,
      "description": "SmPA test",
      "reference": "2019/1234",
      "state": {
        "id": null,
        "created_at": null,
        "updated_at": null,
        "status": "created",
        "finished": false
      },
      "refund_summary": {
        "id": null,
        "created_at": null,
        "updated_at": null,
        "status": "pending",
        "amount_available": 10000,
        "amount_submitted": 0
      },
      "payment_id": "PID",
      "payment_provider": "sandbox",
      "created_date": "2019-07-29T15:34:21.541000+00:00",
      "settlement_summary": {
        "id": null,
        "created_at": null,
        "updated_at": null,
        "capture_submit_time": null,
        "captured_date": null
      },
      "delayed_capture": false,
      "return_url": "http://0.0.0.0:5000",
      "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
      "owner": {
        "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "created_at": "2019-08-05T10:41:49.738000",
        "updated_at": "2019-08-05T10:41:50.281000",
        "_id": "5d4807ed4d4739c881c2ac29",
        "email": "test@example.com",
        "profile_id": "ac863647-7220-4d04-b326-2c4129959b12",
        "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
        "role": {
          "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "created_at": "2019-08-05T10:41:48.937000",
          "updated_at": null,
          "name": "User"
        },
        "profile": {
          "id": "ac863647-7220-4d04-b326-2c4129959b12",
          "created_at": "2019-08-05T10:41:49.736000",
          "updated_at": null,
          "company": null,
          "name": null,
          "email_addresses": null,
          "phone": null
        },
        "verified_at": null
      },
      "application_id": "42e726d4-0cee-43b6-90ec-ce5b32fadb2d"
    }
