from molten import field, schema
from typing import Optional, Type
from inspect import Parameter

from ..helpers.console import console

from .core import (
    BaseResource, BaseManager, BaseComponent, make_base_handler, MetaHandler, handler, Handler
)


@schema
class AreaUnit(BaseResource):
    name: str


@schema
class LinearUnit(BaseResource):
    name: str


@schema
class Area(BaseResource):
    value: float
    unit: Type[AreaUnit]


@schema
class Linear(BaseResource):
    value: float
    unit: Type[LinearUnit]
