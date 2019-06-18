import json
import falcon

from typing import Optional

from .core import Resource, ListResource
from ..services.material import (
    _material_options_roof, _material_options_wall, _material_options_window,
    _material_options_door, _base_materials, _materials_roof, _materials_wall,
    _materials_window, _materials_door, _other_materials, _external_building_materials
)
"""
MaterialOptionRoof
MaterialOptionWall
MaterialOptionWindow
MaterialOptionDoor

MaterialRoof
MaterialWall
MaterialWindow
MaterialDoor

OtherMaterial
ExternalBuildingMaterial
"""


class MaterialOptionRoofPost(ListResource):
    _service = _material_options_roof
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all MaterialOptionRoofs from the DB
        tags:
            - MaterialOptionRoof
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All MaterialOptionRoofs
                schema:
                    type: array
                    items: MaterialOptionRoof
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

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


class MaterialOptionRoofPatch(Resource):
    _service = _material_options_roof
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one MaterialOptionRoof from the DB
        tags:
            - MaterialOptionRoof
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested MaterialOptionRoof
                schema: MaterialOptionRoof
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an MaterialOptionRoof in the database
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


class MaterialOptionWallPost(ListResource):
    _service = _material_options_wall
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all MaterialOptionWalls from the DB
        tags:
            - MaterialOptionWall
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All MaterialOptionWalls
                schema:
                    type: array
                    items: MaterialOptionWall
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

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


class MaterialOptionWallPatch(Resource):
    _service = _material_options_wall
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one MaterialOptionWall from the DB
        tags:
            - MaterialOptionWall
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested MaterialOptionWall
                schema: MaterialOptionWall
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an MaterialOptionWall in the database
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


class MaterialOptionWindowPost(ListResource):
    _service = _material_options_window
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all MaterialOptionWindows from the DB
        tags:
            - MaterialOptionWindow
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All MaterialOptionWindows
                schema:
                    type: array
                    items: MaterialOptionWindow
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

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


class MaterialOptionWindowPatch(Resource):
    _service = _material_options_window
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one MaterialOptionWindow from the DB
        tags:
            - MaterialOptionWindow
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested MaterialOptionWindow
                schema: MaterialOptionWindow
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an MaterialOptionWindow in the database
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


class MaterialOptionDoorPost(ListResource):
    _service = _material_options_door
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all MaterialOptionDoors from the DB
        tags:
            - MaterialOptionDoor
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All MaterialOptionDoors
                schema:
                    type: array
                    items: MaterialOptionDoor
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

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


class MaterialOptionDoorPatch(Resource):
    _service = _material_options_door
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one MaterialOptionDoor from the DB
        tags:
            - MaterialOptionDoor
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested MaterialOptionDoor
                schema: MaterialOptionDoor
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an MaterialOptionDoor in the database
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


class MaterialRoofPost(ListResource):
    _service = _materials_roof
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all MaterialRoofs from the DB
        tags:
            - MaterialRoof
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All MaterialRoofs
                schema:
                    type: array
                    items: MaterialRoof
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new MaterialRoof to the database
        tags:
            - MaterialRoof
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialRoof
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: MaterialRoof created successfully
                schema: MaterialRoof
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class MaterialRoofPatch(Resource):
    _service = _materials_roof
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one MaterialRoof from the DB
        tags:
            - MaterialRoof
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested MaterialRoof
                schema: MaterialRoof
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an MaterialRoof in the database
        tags:
            - MaterialRoof
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialRoof
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated MaterialRoof
                schema: MaterialRoof
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class MaterialWallPost(ListResource):
    _service = _materials_wall
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all MaterialWalls from the DB
        tags:
            - MaterialWall
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All MaterialWalls
                schema:
                    type: array
                    items: MaterialWall
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new MaterialWall to the database
        tags:
            - MaterialWall
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialWall
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: MaterialWall created successfully
                schema: MaterialWall
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class MaterialWallPatch(Resource):
    _service = _materials_wall
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one MaterialWall from the DB
        tags:
            - MaterialWall
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested MaterialWall
                schema: MaterialWall
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an MaterialWall in the database
        tags:
            - MaterialWall
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialWall
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated MaterialWall
                schema: MaterialWall
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class MaterialWindowPost(ListResource):
    _service = _materials_window
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all MaterialWindows from the DB
        tags:
            - MaterialWindow
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All MaterialWindows
                schema:
                    type: array
                    items: MaterialWindow
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new MaterialWindow to the database
        tags:
            - MaterialWindow
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialWindow
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: MaterialWindow created successfully
                schema: MaterialWindow
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class MaterialWindowPatch(Resource):
    _service = _materials_window
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one MaterialWindow from the DB
        tags:
            - MaterialWindow
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested MaterialWindow
                schema: MaterialWindow
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an MaterialWindow in the database
        tags:
            - MaterialWindow
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialWindow
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated MaterialWindow
                schema: MaterialWindow
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)


class MaterialDoorPost(ListResource):
    _service = _materials_door
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Get all MaterialDoors from the DB
        tags:
            - MaterialDoor
        parameters:
            - in: query
              schema: CoreListSchema
        produces:
            - application/json
        responses:
            200:
                description: All MaterialDoors
                schema:
                    type: array
                    items: MaterialDoor
            401:
                description: Unauthorized
        """
        super().on_get(req, resp)

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """
        ---
        summary: Add new MaterialDoor to the database
        tags:
            - MaterialDoor
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialDoor
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            201:
                description: MaterialDoor created successfully
                schema: MaterialDoor
            401:
                description: Unauthorized
            422:
                description: Input body formatting issue
        """
        super().on_post(req, resp)


class MaterialDoorPatch(Resource):
    _service = _materials_door
    auth = {
        'exempt_methods': ['OPTIONS', 'GET']
    }

    def on_get(self, req: falcon.Request, resp: falcon.Response, id: Optional[str] = None) -> None:
        """
        ---
        summary: Get one MaterialDoor from the DB
        tags:
            - MaterialDoor
        parameters:
            - in: path
              schema: CoreGetSchema
        produces:
            - application/json
        responses:
            200:
                description: The requested MaterialDoor
                schema: MaterialDoor
            401:
                description: Unauthorized
        """
        super().on_get(req, resp, id)

    def on_patch(self, req: falcon.Request, resp: falcon.Response, id: str) -> None:
        """
        ---
        summary: Update an MaterialDoor in the database
        tags:
            - MaterialDoor
        parameters:
            - in: path
              schema: CoreGetSchema
            - in: body
              schema: MaterialDoor
        consumes:
            - application/json
        produces:
            - application/json
        responses:
            200:
                description: Returns updated MaterialDoor
                schema: MaterialDoor
            401:
                description: Unauthorized
            404:
                description: Object does not exist
            422:
                description: Input body formatting issue
        """
        super().on_patch(req, resp, id)
