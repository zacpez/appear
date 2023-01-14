"""Backend templates"""

from importlib import import_module
from types import ModuleType


SUPER_TYPE = 'python'


def get_backend_application(schema_model):
    application_type = schema_model.get('type')
    if application_type is not None:
        importer: ModuleType = import_module(
            f'appear_schema.templates.backend.{SUPER_TYPE}.{application_type}'
        )
        return importer
    return None
