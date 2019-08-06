import json
import requests


class GovPayClient:

    def __init__(self, api_key: str) -> None:
        self.base_url = 'https://publicapi.payments.service.gov.uk'
        self.api_version = 'v1'
        self.url = f"{self.base_url}/{self.api_version}"
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            # "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def create_payment(
            self, amount: int, description: str, reference: str,
            application_id: str, payment_id: str):
        """
        Payload should look something like this.
            {
              "amount": 14500,
              "reference" : "12345",
              "description": "Pay your council tax",
              "return_url": "https://your.service.gov.uk/completed"
            }

        Return data looks like this:

        {
            'amount': 10000,
            'description': 'SmPA test',
            'reference': '2019/1234',
            'language': 'en',
            'state': {
                'status': 'created',
                'finished': False
            },
            'payment_id': 'PID',
            'payment_provider': 'sandbox',
            'created_date': '2019-07-29T15:34:21.541Z',
            'refund_summary': {
                'status': 'pending',
                'amount_available': 10000,
                'amount_submitted': 0
            },
            'settlement_summary': {},
            'delayed_capture': False,
            'return_url': 'http://0.0.0.0:5000',
            '_links': {
                'self': {
                    'href': 'https://publicapi.payments.service.gov.uk/v1/payments/PID',
                    'method': 'GET'
                },
                'next_url': {
                    'href': 'https://www.payments.service.gov.uk/secure/SOME_UUID',
                    'method': 'GET'
                },
                'next_url_post': {
                    'type': 'application/x-www-form-urlencoded',
                    'params': {
                        'chargeTokenId': 'b7d609cc-1ebb-42cf-bd27-e9b0ef227d8a'
                    },
                    'href': 'https://www.payments.service.gov.uk/secure',
                    'method': 'POST'
                },
                'events': {
                    'href': 'https://publicapi.payments.service.gov.uk/v1/payments/PID/events',
                    'method': 'GET'
                },
                'refunds': {
                    'href': 'https://publicapi.payments.service.gov.uk/v1/payments/PID/refunds',
                    'method': 'GET'
                },
                'cancel': {
                    'href': 'https://publicapi.payments.service.gov.uk/v1/payments/PID/cancel',
                    'method': 'POST'
                }
            }
        }

        """
        from smpa.app import config
        return_url = config.get_payment_return_url(str(application_id), str(payment_id))
        endpoint = '/payments'
        data = {
            "amount": amount,
            "reference": reference,
            "description": description,
            "return_url": return_url
        }
        rv = requests.post(f'{self.url}{endpoint}', json=data, headers=self.headers)
        return rv

    def check_payment(self, payment_id):
        """Checks the status of a payment.

        {
          "amount": 1200,
          "description": "Your Service Description",
          "reference": "your-reference",
          "language": "en",
          "metadata": {
            "property1": "string",
            "property2": "string"
          },
          "email": "your email",
          "state": {
            "status": "created",
            "finished": true,
            "message": "User cancelled the payment",
            "code": "P010"
          },
          "payment_id": "hu20sqlact5260q2nanm0q8u93",
          "payment_provider": "worldpay",
          "created_date": "2016-01-21T17:15:000Z",
          "refund_summary": {
            "status": "available",
            "amount_available": 100,
            "amount_submitted": 0
          },
          "settlement_summary": {
            "capture_submit_time": "2016-01-21T17:15:000Z",
            "captured_date": "2016-01-21"
          },
          "card_details": {
            "last_digits_card_number": "1234",
            "first_digits_card_number": "123456",
            "cardholder_name": "Mr. Card holder",
            "expiry_date": "12/20",
            "billing_address": {
              "line1": "address line 1",
              "line2": "address line 2",
              "postcode": "AB1 2CD",
              "city": "address city",
              "country": "GB"
            },
            "card_brand": "Visa"
          },
          "delayed_capture": false,
          "corporate_card_surcharge": 250,
          "total_amount": 1450,
          "fee": 5,
          "net_amount": 1195,
          "provider_id": "reference-from-payment-gateway",
          "return_url": "http://your.service.domain/your-reference",
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
              "params": "\"description\":\"This is a value for a parameter called description\"",
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
              "params": "\"description\":\"This is a value for a parameter called description\"",
              "href": "https://an.example.link/from/payment/platform",
              "method": "POST"
            },
            "capture": {
              "type": "application/x-www-form-urlencoded",
              "params": "\"description\":\"This is a value for a parameter called description\"",
              "href": "https://an.example.link/from/payment/platform",
              "method": "POST"
            }
          },
          "card_brand": "Visa"
        }

        """
        endpoint = f'/payments/{payment_id}'
        rv = requests.get(f'{self.url}{endpoint}', headers=self.headers)
        return rv
