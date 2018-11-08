
import functools

from molten import field, Include, Route, schema, Response
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

    _service: Optional[Service]

    def __init__(self, service: Optional[Service] = None) -> None:
        if service is not None:
            self.service = service()

        if hasattr(self, '_service'):
            if self._service is not None:
                self.service = self._service()

        if hasattr(self, 'service'):
            if self.service is None:
                raise ValueError('Cannot init a manager without a service')

    def index(self):
        """Return a list of this manager's resource type
        """
        console.info('BaseManager.index')
        return {}

    def create(self, resource: Any) -> BaseResource:
        """Create an instance of this manager's resource type.

        Args:
            resource (Any): The resource that we're creating

        Returns:
            BaseResource: A saved instance of this manager's resource
        """
        data = {}
        for key, value in resource.__dict__.items():
            if value is not None:
                data[key] = value
                instance = self.service.create(**data)

        resource.id = instance.id

        return resource

    def fetch(self, id: MyUUID) -> BaseResource:
        """Return a single instance of this manager's resource type with
        the specified ID.

        Args:
            id (MyUUID): UUID primary key ID of the resource requested

        Returns:
            BaseResource: An instance of the resource with the specified ID
        """
        console.info('BaseManager.fetch')
        return BaseResource()  #TODO

    def update(self, resource: BaseResource) -> BaseResource:
        """Update a resource

        Args:
            resource (BaseResource): The resource we're updating

        Returns:
            BaseResource: The updated resource.
        """
        console.info('BaseManager.update')
        return BaseResource()  #TODO

    def delete(self, id: MyUUID) -> bool:
        """Delete a resource.

        Args:
            id (MyUUID): The UUID primary key ID

        Returns:
            bool: True if delete was successful
        """
        console.info('BaseManager.delete')
        return True  #TODO


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
        x._manager = dct.get('manager')()
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

