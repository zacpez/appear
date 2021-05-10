import click
import os
from appear.templates.backend import get_backend_application


def load_appear_config():
    if os.path.isdir('.appear') is False:
        click.echo(click.style('No appear configuration available, generate one with appear init', bg='red'))
        return False
    return dict()


def generate_app():
    """Creates a summary report for hte generated builds."""
    click.echo(click.style(f'Building app in {os.getcwd()}', bg='green'))
    config = load_appear_config()
    if config is False:
        exit(1)

    backend = None
    backend_generator = get_backend_application(config.backend)
    if backend_generator is None:
        click.echo(click.style('Backend is not defined', bg='yellow'))
    else:
        backend = backend_generator.Application()
        backend.generate_backend_files()


def generate_summary():
    """Creates a summary report for hte generated builds."""
    click.echo(click.style('Summary:', bg='green'))
