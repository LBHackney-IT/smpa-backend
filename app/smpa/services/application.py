# -*- coding: utf-8 -*-

"""
    services.application
    ~~~~~~~~~~~~~~~~
    Planning Application services.
"""

from ..models.application import Application, ApplicationStatus

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


_applications = ApplicationService()


class ApplicationStatusService(DService):
    __model__ = ApplicationStatus


_application_statuses = ApplicationStatusService()
