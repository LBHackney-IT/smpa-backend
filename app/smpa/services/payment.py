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

    def check(self, id):
        """Checks the status of a payment on GovPay
        """
        from smpa.app import config
        govpay = GovPayClient(config.GOV_PAY_API_KEY)
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
        from smpa.app import config
        from .application import _applications
        govpay = GovPayClient(config.GOV_PAY_API_KEY)
        yyyy = arrow.now().year
        nnnn = 5000 + self.count()
        ref = f"{yyyy}/{nnnn}"
        amount = config.PAYMENT_AMOUNT
        description = config.PAYMENT_DESCRIPTION
        user = req.context['user']
        user.export()

        # Create the payment
        rv = govpay.create_payment(
            amount=amount, description=description, reference=ref, application_id=application_id
        )
        j = rv.json()
        if rv.status_code == 201:
            payment = self.new(json=j)
            payment.owner_id = str(user.id)
            payment.application_id = str(application_id)
            payment.next_url = j['_links']['next_url']['href']
            payment = _payments.save(payment)
            # Update the application with a status of submitted and a reference
            application = _applications.get(str(application_id))
            application.reference = ref
            application.status_id = "5aa415fa-9b25-4828-ac06-cb1ab9b000ea"
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
