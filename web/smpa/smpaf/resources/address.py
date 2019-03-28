import json
import falcon

from .core import Resource
from ..services.address import (
    _addresses, _site_addresses, _bs7666_addresses, _external_addresses, _international_addresses
)


class AddressResource(Resource):
    _service = _addresses

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more Addresses from the database
        tags:
            - Address
        parameters:
            - in: id
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more Addresses
                schema:
                    type: array
                    items: Address
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an Address in the database
        tags:
            - Address
        parameters:
            - in: json
              schema: Address
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated Address
                schema: Address
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add a new Address to the database
        tags:
            - Address
        parameters:
            - in: json
              schema: Address
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: Address created successfully
                schema: Address
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)



class SiteAddressResource(Resource):
    _service = _site_addresses

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more SiteAddresses from the database
        tags:
            - SiteAddress
        parameters:
            - in: id
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more SiteAddresses
                schema:
                    type: array
                    items: SiteAddress
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update a SiteAddress in the database
        tags:
            - SiteAddress
        parameters:
            - in: json
              schema: SiteAddress
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated SiteAddress
                schema: SiteAddress
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new SiteAddress to the database
        tags:
            - SiteAddress
        parameters:
            - in: json
              schema: SiteAddress
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: SiteAddress created successfully
                schema: SiteAddress
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class BS7666AddressResource(Resource):
    _service = _bs7666_addresses

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more BS7666Addresses from the database
        tags:
            - BS7666Address
        parameters:
            - in: id
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more BS7666Addresses
                    type: array
                    items: BS7666Address
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update a BS7666Address in the database
        tags:
            - BS7666Address
        parameters:
            - in: json
              schema: BS7666Address
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated BS7666Address
                schema: BS7666Address
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new BS7666Address to the database
        tags:
            - BS7666Address
        parameters:
            - in: json
              schema: BS7666Address
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: BS7666Address created successfully
                schema: BS7666Address
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class ExternalAddressResource(Resource):
    _service = _external_addresses

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more ExternalAddresses from the database
        tags:
            - ExternalAddress
        parameters:
            - in: id
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more ExternalAddresses
                schema:
                    type: array
                    items: ExternalAddress
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an ExternalAddress in the database
        tags:
            - ExternalAddress
        parameters:
            - in: json
              schema: ExternalAddress
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated ExternalAddress
                schema: ExternalAddress
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new ExternalAddress to the database
        tags:
            - ExternalAddress
        parameters:
            - in: json
              schema: ExternalAddress
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: ExternalAddress created successfully
                schema: ExternalAddress
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class InternationalAddressResource(Resource):
    _service = _international_addresses

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more InternationalAddresses from the database
        tags:
            - InternationalAddress
        parameters:
            - in: id
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more InternationalAddresses
                schema:
                    type: array
                    items: InternationalAddress
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an InternationalAddress in the database
        tags:
            - InternationalAddress
        parameters:
            - in: json
              schema: InternationalAddress
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated InternationalAddress
                schema: InternationalAddress
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new InternationalAddress to the database
        tags:
            - InternationalAddress
        parameters:
            - in: json
              schema: InternationalAddress
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: InternationalAddress created successfully
                schema: InternationalAddress
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)

