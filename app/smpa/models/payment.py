# -*- coding: utf-8 -*-

"""
    models.unit
    ~~~~~~~~~~~
    Unit models.
"""
from typing import List, Type
from datetime import datetime, date
from schematics.types import (  # NOQA
    StringType, BooleanType, DateTimeType, DateType,
    IntType, UUIDType, ModelType, DictType, ListType
)


from .core import BaseModel, ORMMeta, RelType, ArrowDTType, JSONBlobType
from .user import User


class PaymentState(BaseModel, metaclass=ORMMeta):
    """
    'state': {
        'status': 'created',
        'finished': False,
        # We might get these back with the check status step
        "message": "User cancelled the payment",
        "code": "P010"
    }
    """
    status: str = StringType()
    finished: bool = BooleanType(default=False)
    message: str = StringType()
    code: str = StringType()


class PaymentRefundSummary(BaseModel, metaclass=ORMMeta):
    """
    'refund_summary': {
        'status': 'pending',
        'amount_available': 10000,
        'amount_submitted': 0
    },
    """
    status: str = StringType()
    amount_available: int = IntType()  # Amount in pennies
    amount_submitted: int = IntType()  # Amount in pennies


class PaymentSettlementSummary(BaseModel, metaclass=ORMMeta):
    """
    {
      "capture_submit_time": "2016-01-21T17:15:000Z",
      "captured_date": "2016-01-21"
    }
    """
    capture_submit_time: datetime = ArrowDTType()
    captured_date: date = DateType()


class PaymentBillingAddress(BaseModel, metaclass=ORMMeta):
    """
    "billing_address": {
      "line1": "address line 1",
      "line2": "address line 2",
      "postcode": "AB1 2CD",
      "city": "address city",
      "country": "GB"
    },
    """
    line1: str = StringType()
    line2: str = StringType()
    postcode: str = StringType()
    city: str = StringType()
    country: str = StringType()


class PaymentCardDetails(BaseModel, metaclass=ORMMeta):
    """
    "card_details": {
      "last_digits_card_number": "1234",
      "first_digits_card_number": "123456",
      "cardholder_name": "Mr. Card holder",
      "expiry_date": "12/20",
      "billing_address": {
        "line1": "address line 1",
        "line2": "address line 2",
        "postcode": "AB1 2CD",
        "city": "address city",
        "country": "GB"
      },
      "card_brand": "Visa"
    },
    """
    last_digits_card_number: str = StringType()
    first_digits_card_number: str = StringType()
    cardholder_name: str = StringType()
    expiry_date: str = StringType()
    billing_address: Type[PaymentBillingAddress] = ModelType(PaymentBillingAddress)
    card_brand: str = StringType()


class Payment(BaseModel, metaclass=ORMMeta):

    """These are payment objects within our system. We create them on submit
    from the front end and update them with data from the payments API when we
    receive it.
    """
    amount: int = IntType()  # Amount in pennies
    description: str = StringType(default="Submit my Planning Application payment")
    reference: str = StringType()
    state: PaymentState = ModelType(PaymentState)
    refund_summary: PaymentRefundSummary = ModelType(PaymentRefundSummary)
    payment_id: str = StringType()
    payment_provider: str = StringType()
    created_date: datetime = ArrowDTType()
    settlement_summary: PaymentSettlementSummary = ModelType(PaymentSettlementSummary)
    delayed_capture: bool = BooleanType(default=False)
    return_url: str = StringType()
    next_url: str = StringType()

    # These extra fields come back when we check the status of the payment
    email: str = StringType()
    language: str = StringType()
    corporate_card_surcharge: int = IntType()  # Amount in pennies
    total_amount: int = IntType()  # Amount in pennies
    fee: int = IntType()  # Amount in pennies
    net_amount: int = IntType()  # Amount in pennies
    provider_id: str = StringType()
    card_brand: str = StringType()
    card_details: Type[PaymentCardDetails] = ModelType(PaymentCardDetails)
    metadata: str = JSONBlobType()
    _links: str = JSONBlobType()

    # _links: List[dict] = ListType(DictType())  # Don't think we need to be storing all of these

    owner_id = RelType(
        UUIDType(),
        to_field='owner',
        service='UserService'
    )
    owner: Type[User] = ModelType(User)

    # backref ids
    application_id: str = UUIDType()
