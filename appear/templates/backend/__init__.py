"""Backend templates"""

from importlib import import_module
from types import ModuleType


super_type = 'python'


def get_backend_application(schema_model):
    application_type = schema_model['type']
    if application_type is not None:
        importer: ModuleType = import_module(f'appear.templates.backend.{super_type}.{application_type}')
        return importer
    return None
