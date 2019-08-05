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


from .core import BaseModel, ORMMeta, RelType, ArrowDTType
from .user import User


class PaymentState(BaseModel, metaclass=ORMMeta):
    """
    'state': {
        'status': 'created',
        'finished': False
    }
    """
    status: str = StringType()
    finished: bool = BooleanType(default=False)


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
    capture_submit_time: datetime = DateTimeType()
    captured_date: date = DateType()


class PaymentLink(BaseModel, metaclass=ORMMeta):
    """
    {
      "capture_submit_time": "2016-01-21T17:15:000Z",
      "captured_date": "2016-01-21"
    }
    """
    capture_submit_time: datetime = DateTimeType()
    captured_date: date = DateType()


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
    # _links: List[dict] = ListType(DictType())  # Don't think we need to be storing these

    owner_id = RelType(
        UUIDType(),
        to_field='owner',
        service='UserService'
    )
    owner: Type[User] = ModelType(User)

    # backref ids
    application_id: str = UUIDType()
