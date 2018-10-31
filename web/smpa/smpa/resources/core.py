import functools
from molten import field, Include, Route, schema
from typing import Optional, Any, Type
from inspect import Parameter

from arrow.arrow import Arrow

from smpa.services.core import Service
from smpa.helpers.database import MyUUID
from smpa.helpers.console import console


class BaseResource:
    id: Optional[MyUUID] = field(response_only=True)
    created_at: Optional[Arrow]
    updated_at: Optional[Arrow]


@schema
class Todo2:
    id: Optional[int] = field(response_only=True)
    description: str
    status: str = field(choices=["todo", "done"], default="todo")


@schema
class Address2:
    id: Optional[MyUUID] = field(response_only=True)
    number: Optional[str]
    property_name: Optional[str]
    address_line_1: Optional[str]
    address_line_2: Optional[str]
    address_line_3: Optional[str]
    town_city: Optional[str]
    postcode: Optional[str]
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
    __resource__: BaseResource

    def can_handle_parameter(self, parameter: Parameter) -> bool:
        return parameter.annotation is self.__manager__

    def resolve(self) -> BaseManager:
        return self.__manager__(self.__service__)


class MetaHandler(type):

    _resource: BaseResource
    _manager: BaseManager
    _namespace: str

    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x._resource = dct.get('resource')
        x._manager = dct.get('manager')
        x._namespace = dct.get('namespace')
        return x

    def routes(cls):
        return Include(f"/{cls._namespace}", [
            Route("/", cls.index, method="GET"),
            Route("/", cls.create, method="POST"),
            Route("/{id}", cls.update, method="POST"),
            Route("/{id}", cls.fetch, method="GET"),
            Route("/{id}", cls.delete, method="DELETE"),
        ], namespace=cls._namespace)

    def index(cls):
        return cls._manager.index()

    def create(cls, resource: BaseResource) -> BaseResource:
        return cls._manager.create(resource)

    def fetch(cls, id: MyUUID) -> BaseResource:
        return cls._manager.fetch(id)

    def update(cls, resource: BaseResource) -> BaseResource:
        return cls._manager.update(resource)

    def delete(cls, id: MyUUID) -> bool:
        return cls._manager.delete(id)


def make_base_handler(resource_cls, manager_cls, namespace):

    class BaseHandler:

        @classmethod
        def routes(cls):
            return Include(f"/{namespace}", [
                Route("/", cls.index, method="GET"),
                Route("/", cls.create, method="POST"),
                Route("/{id}", cls.update, method="POST"),
                Route("/{id}", cls.fetch, method="GET"),
                Route("/{id}", cls.delete, method="DELETE"),
            ], namespace=namespace)

        @classmethod
        def index(cls):
            manager = cls._get_manager()
            return manager.index()

        @classmethod
        def create(cls, resource: Type[resource_cls]) -> Type[resource_cls]:
            manager = cls._get_manager()
            return manager.create(resource)

        @classmethod
        def fetch(cls, id: MyUUID) -> Type[resource_cls]:
            manager = cls._get_manager()
            return manager.fetch(id)

        @classmethod
        def update(cls, resource: Type[resource_cls]) -> Type[resource_cls]:
            manager = cls._get_manager()
            return manager.update(resource)

        @classmethod
        def delete(cls, id: MyUUID) -> bool:
            manager = cls._get_manager()
            return manager.delete(id)

        @classmethod
        def _get_manager(cls):
            return manager_cls(manager_cls.__service__)

    return BaseHandler


def handler(cls, resource_cls, manager_cls, namespace):

    class BaseHandler(cls):
        @classmethod
        def routes(cls):
            return Include(f"/{namespace}", [
                Route("/", cls.index, method="GET"),
                Route("/", cls.create, method="POST"),
                Route("/{id}", cls.update, method="POST"),
                Route("/{id}", cls.fetch, method="GET"),
                Route("/{id}", cls.delete, method="DELETE"),
            ], namespace=namespace)

        @classmethod
        def index(cls):
            manager = cls._get_manager()
            return manager.index()

        @classmethod
        def create(cls, resource: Type[resource_cls]) -> Type[resource_cls]:
            manager = cls._get_manager()
            return manager.create(resource)

        @classmethod
        def fetch(cls, id: MyUUID) -> Type[resource_cls]:
            manager = cls._get_manager()
            return manager.fetch(id)

        @classmethod
        def update(cls, resource: Type[resource_cls]) -> Type[resource_cls]:
            manager = cls._get_manager()
            return manager.update(resource)

        @classmethod
        def delete(cls, id: MyUUID) -> bool:
            manager = cls._get_manager()
            return manager.delete(id)

        @classmethod
        def _get_manager(cls):
            return manager_cls(manager_cls.__service__)

    return BaseHandler


def handler2(cls):

    class Wrapper(object):
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print('Getting the {} of {}'.format(name, self.wrapped))
            return getattr(self.wrapped, name)

    return Wrapper


class Handler:

    def __init__(self, resource_cls, manager_cls, namespace):
        self.resource_cls = resource_cls
        self.manager_cls = manager_cls
        self.namespace = namespace
        import ipdb; ipdb.set_trace()

    def __call__(self, *args):
        return self.func(*args)

        # @classmethod
        # def routes(cls):
        #     return Include(f"/{cls.namespace}", [
        #         Route("/", cls.index, method="GET"),
        #         Route("/", cls.create, method="POST"),
        #         Route("/{id}", cls.update, method="POST"),
        #         Route("/{id}", cls.fetch, method="GET"),
        #         Route("/{id}", cls.delete, method="DELETE"),
        #     ], namespace=cls.namespace)

        # @classmethod
        # def index(cls):
        #     manager = cls._get_manager()
        #     return manager.index()

        # @classmethod
        # def create(cls, resource: Type[resource_cls]) -> Type[resource_cls]:
        #     manager = cls._get_manager()
        #     return manager.create(resource)

        # @classmethod
        # def fetch(cls, id: MyUUID) -> Type[resource_cls]:
        #     manager = cls._get_manager()
        #     return manager.fetch(id)

        # @classmethod
        # def update(cls, resource: Type[resource_cls]) -> Type[resource_cls]:
        #     manager = cls._get_manager()
        #     return manager.update(resource)

        # @classmethod
        # def delete(cls, id: MyUUID) -> bool:
        #     manager = cls._get_manager()
        #     return manager.delete(id)

        # @classmethod
        # def _get_manager(cls):
        #     return cls.manager_cls(cls.manager_cls.__service__)

