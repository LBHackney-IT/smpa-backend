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


class PaymentService(DService):
    __model__ = Payment

    def check(self, id):
        """Checks the status of a payment on GovPay
        """
        from smpa.app import govpay
        payment = _payments.get(str(id))
        if payment.payment_id is None:
            raise falcon.HTTPError(falcon.HTTP_404, 'Payment not found')

        rv = govpay.check_payment(payment.payment_id)
        j = rv.json()
        if rv.status_code == 200:
            payment = _payments.update(id=payment.id, json=j)
            return payment

        else:
            response = {
                "success": False
            }
            if j.get('description', None) is not None:
                response["message"] = j.get('description')
            if j.get('code', None) is not None:
                response["code"] = j.get('code')

            raise falcon.HTTPError(falcon.HTTP_422, response)

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
        from smpa.app import config, govpay
        from .application import _applications, _application_references
        ref = _application_references.next()
        application = _applications.get(application_id)
        application.reference = ref
        _applications.save(application)
        amount = config.PAYMENT_AMOUNT
        description = config.PAYMENT_DESCRIPTION
        user = req.context['user']
        user.export()

        # Create a local payment object first so we have an ID
        payment = self.new()
        payment.owner_id = str(user.id)
        payment.application_id = str(application_id)
        payment = _payments.save(payment)

        # Create the payment
        rv = govpay.create_payment(
            amount=amount,
            description=description,
            reference=ref,
            application_id=application_id,
            payment_id=str(payment.id)
        )
        j = rv.json()
        if rv.status_code == 201:
            payment = _payments.update(id=str(payment.id), json=j)
            payment.next_url = j['_links']['next_url']['href']
            payment = _payments.save(payment)
            # Update the application with a reference
            application = _applications.get(str(application_id))
            application.reference = ref
            _applications.save(application)
            return payment
        else:
            response = {
                "success": False
            }
            if j.get('description', None) is not None:
                response["message"] = j.get('description')
            if j.get('code', None) is not None:
                response["code"] = j.get('code')

            raise falcon.HTTPError(falcon.HTTP_422, response)


_payments = PaymentService()
