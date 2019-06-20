from apispec import APISpec
from apispec.exceptions import DuplicateComponentNameError
from falcon_apispec import FalconPlugin

from ..openapi.schematics import SchematicsPlugin
from ..rdb.registry import model_registry
from smpa.helpers.console import console


def create_spec(app):
    spec = APISpec(
        title='Submit my Planning Application',
        version='1.0.0',
        openapi_version='3.0',
        plugins=[
            FalconPlugin(app),
            SchematicsPlugin()
        ],
    )

    return spec


def add_components(spec):
    console.log('ADD COMPONENTS CALLED')
    for k, v in model_registry._models.items():
        try:
            spec.components.schema(k, schema=v)
        except DuplicateComponentNameError as e:
            console.warn(e)
            # import ipdb; ipdb.set_trace()


def add_resources(spec, config):
    for resource in config.resources:
        spec.path(resource=resource)


def init_swagger(app, config):
    # Create an APISpec
    spec = create_spec(app)
    add_components(spec)
    add_resources(spec, config)

    # import ipdb; ipdb.set_trace()

    return spec
