"""Flask(Python) Application Model"""
from appear.templates.backend.python.application import Application as BaseApplication


class Application(BaseApplication):
    def __init__(self):
        super.__init__()
        self.name = "flask(python) application"

    def generate_application(self, template, filename, application_model):
        self.generate_template(template, filename, application_model)

    def generate_resources(self, resources_model):
        for resource_model in resources_model:
            self.generate_template(resource_model.template, resource_model.filename, resource_model)
        pass

    def generate_backend_files(self, schema_model):
        super.generate_backend_files(schema_model)

        application = getattr(schema_model, 'application')
        resources = getattr(application, 'resources')

        if resources is not None:
            self.generate_resources(resources)

        if application is not None:
            self.generate_application(schema_model.template, schema_model.filename, schema_model.application)
        pass
