# -*- coding: utf-8 -*-

"""
    services.application
    ~~~~~~~~~~~~~~~~
    Planning Application services.
"""
import arrow
from ..models.application import Application, ApplicationStatus

from smpa.helpers.console import console
from .mongo import DService


class ApplicationService(DService):
    __model__ = Application

    def new(self, *args, **kwargs):
        m = super().new(*args, **kwargs)
        m.reference = f'DRAFT/{self.count()}'
        m.status_id = "68e32fcc-5898-4bd1-bfad-d2f14c1d6306"
        return m

    def create(self, *args, **kwargs):
        kwargs = self._preprocess(**kwargs)
        j = self._jsonify(kwargs)
        j = self._set_id(j)
        j['reference'] = f'DRAFT/{self.count()}'
        j['status_id'] = "68e32fcc-5898-4bd1-bfad-d2f14c1d6306"
        if isinstance(j, list):
            rv = self._insert_some(j)
        else:
            rv = self._insert_one(j)

        return rv

    def submit(self, id: str) -> Application:
        """Submit an application to the planning department.

        Args:
            id (str): The id of the application we want to submit
        """
        application = self.get(id)
        application.status_id = "5aa415fa-9b25-4828-ac06-cb1ab9b000ea"
        application.submitted_at = arrow.now().datetime
        if 'DRAFT' in application.reference:
            application.reference = self.next_reference()
        rv = _applications.save(application)
        # Send a notification to the planning team
        from smpa.app import govnotify
        try:
            govnotify.send_submission_received(rv)
        except Exception as e:
            console.error('Failed to send email')
            console.error(e)
        return rv

    def next_reference(self):
        yyyy = arrow.now().year
        nnnn = 5000 + _applications.count(status_id="5aa415fa-9b25-4828-ac06-cb1ab9b000ea")
        ref = f"{yyyy}/{nnnn}"
        return ref


_applications = ApplicationService()


class ApplicationStatusService(DService):
    __model__ = ApplicationStatus


_application_statuses = ApplicationStatusService()
