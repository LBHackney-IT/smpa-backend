from molten import field, Include, Route
from typing import Optional, Any
from inspect import Parameter

from arrow.arrow import Arrow

from smpa.services.core import Service
from smpa.helpers.database import MyUUID


class BaseResource:
    id: Optional[MyUUID] = field(response_only=True)
    created_at: Optional[Arrow]
    updated_at: Optional[Arrow]


class BaseManager:

    def __init__(self, service: Service) -> None:
        self.service = service()

    def index(self):
        pass

    def create(self, resource: Any):
        data = {}
        for key, value in resource.__dict__.items():
            if value is not None:
                data[key] = value
                instance = self.service.create(**data)

        resource.id = instance.id

        return resource

    def fetch(self, id: MyUUID) -> BaseResource:
        pass

    def update(self, resource: BaseResource) -> BaseResource:
        pass

    def delete(self, id: MyUUID) -> bool:
        pass


class BaseComponent:
    is_cacheable: bool = True
    is_singleton: bool = True
    __manager__: BaseManager
    __service__: Service

    def can_handle_parameter(self, parameter: Parameter) -> bool:
        return parameter.annotation is self.__manager__

    def resolve(self) -> BaseManager:
        return self.__manager__(self.__service__)


class BaseHandler:

    __resource__: BaseResource
    __manager__: BaseManager
    __namespace__: str

    @classmethod
    def routes(cls):
        return Include(f"/{cls.__namespace__}", [
            Route("/", cls.index, method="GET"),
            Route("/", cls.create, method="POST"),
            Route("/{id}", cls.update, method="POST"),
            Route("/{id}", cls.fetch, method="GET"),
            Route("/{id}", cls.delete, method="DELETE"),
        ], namespace=cls.__namespace__)

    @classmethod
    def index(cls):
        manager = cls.__manager__(cls.__manager__.__service__)
        return manager.index()

    @classmethod
    def create(cls, resource: BaseResource) -> BaseResource:
        manager = cls._get_manager()
        return manager.create(resource)

    @classmethod
    def fetch(cls, id: MyUUID) -> BaseResource:
        manager = cls._get_manager()
        return manager.fetch(id)

    @classmethod
    def update(cls, resource: BaseResource) -> BaseResource:
        manager = cls._get_manager()
        return manager.update(resource)

    @classmethod
    def delete(cls, id: MyUUID) -> bool:
        manager = cls._get_manager()
        return manager.delete(id)

    @classmethod
    def _get_manager(cls):
        return cls.__manager__(cls.__manager__.__service__)
