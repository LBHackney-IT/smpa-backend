import json
import falcon

from typing import Optional

from .core import Resource
from ..services.material import (
    _material_options_roof, _material_options_wall, _material_options_window,
    _material_options_door, _base_materials, _materials_roof_other, _materials_wall_other,
    _materials_window_other, _materials_door_other, _other_materials, _external_building_materials
)


class MaterialOptionRoofResource(Resource):
    _service = _material_options_roof
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more MaterialOptionRoofs from the database
        tags:
            - MaterialOptionRoof
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more MaterialOptionRoofs
                schema:
                    type: array
                    items: MaterialOptionRoof
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update a MaterialOptionRoof in the database
        tags:
            - MaterialOptionRoof
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialOptionRoof
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated MaterialOptionRoof
                schema: MaterialOptionRoof
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
        summary: Add new MaterialOptionRoof to the database
        tags:
            - MaterialOptionRoof
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialOptionRoof
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: MaterialOptionRoof created successfully
                schema: MaterialOptionRoof
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class MaterialOptionWallResource(Resource):
    _service = _material_options_wall
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more MaterialOptionWalls from the database
        tags:
            - MaterialOptionWall
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more MaterialOptionWalls
                schema:
                    type: array
                    items: MaterialOptionWall
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update a MaterialOptionWall in the database
        tags:
            - MaterialOptionWall
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialOptionWall
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated MaterialOptionWall
                schema: MaterialOptionWall
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
        summary: Add new MaterialOptionWall to the database
        tags:
            - MaterialOptionWall
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialOptionWall
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: MaterialOptionWall created successfully
                schema: MaterialOptionWall
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class MaterialOptionWindowResource(Resource):
    _service = _material_options_window
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more MaterialOptionWindows from the database
        tags:
            - MaterialOptionWindow
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more MaterialOptionWindows
                schema:
                    type: array
                    items: MaterialOptionWindow
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update a MaterialOptionWindow in the database
        tags:
            - MaterialOptionWindow
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialOptionWindow
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated MaterialOptionWindow
                schema: MaterialOptionWindow
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
        summary: Add new MaterialOptionWindow to the database
        tags:
            - MaterialOptionWindow
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialOptionWindow
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: MaterialOptionWindow created successfully
                schema: MaterialOptionWindow
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class MaterialOptionDoorResource(Resource):
    _service = _material_options_door
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one or more MaterialOptionDoors from the database
        tags:
            - MaterialOptionDoor
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: One or more MaterialOptionDoors
                schema:
                    type: array
                    items: MaterialOptionDoor
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update a MaterialOptionDoor in the database
        tags:
            - MaterialOptionDoor
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialOptionDoor
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated MaterialOptionDoor
                schema: MaterialOptionDoor
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
        summary: Add new MaterialOptionDoor to the database
        tags:
            - MaterialOptionDoor
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialOptionDoor
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: MaterialOptionDoor created successfully
                schema: MaterialOptionDoor
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)
