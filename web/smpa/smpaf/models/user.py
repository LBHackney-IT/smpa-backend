# -*- coding: utf-8 -*-

"""
    models.user
    ~~~~~~~~~~~
    User models.

    {"name": {"title": "Mr", "given_name": "Andy", "family_name": "Beaumont"}}

    {"email_addresses":
        [
            {"email_address": "andy@hactar.is"},
            {"email_address": "andy@andybeaumont.com"}
        ]
    }
"""

from .core import BaseModel, ORMMeta
from schematics.types.serializable import serializable
from schematics.transforms import blacklist
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType, ModelType
)
from marshmallow import fields, validate, pprint


class Role(BaseModel, metaclass=ORMMeta):

    """User roles. Like Admin etc.
    """
    name: str = fields.Str(validate=validate.Length(max=100), required=True)


class PersonName(BaseModel, metaclass=ORMMeta):

    """A Person's name

    Attributes:
        title (Unicode): The person's title
        given_name (Unicode): The given name
        family_name (Unicode): Family / surname
    """

    title = fields.Str(validate=validate.Length(max=100), required=True)
    given_name = fields.Str(validate=validate.Length(max=255), required=True)
    family_name = fields.Str(validate=validate.Length(max=255), required=True)

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.title} {self.given_name} {self.family_name}>'


class ContactMethod(BaseModel, metaclass=ORMMeta):

    """The preferred contact method for a user. ie: SMS, fax, phone, post

    Attributes:
        name (Unicode): The name of the preferred contact method
    """
    name: str = fields.Str(validate=validate.Length(max=100), required=True)


class Email(BaseModel, metaclass=ORMMeta):

    """An email address. Allows us to store a list of email addresses against
    a user and set one as the preferred.


    Attributes:
        email_address (Unicode): The email address
        verified (bool): Has the user verified this email address?
        user (Unicode): The user this email address belongs to
    """
    email_address = fields.Str(validate=validate.Length(max=255), required=True)
    verified = fields.Boolean(default=False)

    # TODO: Relationships
    # user = relationship('User', backref=backref('email_addresses', uselist=True))


class UserProfile(BaseModel, metaclass=ORMMeta):

    """A User object.

    Attributes:
        family_name (Unicode): proxy to PersonName.family_name
        given_name (Unicode): proxy to PersonName.given_name
        person_name (PersonName): The PersonName instance for this user
        title (Unicode): proxy to PersonName.title
    """

    name = fields.Nested(PersonName)
    preferred_contact_method = fields.Nested(ContactMethod)
    email_addresses = fields.List(fields.Nested(Email))
    primary_email_id = fields.UUID()
    primary_phone_id = fields.UUID()


class TelephoneNumber(BaseModel, metaclass=ORMMeta):

    """A Telephone number.

    Attributes:
        tel_number (Unicode): The telephone number.
        tel_type (TYPE): Description
    """
    tel_number = fields.Str(validate=validate.Length(max=100), required=True)
    tel_type_id = fields.UUID()


class TelephoneNumberType(BaseModel, metaclass=ORMMeta):

    """Telephone number types. ie: Landline, work, home, fax, mobile

    Attributes:
        name (Unicode): The name of this type
    """
    name: str = fields.Str(validate=validate.Length(max=100), required=True)


class BasePerson(BaseModel):

    """A base Person model. Use this to create other people types.

    Attributes:
        name (PersonName): Holds the name details for this person
        company_name (Unicode): Name of the company this person is representing
        address (Address): This person's address
        telephone_numbers (list): Telephone numbers for this person
        email_addresses (list): Email addresses for this person
    """

    __abstract__ = True

    name_id = fields.UUID()
    company_name_id = fields.UUID()
    address_id = fields.UUID()
    telephone_number_ids = fields.List(fields.UUID())
    email_addresses_ids = fields.List(fields.UUID())


class Applicant(BasePerson, metaclass=ORMMeta):
    pass


class Agent(BasePerson, metaclass=ORMMeta):
    pass


class User(BaseModel, metaclass=ORMMeta):

    """Super simple user model to facilitate auth. All profile information
    should live on other models.
    Passwords are stored bcrypt hashed via passlib
    """

    class Options:
        roles = {'default': blacklist('password', 'profile_id', 'role_id')}

    email = fields.Str(validate=validate.Length(max=200), required=True)
    password = fields.Str(validate=validate.Length(max=100), required=True)
    profile_id = fields.UUID()
    role_id = fields.UUID()

    @serializable
    def profile(self):
        from ..services.user import _user_profiles
        return _user_profiles.get(id=str(self.profile_id)).to_native()

    @serializable
    def role(self):
        from ..services.user import _roles
        return _roles.get(id=str(self.role_id)).to_native()

    def __str__(self):
        return f'<User: {self.email}>'
