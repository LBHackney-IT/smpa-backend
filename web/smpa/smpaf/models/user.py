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
from typing import (  # NOQA
    TYPE_CHECKING, Any, Callable, ClassVar, List, Dict, Generator, Optional,
    Set, Tuple, Type, Union, cast, no_type_check
)
from schematics.transforms import blacklist
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType, ModelType
)


class Role(BaseModel, metaclass=ORMMeta):

    """User roles. Like Admin etc.
    """
    name: str = StringType(max_length=100, required=True)


class PersonName(BaseModel, metaclass=ORMMeta):

    """A Person's name

    Attributes:
        title (Unicode): The person's title
        given_name (Unicode): The given name
        family_name (Unicode): Family / surname
    """

    title: str = StringType(max_length=100, required=True)
    given_name: str = StringType(max_length=255, required=True)
    family_name: str = StringType(max_length=255, required=True)

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.title} {self.given_name} {self.family_name}>'


class ContactMethod(BaseModel, metaclass=ORMMeta):

    """The preferred contact method for a user. ie: SMS, fax, phone, post

    Attributes:
        name (Unicode): The name of the preferred contact method
    """
    name: str = StringType(max_length=100, required=True)


class Email(BaseModel, metaclass=ORMMeta):

    """An email address. Allows us to store a list of email addresses against
    a user and set one as the preferred.


    Attributes:
        email_address (Unicode): The email address
        verified (bool): Has the user verified this email address?
        user (Unicode): The user this email address belongs to
    """
    email_address: str = StringType(max_length=255, required=True)
    verified: bool = BooleanType(default=False)

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

    name: Type[PersonName] = ModelType(PersonName)
    preferred_contact_method: Type[ContactMethod] = ModelType(ContactMethod)
    email_addresses: List[Type[Email]] = ListType(ModelType(Email))
    primary_email_id: str = UUIDType()
    primary_phone_id: str = UUIDType()


class TelephoneNumber(BaseModel, metaclass=ORMMeta):

    """A Telephone number.

    Attributes:
        tel_number (Unicode): The telephone number.
        tel_type (TYPE): Description
    """
    tel_number: str = StringType(max_length=100, required=True)
    tel_type_id: str = UUIDType()


class TelephoneNumberType(BaseModel, metaclass=ORMMeta):

    """Telephone number types. ie: Landline, work, home, fax, mobile

    Attributes:
        name (Unicode): The name of this type
    """
    name: str = StringType(max_length=100, required=True)


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

    name_id: str = UUIDType()
    company_name_id: str = UUIDType()
    address_id: str = UUIDType()
    telephone_number_ids = ListType(UUIDType)
    email_addresses_ids = ListType(UUIDType)


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
        roles = {
            'default': blacklist('password', 'profile_id', 'role_id')
        }

    email: str = StringType(max_length=200, required=True)
    password: str = StringType(max_length=100, required=True)
    profile_id: str = UUIDType()
    role_id: str = UUIDType()

    #
    # Dynamic relations
    #
    related = {
        'profile_id': '_user_profiles',
        'role_id': '_roles',
    }
    role: Type[Role] = ModelType(Role)
    profile: Type[UserProfile] = ModelType(UserProfile)

    def __str__(self):
        return f'<User: {self.email}>'
