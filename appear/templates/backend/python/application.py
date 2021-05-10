"""Python Application Model"""
from appear.templates.backend.base.application import Application as BaseApplication


class Application(BaseApplication):
    def __init__(self):
        self.name = "python application"

    def generate_requirements(self, template, filename, requirements):
        self.generate_template(template, filename, requirements)

    def generate_backend_files(self, schema_model):
        requirements = getattr(schema_model, 'requirements')
        if requirements is not None:
            self.generate_requirements(requirements.template, requirements.filename, requirements.packages)
        return
