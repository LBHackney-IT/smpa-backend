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


## Check Payment status

`GET /api/v1/payments/{id}/check`

This triggers a call to GovUK Pay to check the status of a payment.

### Returns

This returns an updated payment instance

    {
      "id": "b70e30a5-b126-4906-a98f-64f8448adab9",
      "created_at": "2019-08-05T14:15:31.440000",
      "updated_at": "2019-08-05T14:15:31.440000",
      "amount": 1200,
      "description": "Your Service Description",
      "reference": "your-reference",
      "state": {
        "id": null,
        "created_at": null,
        "updated_at": null,
        "status": "created",
        "finished": true,
        "message": "User cancelled the payment",
        "code": "P010"
      },
      "refund_summary": {
        "id": null,
        "created_at": null,
        "updated_at": null,
        "status": "available",
        "amount_available": 100,
        "amount_submitted": 0
      },
      "payment_id": "hu20sqlact5260q2nanm0q8u93",
      "payment_provider": "worldpay",
      "created_date": "2016-01-21T17:15:00+00:00",
      "settlement_summary": {
        "id": null,
        "created_at": null,
        "updated_at": null,
        "capture_submit_time": "2016-01-21T17:15:00+00:00",
        "captured_date": "2016-01-21"
      },
      "delayed_capture": false,
      "return_url": "http://your.service.domain/your-reference",
      "next_url": "https://www.payments.service.gov.uk/secure/SOME_UUID",
      "email": "your email",
      "language": "en",
      "corporate_card_surcharge": 250,
      "total_amount": 1450,
      "fee": 5,
      "net_amount": 1195,
      "provider_id": "reference-from-payment-gateway",
      "card_brand": "Visa",
      "card_details": {
        "id": null,
        "created_at": null,
        "updated_at": null,
        "last_digits_card_number": "1234",
        "first_digits_card_number": "123456",
        "cardholder_name": "Mr. Card holder",
        "expiry_date": "12/20",
        "billing_address": {
          "id": null,
          "created_at": null,
          "updated_at": null,
          "line1": "address line 1",
          "line2": "address line 2",
          "postcode": "AB1 2CD",
          "city": "address city",
          "country": "GB"
        },
        "card_brand": "Visa"
      },
      "metadata": {
        "property1": "string",
        "property2": "string"
      },
      "_links": {
        "self": {
          "href": "https://an.example.link/from/payment/platform",
          "method": "GET"
        },
        "next_url": {
          "href": "https://an.example.link/from/payment/platform",
          "method": "GET"
        },
        "next_url_post": {
          "type": "application/x-www-form-urlencoded",
          "params": {
            "description": "This is a value for a parameter called description"
          },
          "href": "https://an.example.link/from/payment/platform",
          "method": "POST"
        },
        "events": {
          "href": "https://an.example.link/from/payment/platform",
          "method": "GET"
        },
        "refunds": {
          "href": "https://an.example.link/from/payment/platform",
          "method": "GET"
        },
        "cancel": {
          "type": "application/x-www-form-urlencoded",
          "params": {
            "description": "This is a value for a parameter called description"
          },
          "href": "https://an.example.link/from/payment/platform",
          "method": "POST"
        },
        "capture": {
          "type": "application/x-www-form-urlencoded",
          "params": {
            "description": "This is a value for a parameter called description"
          },
          "href": "https://an.example.link/from/payment/platform",
          "method": "POST"
        }
      },
      "owner_id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
      "owner": {
        "id": "b7d623db-5b4a-43df-b3f1-2bfca845d657",
        "created_at": "2019-08-05T14:15:28.778000",
        "updated_at": "2019-08-05T14:15:29.328000",
        "_id": "5d483a004c820ff0cf14f694",
        "email": "test@example.com",
        "profile_id": "ecf39f20-f8f9-4eea-9467-2adb0fbdbd5c",
        "role_id": "831083f5-b7c9-4967-8561-ac4011be54e4",
        "role": {
          "id": "831083f5-b7c9-4967-8561-ac4011be54e4",
          "created_at": "2019-08-05T14:15:27.960000",
          "updated_at": null,
          "name": "User"
        },
        "profile": {
          "id": "ecf39f20-f8f9-4eea-9467-2adb0fbdbd5c",
          "created_at": "2019-08-05T14:15:28.775000",
          "updated_at": null,
          "company": null,
          "name": null,
          "email_addresses": null,
          "phone": null
        },
        "verified_at": null
      },
      "application_id": "385c40e9-edbd-444a-8224-8b9d5ecca257"
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
