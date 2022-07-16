from appear.schema.namespaces import generate_schema
import click
import os
import time

PUBLIC_DIR = "public/"
CONTENT_DIR = "frontend/content/"


def run_publish(version, date):
    """Builds the publishable a appear assets"""
    build_appear_assets(version, date)
    click.echo("Ready to publish...")
    if click.confirm('Do you want to publish the build now?', default=False):
        publish_appear_assets()
        click.echo('Well done!')


def build_appear_assets(version, date):
    """Builds the publishable a appear assets"""
    click.echo(click.style("Building public source", bg="bright_blue"))
    start = time.time()

    if os.path.isdir(PUBLIC_DIR) is not True:
        os.mkdir(PUBLIC_DIR)
    create_frontend()
    schema_path = create_schema_directories(version)
    create_python_docs(schema_path)
    create_schema_files(schema_path, version, date)
    create_markdown_pages()

    end = time.time()
    click.echo(click.style("Build finished in {} seconds".format(end - start), bg="green"))


def publish_appear_assets():
    """Uploads the built assets to the hosting service"""
    pass


def create_frontend():
    click.echo("Create frontend application")
    os.system('yarn --cwd frontend generate')


def create_python_docs(schema_path):
    click.echo("Creating python docs")
    os.system(f'pdoc3 --html -o {schema_path}docs --force appear')
    # TODO: Make main documentation page the latest version


def create_markdown_pages():
    """Copies markdown from codebase to page content directory"""
    click.echo("Copying markdown pages")
    os.system(f'rm -rf {CONTENT_DIR}*')
    if os.path.isdir(f'{CONTENT_DIR}rfcs/') is False:
        os.mkdir(f'{CONTENT_DIR}rfcs/')
    os.system(f'cp rfcs/*.md {CONTENT_DIR}rfcs/')
    os.system(f'cp README.md {CONTENT_DIR}')
    os.system(f'cp CONTRIBUTION.md {CONTENT_DIR}')


def create_schema_directories(version):
    """Create the schema version directory pattern.
    http://appear-schema.org/{major}/{minor}/{patch}/"""
    click.echo("Creating schema version directories")
    versions = version.split('.')
    major = f'{PUBLIC_DIR}{versions[0]}/'
    minor = f'{major}{versions[1]}/'
    patch = f'{minor}{versions[2]}/'

    if os.path.isdir(major) is not True:
        os.mkdir(major)
    if os.path.isdir(minor) is not True:
        os.mkdir(minor)
    if os.path.isdir(patch) is not True:
        os.mkdir(patch)
    return patch


def create_schema_files(schema_path, version, date):
    """Creates schema files from class definitions"""
    click.echo("Writing schemas")
    f = open(f'{schema_path}namespaces', 'w')
    f.write(generate_schema(version, date))
    f.close()
