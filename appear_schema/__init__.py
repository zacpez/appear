"""Appear Schema commands and argument parsing"""
import click
from appear_schema.commands.build import generate_app, generate_summary
from appear_schema.commands.init import generate_config
from appear_schema.commands.test import run_tests
from appear_schema.commands.publish import run_publish

__package__ = "appear_schema"
__version__ = "0.2.0"
__date__ = "2023-01-14"
DEBUG = False


@click.group()
@click.version_option(version=__version__)
@click.pass_context
def appear_schema(ctx):
    """
    Appear Schema is a CLI toolkit to generate application code.

    Example:\n
    \t$ appear-schema build --summary
    """
    if DEBUG:
        print(ctx)
    if ctx.invoked_subcommand is None:
        click.echo('A command must be used: build, init, test')
    ctx.ensure_object(dict)


@appear_schema.command()
@click.option("--summary", "summary",
              is_flag=True,
              help="Describes the current project's appear-schema configuration")
@click.pass_context
def build(ctx, summary):
    """Builds an application from the appear-schema configuration"""
    if DEBUG:
        print(ctx)
    if summary:
        generate_summary()
    click.echo(generate_app())


@appear_schema.command()
@click.option("--frontend", "frontend",
              default='vue',
              help="Identifies a frontend to put in the appear-schema configuration")
@click.option("--backend", "backend",
              default='flask',
              help="Identifies a backend to put in the appear-schema configuration")
@click.option("--database", "database",
              default='postgres',
              help="Identifies a database to put in the appear-schema configuration")
@click.option("--containers", "containers",
              default='nginx',
              help="Identifies containers to put in the appear-schema configuration")
@click.pass_context
def init(ctx, frontend, backend, database, containers):
    """Creates an appear-schema configuration in .appear-schema/"""
    if DEBUG:
        print(ctx)
    click.echo(generate_config(__version__,
                               __date__,
                               frontend,
                               backend,
                               database,
                               containers.split(",")))


@appear_schema.command()
@click.pass_context
def test(ctx):
    """Tests the appear-schema configuration and application"""
    if DEBUG:
        print(ctx)
    click.echo(run_tests())


@appear_schema.command()
@click.pass_context
def publish(ctx):
    """Builds and publishes the appear-schema hosted assets"""
    if DEBUG:
        print(ctx)
    click.echo(run_publish(__version__, __date__))
