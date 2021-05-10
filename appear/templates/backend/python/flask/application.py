"""Flask(Python) Application Model"""
from jinja2 import Template
from appear.templates.backend.python.application import Application as BaseApplication


class Application(BaseApplication):
    def __init__(self):
        self.name = "flask(python) application"

    def generate_application(self, template, filename, application_model):
        template_fd = open(template, "r")
        template = Template(template_fd.read())
        template_fd.close()
        generated_content = template.render(**application_model)
        generated_fd = open(filename, "w")
        generated_fd.write(generated_content)
        generated_fd.close()
        pass

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
