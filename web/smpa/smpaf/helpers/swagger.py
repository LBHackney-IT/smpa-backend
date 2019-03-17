from apispec import APISpec
from falcon_apispec import FalconPlugin

from ..rdb.registry import model_registry


def init_swagger(app):
    # Create an APISpec
    spec = APISpec(
        title='Submit my Planning Application',
        version='1.0.0',
        openapi_version='2.0',
        plugins=[
            FalconPlugin(app),
        ],
    )

    for k, v in model_registry._models.items():
        spec.components.schema(k, schema=v)

    return spec
