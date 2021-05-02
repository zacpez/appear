import click
import os


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


def generate_summary():
    """Creates a summary report for hte generated builds."""
    click.echo(click.style('Summary:', bg='green'))
