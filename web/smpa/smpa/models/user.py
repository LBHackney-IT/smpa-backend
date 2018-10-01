# -*- coding: utf-8 -*-

"""
    models.user
    ~~~~~~~~~~~
    User models.
"""

# 3rd party
import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.associationproxy import association_proxy

# Project
from ..helpers.database import MyUUID

# Module
from .core import BaseModel


class User(BaseModel):

    """A User object.

    Attributes:
        family_name (Unicode): proxy to PersonName.family_name
        given_name (Unicode): proxy to PersonName.given_name
        person_name (PersonName): The PersonName instance for this user
        title (Unicode): proxy to PersonName.title
    """

    __tablename__ = 'users'

    # Relationships
    person_name_id = sa.Column(MyUUID, sa.ForeignKey('person_names.id'))
    person_name = relationship(
        'PersonName',
        backref=backref('user', uselist=False)
    )

    preferred_contact_method_id = sa.Column(MyUUID, sa.ForeignKey('contact_methods.id'))
    preferred_contact_method = relationship(
        'ContactMethod',
        backref=backref('user', uselist=False)
    )

    primary_email_id = sa.Column(MyUUID, sa.ForeignKey('emails.id'))
    primary_email = relationship(
        'Email',
        backref=backref('user', uselist=False)
    )

    primary_phone_id = sa.Column(MyUUID, sa.ForeignKey('telephone_numbers.id'))
    primary_phone = relationship(
        'TelephoneNumber',
        backref=backref('user', uselist=False)
    )

    # Relationships defined elsewhere
    email_addresses = relationship("EmailAddress", back_populates="user")

    # Proxies
    title = association_proxy('person_name', 'title')
    given_name = association_proxy('person_name', 'given_name')
    family_name = association_proxy('person_name', 'family_name')

    def __str__(self):
        return f'<User: {self.first_name} {self.last_name}>'


class PersonName(BaseModel):

    """A Person's name

    Attributes:
        title (Unicode): The person's title
        given_name (Unicode): The given name
        family_name (Unicode): Family / surname
    """

    __tablename__ = 'person_names'

    title = sa.Column(sa.Unicode(255))
    given_name = sa.Column(sa.Unicode(255))
    family_name = sa.Column(sa.Unicode(255))

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.title} {self.given_name} {self.family_name}>'


class Email(BaseModel):

    """An email address. Allows us to store a list of email addresses against
    a user and set one as the preferred.


    Attributes:
        email_address (Unicode): The email address
        verified (bool): Has the user verified this email address?
        user (Unicode): The user this email address belongs to
    """

    __tablename__ = 'emails'

    email_address = sa.Column(sa.Unicode(255), nullable=False)
    verified = sa.Column(sa.Boolean(), default=False)

    # Relationships
    user = relationship('User', backref=backref('email_addresses', uselist=True))


class TelephoneNumber(BaseModel):

    """A Telephone number.

    Attributes:
        tel_number (Unicode): The telephone number.
        tel_type (TYPE): Description
    """

    __tablename__ = 'telephone_numbers'

    tel_number = sa.Column(sa.Unicode(255), nullable=False)
    tel_type = sa.Column(MyUUID, sa.ForeignKey('telephone_number_types.id'))


class TelephoneNumberType(BaseModel):

    """Telephone number types. ie: Landline, work, home, fax, mobile

    Attributes:
        name (Unicode): The name of this type
    """

    __tablename__ = 'telephone_number_types'

    name = sa.Column(sa.Unicode(255), nullable=False)


class ContactMethod(BaseModel):

    """The preferred contact method for a user. ie: SMS, fax, phone, post

    Attributes:
        name (Unicode): The name of the preferred contact method
    """

    __tablename__ = 'contact_methods'

    name = sa.Column(sa.Unicode(255), nullable=False)


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

    @declared_attr
    def name_id(self):
        return sa.Column(MyUUID, sa.ForeignKey('person_names.id'))

    @declared_attr
    def company_name_id(self):
        return sa.Column(sa.Unicode(255), nullable=True)

    @declared_attr
    def address_id(self):
        return sa.Column(MyUUID, sa.ForeignKey('addresses.id'))

    @declared_attr
    def telephone_numbers(self):
        return relationship('TelephoneNumber', backref=backref('owner', uselist=False))

    @declared_attr
    def email_addresses(self):
        return relationship('EmailAddress', backref=backref('owner', uselist=False))


class Applicant(BasePerson):
    __tablename__ = 'applicants'


class Agent(BasePerson):
    __tablename__ = 'agents'
