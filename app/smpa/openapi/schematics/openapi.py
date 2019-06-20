# -*- coding: utf-8 -*-
"""Utilities for generating OpenAPI Specification (fka Swagger) entities from
marshmallow :class:`Schemas <marshmallow.Schema>` and :class:`Fields <marshmallow.fields.Field>`.

.. warning::

    This module is treated as private API.
    Users should not need to use this module directly.
"""
from __future__ import absolute_import, unicode_literals
import arrow
import datetime
import operator
import functools
from collections import OrderedDict
from typing import Any, Union, Optional

from schematics import types
from schematics.models import Model
from schematics.undefined import UndefinedType

import marshmallow
from marshmallow.utils import is_collection
from marshmallow.compat import iteritems
from marshmallow.orderedset import OrderedSet

from apispec.compat import RegexType
from apispec.utils import OpenAPIVersion, build_reference
from .common import (
    resolve_schema_cls,
    get_fields,
    make_schema_key,
    resolve_schema_instance,
    get_unique_schema_name,
)
from apispec.exceptions import APISpecError

from smpa.helpers.console import console


# Schematics field => (JSON Schema type, format)
DEFAULT_FIELD_MAPPING = {
    types.IntType: ("integer", "int32"),
    types.NumberType: ("number", None),
    types.FloatType: ("number", "float"),
    types.DecimalType: ("number", None),
    types.StringType: ("string", None),
    types.BooleanType: ("boolean", None),
    types.UUIDType: ("string", "uuid"),
    types.DateTimeType: ("string", "date-time"),
    types.DateType: ("string", "date"),
    types.TimestampType: ("string", None),
    types.EmailType: ("string", "email"),
    # types.URL: ("string", "url"),  # Not in Schematics
    types.DictType: ("object", None),
    types.ListType: ("array", None),
    types.BaseType: ("string", None),
}


__location_map__ = {
    "query": "query",
    "querystring": "query",
    "json": "body",
    "headers": "header",
    "cookies": "cookie",
    "form": "formData",
    "files": "formData",
}


# Properties that may be defined in a field's metadata that will be added to the output
# of field2property
# https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#schemaObject
_VALID_PROPERTIES = {
    "format",
    "title",
    "description",
    "default",
    "multipleOf",
    "maximum",
    "exclusiveMaximum",
    "minimum",
    "exclusiveMinimum",
    "maxLength",
    "minLength",
    "pattern",
    "maxItems",
    "minItems",
    "uniqueItems",
    "maxProperties",
    "minProperties",
    "required",
    "enum",
    "type",
    "items",
    "allOf",
    "properties",
    "additionalProperties",
    "readOnly",
    "xml",
    "externalDocs",
    "example",
}

_VALID_PREFIX = "x-"


class OpenAPIConverter(object):
    """Converter generating OpenAPI specification from Marshmallow schemas and fields

    :param str|OpenAPIVersion openapi_version: The OpenAPI version to use.
        Should be in the form '2.x' or '3.x.x' to comply with the OpenAPI standard.
    """

    def __init__(self, openapi_version, schema_name_resolver, spec):
        self.openapi_version = OpenAPIVersion(openapi_version)
        self.schema_name_resolver = schema_name_resolver
        self.spec = spec
        # Schema references
        self.refs = {}
        #  Field mappings
        self.field_mapping = DEFAULT_FIELD_MAPPING

    @staticmethod
    def _observed_name(field, name):
        """Adjust field name to reflect `dump_to` and `load_from` attributes.

        :param Field field: A marshmallow field.
        :param str name: Field name
        :rtype: str

        @TODO re-write this to use the serialize method of a BaseModel maybe?
        """
        # if MARSHMALLOW_VERSION_INFO[0] < 3:
        #     # use getattr in case we're running against older versions of marshmallow.
        #     dump_to = getattr(field, "dump_to", None)
        #     load_from = getattr(field, "load_from", None)
        #     return dump_to or load_from or name
        # return field.data_key or name
        return name

    def map_to_openapi_type(self, *args):
        """Decorator to set mapping for custom fields.

        ``*args`` can be:

        - a pair of the form ``(type, format)``
        - a core marshmallow field type (in which case we reuse that type's mapping)
        """
        if len(args) == 1 and args[0] in self.field_mapping:
            openapi_type_field = self.field_mapping[args[0]]
        elif len(args) == 2:
            openapi_type_field = args
        else:
            raise TypeError("Pass core Schematics type or (type, fmt) pair.")

        def inner(field_type):
            self.field_mapping[field_type] = openapi_type_field
            return field_type

        return inner

    def field2type_and_format(self, field: types.BaseType) -> dict:
        """Return the dictionary of OpenAPI type and format based on the field
        type

        Args:
            field (fields.BaseType): Description

        Returns:
            dict: A dict mapping the field type
        """
        type_, fmt = self.field_mapping.get(type(field), ("string", None))

        ret = {"type": type_}

        if fmt:
            ret["format"] = fmt

        return ret

    def field2default(self, field: types.BaseType):
        """Return the dictionary containing the field's default value

        Args:
            field (types.BaseType): The field we're looking for a default value on

        Returns:
            dict: ie: {'default': False}

        """
        datetypes = (
            types.DateTimeType,
            types.DateType,
            datetime.datetime
        )
        ret: dict = {}
        if hasattr(field, 'default') and field.default is not None:
            if isinstance(field.default, marshmallow.utils._Missing):
                return ret
            if not isinstance(field.default, UndefinedType):
                if isinstance(field.default, datetypes):
                    try:
                        ret["default"] = arrow.get(field.default).isoformat()
                    except Exception as e:
                        console.warn(e)
                        ret["default"] = ""
                else:
                    ret["default"] = field.default

        return ret

    def field2choices(self, field, **kwargs):
        """Return the dictionary of OpenAPI field attributes for valid choices definition

        :param Field field: A marshmallow field.
        :rtype: dict

        @TODO Work out if we're going to need this at all for Schematics.
        """
        attributes = {}
        vals = []

        if hasattr(field, 'validators'):
            vals = field.validators

        comparable = [
            validator.comparable
            for validator in vals
            if hasattr(validator, "comparable")
        ]
        if comparable:
            attributes["enum"] = comparable
        else:
            choices = [
                OrderedSet(validator.choices)
                for validator in vals
                if hasattr(validator, "choices")
            ]
            if choices:
                attributes["enum"] = list(functools.reduce(operator.and_, choices))

        return attributes

    # def field2read_only(self, field, **kwargs):
    #     """Return the dictionary of OpenAPI field attributes for a dump_only field.

    #     :param Field field: A marshmallow field.
    #     :rtype: dict
    #     @TODO Work out if we're going to need this at all for Schematics.
    #     """
    #     attributes = {}
    #     if field.dump_only:
    #         attributes["readOnly"] = True
    #     return attributes

    # def field2write_only(self, field, **kwargs):
    #     """Return the dictionary of OpenAPI field attributes for a load_only field.

    #     :param Field field: A marshmallow field.
    #     :rtype: dict
    #     @TODO Work out if we're going to need this at all for Schematics.
    #     """
    #     attributes = {}
    #     if field.load_only and self.openapi_version.major >= 3:
    #         attributes["writeOnly"] = True
    #     return attributes

    def field2nullable(self, field: types.BaseType, **kwargs: dict) -> dict:
        """Return the dictionary of OpenAPI field attributes for a nullable field.

        Args:
            field (types.BaseType): The field
            **kwargs (dict): Any extra kwargs for some reason

        Returns:
            dict: ie: {'nullable': False}
        """
        attributes = {}
        required = False
        if hasattr(field, 'required'):
            required = field.required

        if not required:
            attributes[
                "x-nullable" if self.openapi_version.major < 3 else "nullable"
            ] = True
        return attributes

    def field2range(self, field, **kwargs):
        """Return the dictionary of OpenAPI field attributes for a set of
        :class:`Range <marshmallow.validators.Range>` validators.

        :param Field field: A marshmallow field.
        :rtype: dict
        # @NOTE: Schematics has no Range validator and we don't use a custom one
        """
        validators = [
            validator
            for validator in field.validators
            if (
                hasattr(validator, "min")
                and hasattr(validator, "max")
                and not hasattr(validator, "equal")
            )
        ]

        attributes = {}
        for validator in validators:
            if validator.min is not None:
                if hasattr(attributes, "minimum"):
                    attributes["minimum"] = max(attributes["minimum"], validator.min)
                else:
                    attributes["minimum"] = validator.min
            if validator.max is not None:
                if hasattr(attributes, "maximum"):
                    attributes["maximum"] = min(attributes["maximum"], validator.max)
                else:
                    attributes["maximum"] = validator.max
        return attributes

    def field2length(self, field: types.BaseType, **kwargs) -> dict:
        """Return the dictionary of OpenAPI field attributes for min and max length

        {'minLength': 6, 'maxLength': 36}

        :param Field field: A marshmallow field.
        :rtype: dict

        Args:
            field (types.BaseType): the field
            **kwargs: Any kwargs

        Returns:
            dict: ie: {'minLength': 6, 'maxLength': 36}
        """
        attributes = {}

        is_array = isinstance(field, types.ListType)

        min_attr = "minItems" if is_array else "minLength"
        max_attr = "maxItems" if is_array else "maxLength"

        if hasattr(field, 'max_length') and field.max_length is not None:
            attributes[max_attr] = field.max_length

        if hasattr(field, 'min_length') and field.min_length is not None:
            attributes[min_attr] = field.min_length

        return attributes

    # def field2pattern(self, field, **kwargs):
    #     """Return the dictionary of OpenAPI field attributes for a set of
    #     :class:`Range <marshmallow.validators.Regexp>` validators.

    #     :param Field field: A marshmallow field.
    #     :rtype: dict
    #     """
    #     regex_validators = (
    #         v
    #         for v in field.validators
    #         if isinstance(getattr(v, "regex", None), RegexType)
    #     )
    #     v = next(regex_validators, None)
    #     attributes = {} if v is None else {"pattern": v.regex.pattern}

    #     if next(regex_validators, None) is not None:
    #         warnings.warn(
    #             "More than one regex validator defined on {} field. Only the "
    #             "first one will be used in the output spec.".format(type(field)),
    #             UserWarning,
    #         )

    #     return attributes

#    def metadata2properties(self, field):
#        """Return a dictionary of properties extracted from field Metadata
#
#        Will include field metadata that are valid properties of `OpenAPI schema
#        objects
#        <https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#schemaObject>`_
#        (e.g. “description”, “enum”, “example”).
#
#        In addition, `specification extensions
#        <https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#specification-extensions>`_
#        are supported.  Prefix `x_` to the desired extension when passing the
#        keyword argument to the field constructor. apispec will convert `x_` to
#        `x-` to comply with OpenAPI.
#
#        :param Field field: A marshmallow field.
#        :rtype: dict
#        """
#        # Dasherize metadata that starts with x_
#        metadata = {
#            key.replace("_", "-") if key.startswith("x_") else key: value
#            for key, value in iteritems(field.metadata)
#        }
#
#        # Avoid validation error with "Additional properties not allowed"
#        ret = {
#            key: value
#            for key, value in metadata.items()
#            if key in _VALID_PROPERTIES or key.startswith(_VALID_PREFIX)
#        }
#        return ret

    def field2property(self, field: types.BaseType) -> dict:
        """Return the JSON Schema property definition given a marshmallow
        :class:`Field <marshmallow.fields.Field>`.

        Will include field metadata that are valid properties of OpenAPI schema objects
        (e.g. "description", "enum", "example").

        https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#schemaObject

        :param Field field: A marshmallow field.
        :rtype: dict, a Property Object

        Args:
            field (types.BaseType): The field

        Returns:
            dict: An updated dict
        """
        ret: dict = {}

        for attr_func in (
            self.field2type_and_format,
            self.field2default,
            self.field2choices,
            # self.field2read_only,
            # self.field2write_only,
            self.field2nullable,
            # self.field2range,
            self.field2length,
            # self.field2pattern,
            # self.metadata2properties,
        ):
            if callable(attr_func):
                ret.update(attr_func(field))

        try:
            if isinstance(field, types.ModelType):
                del ret["type"]
                schema_dict = self.resolve_nested_schema(field.model_class)
                if ret and "$ref" in schema_dict:
                    ret.update({"allOf": [schema_dict]})
                else:
                    ret.update(schema_dict)
            elif isinstance(field, types.ListType):
                ret["items"] = self.field2property(field.field)
        except Exception as e:
            console.error(e)

        return ret

    def resolve_nested_schema(self, schema):
        """Return the Open API representation of a marshmallow Schema.

        Adds the schema to the spec if it isn't already present.

        Typically will return a dictionary with the reference to the schema's
        path in the spec unless the `schema_name_resolver` returns `None`, in
        which case the returned dictoinary will contain a JSON Schema Object
        representation of the schema.

        :param schema: schema to add to the spec
        """
        schema_instance = resolve_schema_instance(schema)
        schema_key = make_schema_key(schema_instance)
        if schema_key not in self.refs:
            schema_cls = self.resolve_schema_class(schema)
            name = self.schema_name_resolver(schema_cls)
            if not name:
                try:
                    json_schema = self.schema2jsonschema(schema)
                except RuntimeError:
                    raise APISpecError(
                        "Name resolver returned None for schema {schema} which is "
                        "part of a chain of circular referencing schemas. Please"
                        " ensure that the schema_name_resolver passed to"
                        " SchematicsPlugin returns a string for all circular"
                        " referencing schemas.".format(schema=schema)
                    )
                if getattr(schema, "many", False):
                    return {"type": "array", "items": json_schema}
                return json_schema
            name = get_unique_schema_name(self.spec.components, name)
            self.spec.components.schema(name, schema=schema)
        return self.get_ref_dict(schema_instance)

    def schema2parameters(
        self, schema: Model,
        default_in: str = "body",
        name: str = "body",
        required: bool = False,
        description: bool = None
    ) -> list:
        """Return an array of OpenAPI parameters given a given a schematics Model.
        If `default_in` is "body", then return an array of a single parameter;
        else return an array of a parameter for each included field in
        the model.

        https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#parameterObject
        """
        openapi_default_in = __location_map__.get(default_in, default_in)
        if self.openapi_version.major < 3 and openapi_default_in == "body":
            prop = self.resolve_schema_dict(schema)

            param = {
                "in": openapi_default_in,
                "required": required,
                "name": name,
                "schema": prop,
            }

            if description:
                param["description"] = description

            return [param]

        assert not getattr(
            schema, "many", False
        ), "Schemas with many=True are only supported for 'json' location (aka 'in: body')"

        fields = get_fields(schema, exclude_dump_only=True)

        return self.fields2parameters(fields, default_in=default_in)

    def fields2parameters(self, fields: types.BaseType, default_in: str = "body") -> list:
        """Return an array of OpenAPI parameters given a mapping between field names and
        ``types.BaseType`` objects. If ``default_in`` is "body", then return an array
        of a single parameter; else return an array of a parameter for each included field in
        the Model.

        In OpenAPI 3, only "query", "header", "path" or "cookie" are allowed for the location
        of parameters. In OpenAPI 3, "requestBody" is used when fields are in the body.

        This function always returns a list, with a parameter
        for each included field in the Model.

        https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#parameterObject
        """
        parameters = []
        body_param = None
        for field_name, field_obj in iteritems(fields):
            if hasattr(field_obj, 'dump_only') and field_obj.dump_only:
                continue
            param = self.field2parameter(
                field_obj,
                name=self._observed_name(field_obj, field_name),
                default_in=default_in,
            )
            if (
                self.openapi_version.major < 3
                and param["in"] == "body"
                and body_param is not None
            ):
                body_param["schema"]["properties"].update(param["schema"]["properties"])
                required_fields = param["schema"].get("required", [])
                if required_fields:
                    body_param["schema"].setdefault("required", []).extend(
                        required_fields
                    )
            else:
                if self.openapi_version.major < 3 and param["in"] == "body":
                    body_param = param
                parameters.append(param)
        return parameters

    def field2parameter(
            self, field: types.BaseType, name: str = "body", default_in: str = "body") -> dict:
        """Return an OpenAPI parameter as a `dict`, given a schematics
        ``types.BaseType``.

        https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#parameterObject
        """
        location = field.metadata.get("location", None)
        prop = self.field2property(field)
        return self.property2parameter(
            prop,
            name=name,
            required=field.required,
            multiple=isinstance(field, types.ListType),
            location=location,
            default_in=default_in,
        )

    def property2parameter(
        self,
        prop: dict,
        name: str = "body",
        required: bool = False,
        multiple: bool = False,
        location: str = None,
        default_in: str = "body",
    ):
        """Return the Parameter Object definition for a JSON Schema property.

        https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#parameterObject

        :param dict prop: JSON Schema property
        :param str name: Field name
        :param bool required: Parameter is required
        :param bool multiple: Parameter is repeated
        :param str location: Location to look for ``name``
        :param str default_in: Default location to look for ``name``
        :raise: TranslationError if arg object cannot be translated to a Parameter Object schema.
        :rtype: dict, a Parameter Object
        """
        openapi_default_in = __location_map__.get(default_in, default_in)
        openapi_location = __location_map__.get(location, openapi_default_in)
        ret = {"in": openapi_location, "name": name}

        if openapi_location == "body":
            ret["required"] = False
            ret["name"] = "body"
            ret["schema"] = {
                "type": "object",
                "properties": {name: prop} if name else {},
            }
            if name and required:
                ret["schema"]["required"] = [name]
        else:
            ret["required"] = required
            if self.openapi_version.major < 3:
                if multiple:
                    ret["collectionFormat"] = "multi"
                ret.update(prop)
            else:
                if multiple:
                    ret["explode"] = True
                    ret["style"] = "form"
                if prop.get("description", None):
                    ret["description"] = prop.pop("description")
                ret["schema"] = prop
        return ret

    def schema2jsonschema(self, schema: Model):
        """Return the JSON Schema Object for a given schematics Model instance.
        Schema may optionally provide the ``title`` and ``description`` class Meta options.

        https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#schemaObject

        Example:
            class WorkExtensionOption(BaseModel, metaclass=ORMMeta):
                works_location_ids = ListType(UUIDType())
                works_locations = ListType(ModelType(WorksLocation))

                class Meta:
                    title = 'User'
                    description = 'A registered user'

            oaic = OpenAPIConverter(openapi_version='3.0.2', schema_name_resolver=resolver, spec=spec)
            pprint(oaic.schema2jsonschema(UserSchema))
            # {'description': 'A registered user',
            #  'properties': {'_id': {'format': 'int32', 'type': 'integer'},
            #                 'email': {'description': 'email address of the user',
            #                           'format': 'email',
            #                           'type': 'string'},
            #                 'name': {'type': 'string'}},
            #  'title': 'User',
            #  'type': 'object'}

        Args:
            schema (Model): The model you want a json schema for

        Returns:
            dict: A jsonschema dict

        """
        fields = get_fields(schema)
        Meta = getattr(schema, "Meta", None)
        partial = getattr(schema, "partial", None)
        ordered = getattr(schema, "ordered", False)

        jsonschema = self.fields2jsonschema(fields, partial=partial, ordered=ordered)

        if hasattr(Meta, "title"):
            jsonschema["title"] = Meta.title
        if hasattr(Meta, "description"):
            jsonschema["description"] = Meta.description

        return jsonschema

    def fields2jsonschema(
        self,
        fields: dict,
        ordered: bool = False,
        partial: Optional[Union[bool, tuple]] = None
    ) -> dict:
        """Return the JSON Schema Object given a mapping between field names and
        types.BaseType objects.

        :param dict fields: A dictionary of field name field object pairs
        :param bool ordered: Whether to preserve the order in which fields were declared
        :param bool|tuple partial: Whether to override a field's required flag.
            If `True` no fields will be set as required. If an iterable fields
            in the iterable will not be marked as required.
        :rtype: dict, a JSON Schema Object
        """
        jsonschema: dict = {
            "type": "object",
            "properties": OrderedDict() if ordered else {}
        }

        for field_name, field_obj in iteritems(fields):
            observed_field_name = self._observed_name(field_obj, field_name)
            property = self.field2property(field_obj)
            jsonschema["properties"][observed_field_name] = property

            if field_obj.required:
                if not partial or (
                    is_collection(partial) and field_name not in partial
                ):
                    jsonschema.setdefault("required", []).append(observed_field_name)

        if "required" in jsonschema:
            jsonschema["required"].sort()

        return jsonschema

    def get_ref_dict(self, schema):
        """Method to create a dictionary containing a JSON reference to the
        schema in the spec
        """
        schema_key = make_schema_key(schema)
        ref_schema = build_reference(
            "schema", self.openapi_version.major, self.refs[schema_key]
        )
        if getattr(schema, "many", False):
            return {"type": "array", "items": ref_schema}
        return ref_schema

    def resolve_schema_dict(self, schema):
        if isinstance(schema, dict):
            if schema.get("type") == "array" and "items" in schema:
                schema["items"] = self.resolve_schema_dict(schema["items"])
            if schema.get("type") == "object" and "properties" in schema:
                schema["properties"] = {
                    k: self.resolve_schema_dict(v)
                    for k, v in schema["properties"].items()
                }
            return schema

        return self.resolve_nested_schema(schema)

    def resolve_schema_class(self, schema):
        """Return schema class for given schema (instance or class)

        :param type|Schema|str: instance, class or class name of marshmallow.Schema
        :return: schema class of given schema (instance or class)
        """
        return resolve_schema_cls(schema)
