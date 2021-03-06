import os
import falcon
import arrow
import envkey  # NOQA
from typing import Type, List, Dict
from notifications_python_client.notifications import NotificationsAPIClient

from smpa.models.application import Application


TEMPLATE_IDS: Dict[str, str] = {
    'password_reset': 'a5dbad93-8dca-4f60-b275-de0931e1e07b',
    'account_verify': 'd4c144d2-3cb6-400e-bdb6-6b0dd5dbd087',
    'submitted': 'e0936b6c-c938-4fa1-a48a-2cd8ae470540',
    'submission_received': '4743ee3d-1858-4497-9256-acce5150594e'
}


class GovNotifyClient:
    """Initialise with...

        notify = GovNotifyClient(os.environ.get('GOV_NOTIFY_API_KEY'))

    """

    def __init__(self, api_key: str) -> None:
        self.client = NotificationsAPIClient(api_key)

    def send_submission_received(self, application: Application):
        from smpa.app import config
        email = config.NOTIFICATIONS_NOTIFY
        data = {
            'reference': application.reference,
            'submitted_at': arrow.get(application.submitted_at).isoformat(),
            'address': application.short_address,
            'view_link': config.get_view_application_url(str(application.id))
        }
        template = TEMPLATE_IDS['submission_received']
        rv = self._send_email(email, template, data)
        return rv

    def send_submitted(self, application: Application):
        from smpa.app import config
        application.export()  # We do this to populate the relationships
        email = application.owner.email
        try:
            name = application.owner.profile.name
        except Exception:
            name = ''
        data = {
            'name': name,
            'reference_number': application.reference,
            'address': application.short_address,
            'link': config.get_view_application_url(str(application.id))
        }
        template = TEMPLATE_IDS['submitted']
        rv = self._send_email(email, template, data)
        return rv

    def send_password_reset(self, email: str, reset_link: str):
        data = {
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
        if os.environ.get('SERVER_ENV') != 'test':
            rv = self._send_email(email, template, data)
            return rv
        else:
            return verify_link

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
