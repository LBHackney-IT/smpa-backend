import falcon

from typing import Optional

from ..schemas.core import CoreListSchema, CoreGetSchema  # NOQA
from .core import Resource, ListResource
from ..services.work import (
    _works_locations, _basement_works_types, _roof_works_types, _border_works_types,
    _access_works_scopes, _access_works_types, _parking_works_scopes, _equipment_works_types,
    _equipment_works_conservation_types, _gates_fences_walls_types
)


class WorksLocationPost(ListResource):
    _service = _works_locations
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all WorksLocations from the DB
        tags:
            - WorksLocation
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All WorksLocations
                schema:
                    type: array
                    items: WorksLocation
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new WorksLocation to the database
        tags:
            - WorksLocation
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: WorksLocation
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: WorksLocation created successfully
                schema: WorksLocation
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class WorksLocationPatch(Resource):
    _service = _works_locations
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one WorksLocation from the DB
        tags:
            - WorksLocation
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested WorksLocation
                schema: WorksLocation
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an WorksLocation in the database
        tags:
            - WorksLocation
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: WorksLocation
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated WorksLocation
                schema: WorksLocation
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class BasementWorksTypePost(ListResource):
    _service = _basement_works_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all BasementWorksTypes from the DB
        tags:
            - BasementWorksType
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All BasementWorksTypes
                schema:
                    type: array
                    items: BasementWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new BasementWorksType to the database
        tags:
            - BasementWorksType
        parameters:
            - in: body
              schema: BasementWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: BasementWorksType created successfully
                schema: BasementWorksType
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class BasementWorksTypePatch(Resource):
    _service = _basement_works_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one BasementWorksType from the database
        tags:
            - BasementWorksType
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One BasementWorksType
                schema: BasementWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an BasementWorksType in the database
        tags:
            - BasementWorksType
        parameters:
            - in: body
              schema: BasementWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated BasementWorksType
                schema: BasementWorksType
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class RoofWorksTypePost(ListResource):
    _service = _roof_works_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all RoofWorksTypes from the DB
        tags:
            - RoofWorksType
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All RoofWorksTypes
                schema:
                    type: array
                    items: RoofWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new RoofWorksType to the database
        tags:
            - RoofWorksType
        parameters:
            - in: body
              schema: RoofWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: RoofWorksType created successfully
                schema: RoofWorksType
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class RoofWorksTypePatch(Resource):
    _service = _roof_works_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one RoofWorksType from the database
        tags:
            - RoofWorksType
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One RoofWorksType
                schema: RoofWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an RoofWorksType in the database
        tags:
            - RoofWorksType
        parameters:
            - in: body
              schema: RoofWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated RoofWorksType
                schema: RoofWorksType
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class BorderWorksTypePost(ListResource):
    _service = _border_works_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all BorderWorksTypes from the DB
        tags:
            - BorderWorksType
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All BorderWorksTypes
                schema:
                    type: array
                    items: BorderWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new BorderWorksType to the database
        tags:
            - BorderWorksType
        parameters:
            - in: body
              schema: BorderWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: BorderWorksType created successfully
                schema: BorderWorksType
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class BorderWorksTypePatch(Resource):
    _service = _border_works_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one BorderWorksType from the database
        tags:
            - BorderWorksType
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One BorderWorksType
                schema: BorderWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an BorderWorksType in the database
        tags:
            - BorderWorksType
        parameters:
            - in: body
              schema: BorderWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated BorderWorksType
                schema: BorderWorksType
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class AccessWorksScopePost(ListResource):
    _service = _access_works_scopes
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all AccessWorksScopes from the DB
        tags:
            - AccessWorksScope
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All AccessWorksScopes
                schema:
                    type: array
                    items: AccessWorksScope
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new AccessWorksScope to the database
        tags:
            - AccessWorksScope
        parameters:
            - in: body
              schema: AccessWorksScope
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: AccessWorksScope created successfully
                schema: AccessWorksScope
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class AccessWorksScopePatch(Resource):
    _service = _access_works_scopes
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one AccessWorksScope from the database
        tags:
            - AccessWorksScope
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One AccessWorksScope
                schema: AccessWorksScope
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an AccessWorksScope in the database
        tags:
            - AccessWorksScope
        parameters:
            - in: body
              schema: AccessWorksScope
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated AccessWorksScope
                schema: AccessWorksScope
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class AccessWorksTypePost(ListResource):
    _service = _access_works_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all AccessWorksTypes from the DB
        tags:
            - AccessWorksType
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All AccessWorksTypes
                schema:
                    type: array
                    items: AccessWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new AccessWorksType to the database
        tags:
            - AccessWorksType
        parameters:
            - in: body
              schema: AccessWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: AccessWorksType created successfully
                schema: AccessWorksType
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class AccessWorksTypePatch(Resource):
    _service = _access_works_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one AccessWorksType from the database
        tags:
            - AccessWorksType
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One AccessWorksType
                schema: AccessWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an AccessWorksType in the database
        tags:
            - AccessWorksType
        parameters:
            - in: body
              schema: AccessWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated AccessWorksType
                schema: AccessWorksType
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class ParkingWorksScopePost(ListResource):
    _service = _parking_works_scopes
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all ParkingWorksScopes from the DB
        tags:
            - ParkingWorksScope
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All ParkingWorksScopes
                schema:
                    type: array
                    items: ParkingWorksScope
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new ParkingWorksScope to the database
        tags:
            - ParkingWorksScope
        parameters:
            - in: body
              schema: ParkingWorksScope
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: ParkingWorksScope created successfully
                schema: ParkingWorksScope
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class ParkingWorksScopePatch(Resource):
    _service = _parking_works_scopes
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one ParkingWorksScope from the database
        tags:
            - ParkingWorksScope
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One ParkingWorksScope
                schema: ParkingWorksScope
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an ParkingWorksScope in the database
        tags:
            - ParkingWorksScope
        parameters:
            - in: body
              schema: ParkingWorksScope
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated ParkingWorksScope
                schema: ParkingWorksScope
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class EquipmentWorksTypePost(ListResource):
    _service = _equipment_works_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all EquipmentWorksTypes from the DB
        tags:
            - EquipmentWorksType
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All EquipmentWorksTypes
                schema:
                    type: array
                    items: EquipmentWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new EquipmentWorksType to the database
        tags:
            - EquipmentWorksType
        parameters:
            - in: body
              schema: EquipmentWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: EquipmentWorksType created successfully
                schema: EquipmentWorksType
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class EquipmentWorksTypePatch(Resource):
    _service = _equipment_works_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one EquipmentWorksType from the database
        tags:
            - EquipmentWorksType
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One EquipmentWorksType
                schema: EquipmentWorksType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an EquipmentWorksType in the database
        tags:
            - EquipmentWorksType
        parameters:
            - in: body
              schema: EquipmentWorksType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated EquipmentWorksType
                schema: EquipmentWorksType
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class EquipmentWorksConservationTypePost(ListResource):
    _service = _equipment_works_conservation_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all EquipmentWorksConservationTypes from the DB
        tags:
            - EquipmentWorksConservationType
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All EquipmentWorksConservationTypes
                schema:
                    type: array
                    items: EquipmentWorksConservationType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new EquipmentWorksConservationType to the database
        tags:
            - EquipmentWorksConservationType
        parameters:
            - in: body
              schema: EquipmentWorksConservationType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: EquipmentWorksConservationType created successfully
                schema: EquipmentWorksConservationType
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class EquipmentWorksConservationTypePatch(Resource):
    _service = _equipment_works_conservation_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one EquipmentWorksConservationType from the database
        tags:
            - EquipmentWorksConservationType
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One EquipmentWorksConservationType
                schema: EquipmentWorksConservationType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an EquipmentWorksConservationType in the database
        tags:
            - EquipmentWorksConservationType
        parameters:
            - in: body
              schema: EquipmentWorksConservationType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated EquipmentWorksConservationType
                schema: EquipmentWorksConservationType
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class GatesFencesWallsTypePost(ListResource):
    _service = _gates_fences_walls_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all GatesFencesWallsType from the DB
        tags:
            - GatesFencesWallsType
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All GatesFencesWallsTypes
                schema:
                    type: array
                    items: GatesFencesWallsType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new GatesFencesWallsType to the database
        tags:
            - GatesFencesWallsType
        parameters:
            - in: body
              schema: GatesFencesWallsType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: GatesFencesWallsType created successfully
                schema: GatesFencesWallsType
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class GatesFencesWallsTypePatch(Resource):
    _service = _gates_fences_walls_types
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one GatesFencesWallsType from the database
        tags:
            - GatesFencesWallsType
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One GatesFencesWallsType
                schema: GatesFencesWallsType
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an GatesFencesWallsType in the database
        tags:
            - GatesFencesWallsType
        parameters:
            - in: body
              schema: GatesFencesWallsType
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated GatesFencesWallsType
                schema: GatesFencesWallsType
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)
