from appear.schema.namespaces import generate_schema
import os
# import json
import importlib.resources


# TODO: Create path&filename builder
ROOT_PATH = ".appear/"
SCHEMA_PATH = ROOT_PATH + "schema/"
TEMPLATES_PATH = ROOT_PATH + "templates/"


def generate_config(version, date, frontend, backend, database, containers):
    """Generate an appear configuration"""
    create_paths(frontend, backend, database, containers)
    print(generate_schema(version, date))


def create_paths(frontend, backend, database, containers):
    """Create configuration paths"""
    if os.path.isdir(ROOT_PATH) is False:
        os.mkdir(ROOT_PATH)

    if os.path.isdir(SCHEMA_PATH) is False:
        os.mkdir(SCHEMA_PATH)

    if os.path.isdir(TEMPLATES_PATH) is False:
        os.mkdir(TEMPLATES_PATH)

    if frontend is not None:
        create_templates_schemas('frontend', frontend)

    if backend is not None:
        create_templates_schemas('backend', backend)

    if database is not None:
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

    # TODO: Convert to a http request for assets
    # TODO: Create path&filename builder
    schema_source_path = f'schemas/{schema_type}/{name}/'
    with importlib.resources.path("appear", f'{schema_source_path}appear.config.json') as data_path:
        with open(data_path, 'r') as config_source_fd:
            config_content = config_source_fd.read()
            config_target_fd = open(f'{schema_path}appear.config.json', 'w')
            config_target_fd.write(config_content)
            config_target_fd.close()

    # TODO: Create path&filename builder
    template_source_path = f'templates/{schema_type}/{name}/'
    with importlib.resources.path("appear", f'{template_source_path}appear.config.json') as data_path:
        with open(data_path, 'r') as template_source_fd:
            template_content = template_source_fd.read()
            template_fd = open(f'{template_path}appear.config.jinja', 'w')
            template_fd.write(template_content)
            template_fd.close()
