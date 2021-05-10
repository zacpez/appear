"""Backend templates"""


def get_backend_application(schema_model):
    application_type = getattr(schema_model, type, None)
    if application_type is not None:
        importer = __import__(f'appear.templates.backend.{schema_model.type}', globals(), locals())
        return importer
    return None
