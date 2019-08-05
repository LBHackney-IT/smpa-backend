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
      "next_url": "https://www.payments.service.gov.uk/secure/SOME_UUID",
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


## Errors

Errors from the payment gateway will return a 422 response with a JSON response that looks like this...

    {
      "title": {
        "success": false,
        "message": "Invalid attribute value: amount. Must be less than or equal to 10000000",
        "code": "P0102"
      }
    }


## List Payments

`GET /api/v1/payments`

Lists payments for the authenticated user (or all payments if Admin)

    [
      {
        "id": "bf3b6fa7-c6c9-4c7a-8ab9-71bb7e618b64",
        "created_at": "2019-08-05T12:02:16.977000",
        "updated_at": "2019-08-05T12:02:16.977000",
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
        "next_url": "https://www.payments.service.gov.uk/secure/SOME_UUID",
        "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "owner": {
          "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
          "created_at": "2019-08-05T12:02:14.322000",
          "updated_at": "2019-08-05T12:02:14.848000",
          "_id": "5d481ac67fc3fd3cb4d9589a",
          "email": "test@example.com",
          "profile_id": "4f6a0194-77dd-4cae-82c5-3b1767103287",
          "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "role": {
            "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "created_at": "2019-08-05T12:02:13.505000",
            "updated_at": null,
            "name": "User"
          },
          "profile": {
            "id": "4f6a0194-77dd-4cae-82c5-3b1767103287",
            "created_at": "2019-08-05T12:02:14.320000",
            "updated_at": null,
            "company": null,
            "name": null,
            "email_addresses": null,
            "phone": null
          },
          "verified_at": null
        },
        "application_id": "d9ad8830-67bc-45d4-800e-0106fd365cd0"
      }
    ]


## List Payments for a specific application

`GET /api/v1/applications/{application_id}/payments`

Lists payments for the Application with id = application_id

    [
      {
        "id": "bf3b6fa7-c6c9-4c7a-8ab9-71bb7e618b64",
        "created_at": "2019-08-05T12:02:16.977000",
        "updated_at": "2019-08-05T12:02:16.977000",
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
        "next_url": "https://www.payments.service.gov.uk/secure/SOME_UUID",
        "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "owner": {
          "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
          "created_at": "2019-08-05T12:02:14.322000",
          "updated_at": "2019-08-05T12:02:14.848000",
          "_id": "5d481ac67fc3fd3cb4d9589a",
          "email": "test@example.com",
          "profile_id": "4f6a0194-77dd-4cae-82c5-3b1767103287",
          "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "role": {
            "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
            "created_at": "2019-08-05T12:02:13.505000",
            "updated_at": null,
            "name": "User"
          },
          "profile": {
            "id": "4f6a0194-77dd-4cae-82c5-3b1767103287",
            "created_at": "2019-08-05T12:02:14.320000",
            "updated_at": null,
            "company": null,
            "name": null,
            "email_addresses": null,
            "phone": null
          },
          "verified_at": null
        },
        "application_id": "d9ad8830-67bc-45d4-800e-0106fd365cd0"
      }
    ]
