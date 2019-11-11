# -*- coding: utf-8 -*-

"""
    services.application
    ~~~~~~~~~~~~~~~~
    Planning Application services.
"""
import arrow
from typing import Optional
from ..models.application import Application, ApplicationStatus, ApplicationReference

from smpa.helpers.console import console
from .mongo import DService


class ApplicationStatusService(DService):
    __model__ = ApplicationStatus


_application_statuses = ApplicationStatusService()


class ApplicationReferenceService(DService):
    __model__ = ApplicationReference

    def next(self):
        y = arrow.now().year
        obj = self.get_or_create(year=y)
        if obj.counter is None:
            obj.counter = 5010
            obj = self.save(obj)
        else:
            obj = self._increment(str(obj.id))

        return f"{y}/{obj.counter}"

    def _increment(self, id: str):
        self.q.update_one({'id': id}, {'$inc': {'counter': 1}})
        return self.get(id)


_application_references = ApplicationReferenceService()


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

    def submitted(self, since: Optional[str] = None, *args, **kwargs):
        """Get only submitted applications. If passed a since, only retrieve applications
        that have a submitted_at > since.

        Args:
            since (Optional[str], optional): The date you want applications since. ie: '2019-09-01'
        """
        if since is None:
            query = self.q.find({'submitted_at': {'$ne': None}})
        else:
            query = self.q.find({'submitted_at': {'$gt': since}})

        rv = [self._model_out(obj) for obj in query]
        return rv

    def submit(self, id: str) -> Application:
        """Submit an application to the planning department.

        Args:
            id (str): The id of the application we want to submit
        """
        application = self.get(id)
        status = _application_statuses.get("5aa415fa-9b25-4828-ac06-cb1ab9b000ea")
        application.status_id = "5aa415fa-9b25-4828-ac06-cb1ab9b000ea"
        application.status = status
        application.submitted_at = arrow.utcnow().datetime
        if 'DRAFT' in application.reference:
            application.reference = _application_references.next()

        rv = _applications.save(application)
        # Send a notification to the planning team
        from smpa.app import govnotify
        try:
            govnotify.send_submission_received(rv)
        except Exception as e:
            console.error('Failed to send email')
            console.error(e)

        try:
            govnotify.send_submitted(rv)
        except Exception as e:
            console.error('Failed to send email')
            console.error(e)
        return rv


_applications = ApplicationService()
