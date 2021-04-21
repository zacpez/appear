import click
from appear.commands.build import generate_app, generate_summary
from appear.commands.init import generate_config
from appear.commands.test import run_tests

__package__ = "appear"
__version__ = "0.0.1"
__date__ = "2021-04-21"


@click.group()
@click.version_option(version=__version__)
@click.pass_context
def appear(ctx):
    """
    Appear is a CLI toolkit to generate application code.

    Example:\n
    \t$ appear build --summary
    """
    if ctx.invoked_subcommand is None:
        click.echo('A command must be used: build, init, test')
    ctx.ensure_object(dict)


@appear.command()
@click.option("--summary", "summary",
              is_flag=True,
              help="Describes the current project's appear configuration")
@click.pass_context
def build(ctx, summary):
    """Builds an application from the appear configuration"""
    if summary:
        generate_summary()
    click.echo(generate_app())


@appear.command()
@click.option("--frontend", "frontend",
              default='vue',
              help="Identifies a frontend to put in the appear configuration")
@click.option("--backend", "backend",
              default='flask',
              help="Identifies a backend to put in the appear configuration")
@click.option("--database", "database",
              default='postgres',
              help="Identifies a database to put in the appear configuration")
@click.option("--container", "container",
              default='nginx',
              help="Identifies a container to put in the appear configuration")
@click.pass_context
def init(ctx, frontend, backend, database, container):
    """Creates an appear configuration in .appear/"""
    click.echo(frontend)
    click.echo(backend)
    click.echo(database)
    click.echo(container)
    click.echo(generate_config(__version__, __date__))


@appear.command()
@click.pass_context
def test(ctx):
    """Tests the appear configuration and application"""
    click.echo(run_tests(__version__, __date__))
