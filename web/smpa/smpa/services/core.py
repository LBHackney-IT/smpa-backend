# -*- coding: utf-8 -*-

"""
    services.core
    ~~~~~~~~~~~~~
    Core service.
"""

from typing import List, Any, Optional, Iterable  # NOQA

from sqlalchemy import inspect
from slugify import slugify

from .core import BaseModel
from q import db


class Service(object):
    """Core service object. Extend this to provide services to your models.
    """
    __model__ = BaseModel  # type: BaseModel

    @property
    def q(self):
        """
        Shorthand property for accessing the query property of the model.
        You can also override this on an individual service level, for instance
        if you need to implement soft-deletes on a specific service this could be
        overridden to return self.__model__.query.filter(deleted=True)

        Returns:
            [type]: [description]
        """
        return self.__model__.query

    def make_slug(
            self, instance: BaseModel,
            field: Optional[str] = None,
            fields: Optional[list[str]] = None) -> str:
        """
        Make a slug for ``instance`` using ``field`` as the input, or optionally ``fields``,
        useful for when you want to slug on two or more fields like firstname-lastname.

        Args:
            instance (Model): The model instance that we want a slug for
            field (str, optional): Defaults to None. The field to take the input from
            fields (str, optional): Defaults to None. For creating multi field slugs

        Raises:
            ValueError: If the supplied field(s) are None or empty strings

        Returns:
            str: The slug
        """
        if field is not None:
            text = str(getattr(instance, field))
            if text is None or text == '':
                raise ValueError('There was no string to make a slug from')
        elif fields is not None:
            parts = [str(getattr(instance, field)) for field in fields]
            text = '-'.join(parts)
            if text is None or text.replace('-', '') == '':
                raise ValueError('There was no string to make a slug from')

        concrete_slug = slugify(text, to_lower=True)
        slug = concrete_slug
        counter = 1
        while self.q.filter_by(slug=slug).first() is not None:
            slug = '{}-{}'.format(concrete_slug, counter)
            counter += 1
        return slug

    def count(self) -> int:
        """
        How many of these are there?

        Returns:
            int: The number of this services model according to self.q
        """
        return self.q.count()

    def from_form(self, form) -> BaseModel:
        """Like form.populate_obj but less error prone with with nullable=False fields.
        Use this to create a new model instance populated from a form.

        Args:
            form (wtforms.Form): The form object

        Returns:
            BaseModel: a new, saved model instance
        """
        obj = self.new()
        mapper = inspect(self.__model__)
        for column in mapper.attrs:
            if hasattr(form, column.key):
                d = getattr(form, column.key)
                if d is not None:
                    val = d.data
                    setattr(obj, column.key, val)

        return self.save(obj)

    def _isinstance(self, model: BaseModel, raise_error=True) -> bool:
        """Checks if the specified model instance matches the service's model.
        By default this method will raise a ``ValueError`` if the model is not the
        expected type.
        Args:
            model (BaseModel): the model instance to check
            raise_error (bool): flag to raise an error on a mismatch
        """
        rv = isinstance(model, self.__model__)
        if not rv and raise_error:
            raise ValueError(f'{model} is not of type {self.__model__}')
        return rv

    def _preprocess_params(self, kwargs:dict) -> dict:
        """Returns a preprocessed dictionary of parameters. Used by default
        before creating a new instance or updating an existing instance. Use this
        to do things like remove the csrf_token etc.

        Args:
            kwargs (dict): a dictionary of parameters
        """
        kwargs.pop('csrf_token', None)
        return kwargs

    def save(self, model: BaseModel) -> BaseModel:
        """Commits the model to the database and returns the model

        Args:
            model (BaseModel): the model instance you want to save
        """
        self._isinstance(model)
        db.session.add(model)
        db.session.commit()
        return model

    def all(self) -> Iterable[BaseModel]:
        """Returns a generator containing all instances of the service's model
        according to self.q

        Returns:
            Iterable[BaseModel]: the result set
        """
        return self.q.all()

    def get(self, id: int) -> Optional[BaseModel]:
        """Returns an instance of the service's model with the specified id.
        Returns ``None`` if an instance with the specified id does not exist.

        Args
            id: the instance id

        Returns:
            BaseModel (optiona): The model.
        """
        return self.q.get(id)

    def get_all(self, *ids: list) -> Iterable[BaseModel]:
        """Returns a list of instances of the service's model with the specified ids.

        Args:
            ids (list): instance ids

        Returns:
            Iterable[BaseModel]: the result set
        """
        return self.q.filter(self.__model__.id.in_(ids)).all()

    def find(self, **kwargs: dict) -> Iterable[BaseModel]:
        """Returns a query set of instances of the service's model filtered by the
        specified key word arguments.

        Args:
            kwargs (dict): filter parameters

        Returns:
            Iterable[BaseModel]: the result set
        """
        return self.q.filter_by(**kwargs)

    def find_all(self, **kwargs: dict) -> Iterable[BaseModel]:
        """Returns a list of instances of the service's model filtered by the
        specified key word arguments.

        Args:
            kwargs: filter parameters

        Returns:
            Iterable[BaseModel]: the result set
        """
        return self.find(**kwargs).all()

    def first_or_404(self, **kwargs: dict) -> BaseModel:
        """Returns the first instance of the service's model filtered by the
        specified key word arguments.

        Args:
            kwargs: filter parameters

        Returns:
            BaseModel (optional): An instance if found

        Raises:
            HTTP404
        """
        return self.q.filter_by(**kwargs).first_or_404()

    def first(self, **kwargs: dict) -> Optional[BaseModel]:
        """Returns the first instance found of the service's model filtered by
        the specified key word arguments.

        Args:
            kwargs (dict): filter parameters

        Returns:
            BaseModel (optional): The instance if it finds one
        """
        return self.find(**kwargs).first()

    def last(self, **kwargs: dict) -> Optional[BaseModel]:
        """Returns the last instance found of the service's model filtered by
        the specified key word arguments.

        Args:
            kwargs(dict): filter parameters

        Returns:
            BaseModel (otpional): An instance or None
        """
        return self.q.order_by(self.__model__.created_at.desc()).filter_by(**kwargs).first()

    def get_or_404(self, id: Any[int, uuid]) -> BaseModel:
        """Returns an instance of the service's model with the specified id or
        raises an 404 error if an instance with the specified id does not exist.

        Args:
            id (int, uuid): the instance id

        Returns:
            BaseModel: A model instance

        Raises:
            HTTP404 if the model is not found
        """
        return self.__model__.query.get_or_404(id)

    def new(self, **kwargs: dict) -> BaseModel:
        """Returns a new, unsaved instance of the service's model class.

        Args:
            kwargs (dict): instance parameters

        Returns:
            BaseModel: An _unsaved_ instance of this service's model
        """
        return self.__model__(**self._preprocess_params(kwargs))

    def create(self, **kwargs: dict) -> BaseModel:
        """Returns a new, saved instance of the service's model class.

        Args:
            kwargs (dict): instance parameters

        Returns:
            BaseModel: A new _saved_ instance of the service's model class
        """
        return self.save(self.new(**kwargs))

    def update(self, model, **kwargs: dict) -> BaseModel:
        """Returns an updated instance of the service's model class.

        Args:
            model (BaseModel): the model instance to update
            kwargs (dict): update parameters

        Returns:
            BaseModel: The updated, saved model instance
        """
        self._isinstance(model)
        for k, v in list(self._preprocess_params(kwargs).items()):
            setattr(model, k, v)
        self.save(model)
        return model

    def prepare(self, model: BaseModel, **kwargs: dict) -> BaseModel:
        """Like update, but doesn't save the model. Use this when you know
        you're going to do something else to it before saving.

        Args:
            model (BaseModel): the model to update
            kwargs (dict): update parameters

        Returns:
            BaseModel: The updated but not saved model instance
        """
        self._isinstance(model)
        for k, v in list(self._preprocess_params(kwargs).items()):
            setattr(model, k, v)
        # self.save(model)
        return model

    def delete(self, model: BaseModel) -> None:
        """Immediately deletes the specified model instance.

        Args:
            model (BaseModel): the model instance to delete
        """
        self._isinstance(model)
        db.session.delete(model)
        db.session.commit()
