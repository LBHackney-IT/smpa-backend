# -*- coding: utf-8 -*-

"""
    services.user
    ~~~~~~~~~~~~~
    User services.
"""

from ..models.user import User, Agent, Applicant

from .rethink import RService


class UserService(RService):
    __model__ = User


class AgentService(RService):
    __model__ = Agent


class ApplicantService(RService):
    __model__ = Applicant


_users = UserService()
_agents = AgentService()
_applicants = ApplicantService()
