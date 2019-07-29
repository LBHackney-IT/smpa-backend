import os
import envkey  # NOQA
from notifications_python_client.notifications import NotificationsAPIClient


noty = NotificationsAPIClient(os.environ.get('GOV_NOTIFY_API_KEY'))
