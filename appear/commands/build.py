import click
import json
import os
from appear.templates.backend import get_backend_application

# TODO: Create path&filename builder
BACKEND_FILE = '.appear/schema/backend/appear.config.json'
CONTAINER_FILE = '.appear/schema/container/appear.config.json'
DATABASE_FILE = '.appear/schema/database/appear.config.json'
FRONTEND_FILE = '.appear/schema/frontend/appear.config.json'


def load_appear_config():
    whole_app = dict()
    if os.path.isdir('.appear') is False:
        click.echo(click.style('No appear configuration available, generate one with appear init', bg='red'))
        return False
    if os.path.isfile(BACKEND_FILE):
        with open(BACKEND_FILE) as json_file:
            whole_app['backend'] = json.load(json_file)
    if os.path.isfile(CONTAINER_FILE):
        with open(CONTAINER_FILE) as json_file:
            whole_app['container'] = json.load(json_file)
    if os.path.isfile(DATABASE_FILE):
        with open(DATABASE_FILE) as json_file:
            whole_app['database'] = json.load(json_file)
    if os.path.isfile(FRONTEND_FILE):
        with open(FRONTEND_FILE) as json_file:
            whole_app['frontend'] = json.load(json_file)
    return whole_app


def generate_app():
    """Creates a summary report for hte generated builds."""
    click.echo(click.style(f'Building app in {os.getcwd()}', bg='green'))
    config = load_appear_config()
    if config is False:
        exit(1)

    backend = None
    if config['backend'] is None:
        click.echo(click.style('Backend is not defined', bg='yellow'))

    backend_config = config.get('backend')
    if backend_config is None:
        click.echo(click.style('Backend is not defined', bg='yellow'))

    backend_generator = get_backend_application(backend_config)
    if backend_generator is None:
        click.echo(click.style('Backend generator is not defined', bg='yellow'))
    else:
        backend = backend_generator.Application()
        backend.generate_backend_files(backend_config)


def generate_summary():
    """Creates a summary report for hte generated builds."""
    click.echo(click.style('Summary:', bg='green'))
