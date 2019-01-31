# -*- coding: utf-8 -*-

"""
    models.user
    ~~~~~~~~~~~
    User models.
"""

from .core import BaseModel, ORMMeta
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, IntType, UUIDType, ListType
)


class User(BaseModel, metaclass=ORMMeta):

    """A User object.

    Attributes:
        family_name (Unicode): proxy to PersonName.family_name
        given_name (Unicode): proxy to PersonName.given_name
        person_name (PersonName): The PersonName instance for this user
        title (Unicode): proxy to PersonName.title
    """

    # Relationships
    person_name_id = UUIDType()
    preferred_contact_method_id = UUIDType()
    primary_email_id = UUIDType()
    primary_phone_id = UUIDType()

    def __str__(self):
        return f'<User: {self.first_name} {self.last_name}>'


class PersonName(BaseModel, metaclass=ORMMeta):

    """A Person's name

    Attributes:
        title (Unicode): The person's title
        given_name (Unicode): The given name
        family_name (Unicode): Family / surname
    """

    title = StringType(max_length=100, required=True)
    given_name = StringType(max_length=255, required=True)
    family_name = StringType(max_length=255, required=True)

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.title} {self.given_name} {self.family_name}>'


class Email(BaseModel, metaclass=ORMMeta):

    """An email address. Allows us to store a list of email addresses against
    a user and set one as the preferred.


    Attributes:
        email_address (Unicode): The email address
        verified (bool): Has the user verified this email address?
        user (Unicode): The user this email address belongs to
    """
    email_address = StringType(max_length=255, required=True)
    verified = BooleanType(default=False)

    # TODO: Relationships
    # user = relationship('User', backref=backref('email_addresses', uselist=True))


class TelephoneNumber(BaseModel, metaclass=ORMMeta):

    """A Telephone number.

    Attributes:
        tel_number (Unicode): The telephone number.
        tel_type (TYPE): Description
    """
    tel_number = StringType(max_length=100, required=True)
    tel_type_id = UUIDType()


class TelephoneNumberType(BaseModel, metaclass=ORMMeta):

    """Telephone number types. ie: Landline, work, home, fax, mobile

    Attributes:
        name (Unicode): The name of this type
    """
    name = StringType(max_length=100, required=True)


class ContactMethod(BaseModel, metaclass=ORMMeta):

    """The preferred contact method for a user. ie: SMS, fax, phone, post

    Attributes:
        name (Unicode): The name of the preferred contact method
    """
    name = StringType(max_length=100, required=True)


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

    name_id = UUIDType()
    company_name_id = UUIDType()
    address_id = UUIDType()
    telephone_number_ids = ListType(UUIDType)
    email_addresses_ids = ListType(UUIDType)


class Applicant(BasePerson, metaclass=ORMMeta):
    pass


class Agent(BasePerson, metaclass=ORMMeta):
    pass
