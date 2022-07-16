"""Python Application Model"""
from appear.templates.backend.base.application import Application as BaseApplication


class Application(BaseApplication):
    ''' Application used in template generation '''
    def __init__(self):
        super().__init__()
        self.name = "python application"

    def generate_requirements(self, template, filename, requirements_model):
        ''' requirements template rendering '''
        self.generate_template(template, filename, requirements_model)

    def generate_backend_files(self, schema_model):
        ''' application template rendering '''
        requirements = schema_model.get('requirements')
        template = requirements.get('template')
        filename = requirements.get('filename')
        packages = requirements.get('packages')
        if template is not None and filename is not None and packages is not None:
            self.generate_requirements(template, filename, packages)
        return
