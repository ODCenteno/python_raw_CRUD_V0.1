import click
from clients import commands as client_commands

CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def cli(ctx):
    """An Aplicaction to manage clients, inventory, sales and produce reports"""
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(client_commands.all)