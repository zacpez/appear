from appear.schema.namespaces import generate_schema
import os

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

    create_templates_schemas(frontend)
    create_templates_schemas(backend)
    create_templates_schemas(database)

    if len(containers) > 0:
        for container in containers:
            create_templates_schemas(container)


def create_templates_schemas(name):
    """Create the schema-template directory pattern"""
    if name is not None:
        schema_path = "{}{}".format(SCHEMA_PATH, name)
        template_path = "{}{}".format(TEMPLATES_PATH, name)

        if os.path.isdir(schema_path) is not True:
            os.mkdir(schema_path)
        if os.path.isdir(template_path) is not True:
            os.mkdir(template_path)
