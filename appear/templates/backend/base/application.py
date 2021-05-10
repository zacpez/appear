"""Base Application Model"""
from jinja2 import Template


class Application():
    def __init__(self):
        self.name = "base application"

    def generate_template(template, filename, model):
        template_fd = open(template, "r")
        template = Template(template_fd.read())
        template_fd.close()
        generated_content = template.render(**model)
        generated_fd = open(filename, "w")
        generated_fd.write(generated_content)
        generated_fd.close()

    def generate_backend_files(self, schema_model):
        pass
