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
import arrow

from .core import BaseModel, ORMMeta, RelType
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


class CompanyProfile(BaseModel, metaclass=ORMMeta):

    """A Company Profile
    """
    company_name: str = StringType(max_length=255)
    address_line_1: str = StringType(max_length=255)
    address_line_2: str = StringType(max_length=255)
    city: str = StringType(max_length=255)
    postcode: str = StringType(max_length=255)
    phone: str = StringType(max_length=255)
    email: str = ModelType(Email)


class UserProfile(BaseModel, metaclass=ORMMeta):

    """A User object.

    Attributes:
        family_name (Unicode): proxy to PersonName.family_name
        given_name (Unicode): proxy to PersonName.given_name
        person_name (PersonName): The PersonName instance for this user
        title (Unicode): proxy to PersonName.title
    """
    company = ModelType(CompanyProfile)
    name: Type[PersonName] = ModelType(PersonName)
    email_addresses: List[Type[Email]] = ListType(ModelType(Email))
    primary_email_id: str = UUIDType()
    primary_phone_id: str = UUIDType()

    preferred_contact_method: Type[ContactMethod] = ModelType(ContactMethod)


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
            'default': blacklist('password', 'verification_key')
        }

    email: str = StringType(max_length=200, required=True)
    password: str = StringType(max_length=100, required=True)
    profile_id = RelType(
        UUIDType(),
        to_field='profile',
        service='UserProfileService'
    )
    role_id = RelType(
        UUIDType(),
        to_field='role',
        service='RoleService'
    )

    role: Type[Role] = ModelType(Role)
    profile: Type[UserProfile] = ModelType(UserProfile)

    verified_at = DateTimeType()
    verification_key = UUIDType()

    @property
    def verified(self):
        """Tries to get an arrow datetime from self.verified_at
        Returns True if it succeeds, false if not

        Returns:
            bool: Whether or not the user's account is verified
        """
        try:
            arrow.get(self.verified_at)
        except Exception:
            return False
        else:
            return True

    @property
    def is_admin(self):
        self.export()
        if 'Admin' in self.role.name:
            return True
        return False

    def __str__(self):
        return f'<User: {self.email}>'
