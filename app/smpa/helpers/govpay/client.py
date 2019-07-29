import json
import requests


class GovPayClient:

    def __init__(self, api_key: str) -> None:
        self.return_url = "http://0.0.0.0:5000"
        self.base_url = 'https://publicapi.payments.service.gov.uk'
        self.api_version = 'v1'
        self.url = f"{self.base_url}/{self.api_version}"
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            # "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def create_payment(self, amount: int, description: str, reference: str):
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
        endpoint = '/payments'
        data = {
            "amount": amount,
            "reference": reference,
            "description": description,
            "return_url": self.return_url
        }
        rv = requests.post(f'{self.url}{endpoint}', json=data, headers=self.headers)
        return rv
