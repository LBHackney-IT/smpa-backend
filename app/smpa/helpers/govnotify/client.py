import os
import falcon
import envkey  # NOQA
from typing import Type, List, Dict
from notifications_python_client.notifications import NotificationsAPIClient


TEMPLATE_IDS: Dict[str, str] = {
    'password_reset': 'fda4a110-5ad3-40d8-9185-11a627f70766',
    'account_verify': 'd4c144d2-3cb6-400e-bdb6-6b0dd5dbd087'
}


class GovNotifyClient:
    """Initialise with...

        notify = GovNotifyClient(os.environ.get('GOV_NOTIFY_API_KEY'))

    """

    def __init__(self, api_key: str) -> None:
        self.client = NotificationsAPIClient(api_key)

    def send_password_reset(self, email: str, name: str, reset_link: str):
        data = {
            'name': name,
            'link': reset_link
        }
        template = TEMPLATE_IDS['password_reset']
        rv = self._send_email(email, template, data)
        return rv

    def send_verify_account(self, email: str, verify_link: str):
        data = {
            'link': verify_link
        }
        template = TEMPLATE_IDS['account_verify']
        rv = self._send_email(email, template, data)
        return rv

    def _send_email(self, email: str, template: str, data: dict):
        """Send an email via Gov.UK Notify

        client returns...

        {
            'content': {
                'body': email body goes here
                'from_email': 'submit.my.planning.application@notifications.service.gov.uk',
                'subject': 'Confirm your Submit my Planning Application account'
            },
            'id': '91626a62-4557-46d8-90a1-7303b75f9f78',
            'reference': None,
            'scheduled_for': None,
            'template': {
                'id': 'd4c144d2-3cb6-400e-bdb6-6b0dd5dbd087',
                'uri': template url goes here
                'version': 1
            },
            'uri': some other url goes here
        }

        Args:
            data (dict): Dict of k,v pairs for inserting vairables into the message template
        """
        rv = self.client.send_email_notification(
            email_address=email,
            template_id=template,
            personalisation=data
        )
        return rv
