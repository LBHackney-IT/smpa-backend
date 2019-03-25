from apispec import APISpec
from falcon_apispec import FalconPlugin
from apispec.ext.marshmallow import MarshmallowPlugin

from ..rdb.registry import model_registry


def create_spec(app):
    spec = APISpec(
        title='Submit my Planning Application',
        version='1.0.0',
        openapi_version='3.0',
        plugins=[
            FalconPlugin(app),
            MarshmallowPlugin()
        ],
    )

    return spec


def add_components(spec):
    for k, v in model_registry._models.items():
        spec.components.schema(k, schema=v)


def add_resources(spec, config):
    for resource in config.resources:
        spec.path(resource=resource)


def init_swagger(app, config):
    # Create an APISpec
    spec = create_spec(app)
    add_components(spec)
    add_resources(spec, config)

    return spec
