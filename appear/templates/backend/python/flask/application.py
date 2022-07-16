"""Flask(Python) Application Model"""
from appear.templates.backend.python.application import Application as BaseApplication


class Application(BaseApplication):
    ''' Application used in template generation '''
    def __init__(self):
        super().__init__()
        self.name = "flask(python) application"

    def generate_application(self, template, filename, application_model):
        ''' application template rendering '''
        self.generate_template(template, filename, application_model)

    def generate_resources(self, resources_model):
        ''' resources template rendering '''
        for resource_model in resources_model:
            template = resources_model.get('template')
            filename = resources_model.get('filename')
            self.generate_template(template, filename, resource_model)

    def generate_backend_files(self, schema_model):
        ''' Full application templates rendering '''
        super().generate_backend_files(schema_model)

        application = schema_model.get('application')
        resources = schema_model.get('resources')

        if resources is not None:
            self.generate_resources(resources)

        if application is not None:
            template = schema_model.get('template')
            filename = schema_model.get('filename')
            application = schema_model.get('application')
            self.generate_application(template, filename, application)
