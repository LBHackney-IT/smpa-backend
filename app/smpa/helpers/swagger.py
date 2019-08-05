from apispec import APISpec
from apispec.exceptions import DuplicateComponentNameError
from falcon_apispec import FalconPlugin

from ..openapi.schematics import SchematicsPlugin
from smpa.helpers.console import console
from smpa.db.documentdb.registry import model_registry


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
    models = model_registry.get_models()
    try:
        for k, v in models.items():
            try:
                spec.components.schema(k, schema=v)
            except DuplicateComponentNameError as e:
                pass
            except Exception as e:
                console.error(e)
    except Exception as e:
        console.error(e)


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
