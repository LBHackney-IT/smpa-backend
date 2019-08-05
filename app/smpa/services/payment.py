# -*- coding: utf-8 -*-

"""
    services.payment
    ~~~~~~~~~~~~~~~~
    Services for payments
"""

import falcon
import arrow
from .mongo import DService

from smpa.models.payment import Payment
from smpa.helpers.govpay.client import GovPayClient


class PaymentService(DService):
    __model__ = Payment

    def create(self, req, application_id):
        """
        Errors from GovPay look like this...

        {
          "field": "amount",
          "code": "P0102",
          "description": "Invalid attribute value: amount. Must be less than or equal to 10000000"
        }

        The create application payment method needs to...
        1. Generate a unique reference number
        2. Call govpay.create_payment
        3. Create a Payment model
        4. Return that Payment model

        Args:
            **kwargs: Description

        """
        from smpa.app import config
        govpay = GovPayClient(config.GOV_PAY_API_KEY)
        yyyy = arrow.now().year
        nnnn = 5000 + self.count()
        ref = f"{yyyy}/{nnnn}"
        amount = config.PAYMENT_AMOUNT
        description = config.PAYMENT_DESCRIPTION
        user = req.context['user']
        user.export()

        # Create the payment
        rv = govpay.create_payment(amount=amount, description=description, reference=ref)
        j = rv.json()
        if rv.status_code == 201:
            payment = self.new(json=j)
            payment.owner_id = str(user.id)
            payment.application_id = str(application_id)
            payment = _payments.save(payment)
            return payment
        else:
            response = {
                "success": False,
                "message": j['description'],
                'code': j['code']
            }
            raise falcon.HTTPError(falcon.HTTP_422, response)


_payments = PaymentService()
