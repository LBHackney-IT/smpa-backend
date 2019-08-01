# -*- coding: utf-8 -*-

"""
    smpa.openapi.schematics.common
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Schematics plugin for apispec based on the bundled Marshmallow
    plugin.

"""

import copy
import warnings
from collections import namedtuple, OrderedDict
from typing import Union

from smpa.models.core import BaseModel
from smpa.db.documentdb.registry import RegistryError, model_registry

# import marshmallow


MODIFIERS = ["only", "exclude", "load_only", "dump_only", "partial"]


def resolve_schema_instance(schema: Union[BaseModel, str]) -> BaseModel:
    """Fetches an instance of the schematics model ``schema``

    Args:
        schema (BaseModel, str): Model or name of the model you want an instance of

    Returns:
        BaseModel: Instance

    Raises:
        ValueError: If the model is not found or registered.
    """
    from smpa.schemas.core import CoreGetSchema, CoreListSchema
    from smpa.schemas.auth import LoginSchema

    if schema == 'CoreListSchema':
        return CoreListSchema
    elif schema == 'CoreGetSchema':
        return CoreGetSchema
    elif schema == 'LoginSchema':
        return LoginSchema

    if isinstance(schema, type) and issubclass(schema, BaseModel):
        return schema()
    if isinstance(schema, BaseModel):
        return schema
    try:
        return model_registry.get_class(schema)()
    except RegistryError:
        raise ValueError(
            "{!r} is not a BaseModel subclass or instance and has not"
            " been registered in the model registry.".format(schema)
        )


def resolve_schema_cls(schema: Union[BaseModel, str]) -> BaseModel:
    """Fetches the class of the schematics model ``schema``

    Args:
        schema (BaseModel, str): Model or name of the model you want an instance of

    Returns:
        BaseModel: BaseModel class, not an instance of

    Raises:
        ValueError: If the model is not found or registered.
    """

    if isinstance(schema, type) and issubclass(schema, BaseModel):
        return schema
    if isinstance(schema, BaseModel):
        return type(schema)
    try:
        return model_registry.get_class(schema)
    except RegistryError:
        raise ValueError(
            "{!r} is not a BaseModel subclass or instance and has not"
            " been registered in the model registry.".format(schema)
        )


def get_fields(schema: BaseModel, exclude_dump_only: bool = False) -> dict:
    """Return fields from schema

    :param Schema schema: A marshmallow Schema instance or a class object
    :param bool exclude_dump_only: whether to filter fields in Meta.dump_only
    :rtype: dict, of field name field object pairs

    Args:
        schema (BaseModel): The model you want the fields for
        exclude_dump_only (bool, optional): @TODO

    Returns:
        dict: Dict of field name field object pairs

    Raises:
        ValueError: If the model has no fields.
    """
    if hasattr(schema, "fields"):
        fields = schema.fields
    elif hasattr(schema, "_declared_fields"):
        fields = copy.deepcopy(schema._declared_fields)
    else:
        raise ValueError(
            "{!r} doesn't have either `fields` or `_declared_fields`.".format(schema)
        )
    Meta = getattr(schema, "Meta", None)
    return filter_excluded_fields(fields, Meta, exclude_dump_only)


def filter_excluded_fields(fields, Meta, exclude_dump_only):
    """Filter fields that should be ignored in the OpenAPI spec

    :param dict fields: A dictionary of of fields name field object pairs
    :param Meta: the schema's Meta class
    :param bool exclude_dump_only: whether to filter fields in Meta.dump_only
    """
    exclude = getattr(Meta, "exclude", [])
    if exclude_dump_only:
        exclude += getattr(Meta, "dump_only", [])

    filtered_fields = OrderedDict(
        (key, value) for key, value in fields.items() if key not in exclude
    )

    return filtered_fields


def make_schema_key(schema):
    """Creates a schema key which is used to check for duplicates in the refs."""
    # @TODO make this use schematics modifiers
    if not isinstance(schema, BaseModel):
        raise TypeError("can only make a schema key based on a BaseModel instance.")
    modifiers = []
    for modifier in MODIFIERS:
        if hasattr(schema, modifier):
            attribute = getattr(schema, modifier)
            try:
                hash(attribute)
            except TypeError:
                attribute = tuple(attribute)
            modifiers.append(attribute)


        else:
            modifiers.append((modifier, None))

    return SchemaKey(schema.__class__, *modifiers)


SchemaKey = namedtuple("SchemaKey", ["SchemaClass"] + MODIFIERS)


def get_unique_schema_name(components, name, counter=0):
    """Function to generate a unique name based on the provided name and names
    already in the spec.  Will append a number to the name to make it unique if
    the name is already in the spec.

    :param Components components: instance of the components of the spec
    :param string name: the name to use as a basis for the unique name
    :param int counter: the counter of the number of recursions
    :return: the unique name
    """
    if name not in components._schemas:
        return name
    if not counter:  # first time through recursion
        warnings.warn(
            "Multiple schemas resolved to the name {}. The name has been modified. "
            "Either manually add each of the schemas with a different name or "
            "provide a custom schema_name_resolver.".format(name),
            UserWarning,
        )
    else:  # subsequent recursions
        name = name[: -len(str(counter))]
    counter += 1
    return get_unique_schema_name(components, name + str(counter), counter)
