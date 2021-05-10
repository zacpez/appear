from appear.schema.namespaces import generate_schema
import os
import json

ROOT_PATH = ".appear/"
SCHEMA_PATH = ROOT_PATH + "schema/"
TEMPLATES_PATH = ROOT_PATH + "templates/"


def generate_config(version, date, frontend, backend, database, containers):
    """Generate an appear configuration"""
    create_paths(frontend, backend, database, containers)
    print(generate_schema(version, date))


def create_paths(frontend, backend, database, containers):
    """Create configuration paths"""
    if os.path.isdir(ROOT_PATH) is not True:
        os.mkdir(ROOT_PATH)

    if os.path.isdir(SCHEMA_PATH) is not True:
        os.mkdir(SCHEMA_PATH)

    if os.path.isdir(TEMPLATES_PATH) is not True:
        os.mkdir(TEMPLATES_PATH)

    create_templates_schemas('frontend', frontend)
    create_templates_schemas('backend', backend)
    create_templates_schemas('database', database)

    if len(containers) > 0:
        for container in containers:
            create_templates_schemas('container', container)


def create_templates_directories(schema_path, template_path):
    """Create the schema-template directory pattern"""
    if os.path.isdir(schema_path) is not True:
        os.mkdir(schema_path)
    if os.path.isdir(template_path) is not True:
        os.mkdir(template_path)


def create_templates_schemas(schema_type, name):
    """Create the schema-template directory pattern"""
    if name is None:
        return False
    schema_path = f'{SCHEMA_PATH}{schema_type}/'
    template_path = f'{TEMPLATES_PATH}{schema_type}/'

    create_templates_directories(schema_path, template_path)
    config_fd = open(f'{schema_path}appear.config.json', 'w')
    config_fd.write(json.dumps(dict(type=name)))
    config_fd.close()
    template_fd = open(f'{template_path}appear.config.jinja', 'w')
    template_fd.write(json.dumps(dict(type=name)))
    template_fd.close()
