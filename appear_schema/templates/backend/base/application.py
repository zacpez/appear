"""Base Application Model"""
from jinja2 import Template


class Application():
    ''' Application used in template generation '''
    def __init__(self):
        super().__init__()
        self.name = "base application"

    def generate_template(self, template, filename, model):
        ''' basic template rendering '''
        try:
            template_fd = open(template, "r", encoding='utf-8')
            template = Template(template_fd.read())
            template_fd.close()
            generated_content = template.render(**model)
            generated_fd = open(filename, "w", encoding='utf-8')
            generated_fd.write(generated_content)
            generated_fd.close()

        except (FileNotFoundError, IOError) as error:
            print(f'{error.errno}: Failed to write {template}, {filename}')

    def generate_backend_files(self, schema_model):
        ''' basic application template rendering '''
        pass
