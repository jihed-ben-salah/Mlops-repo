"""this  file is for making calculation functions"""
"""this file also is supposed to be invoked as a command line script using click"""

import click

def add(a, b):
    return a + b
def sub(a, b):
    return a - b

"""cretae a click group to group all the commands together"""
@click.group()
def cli():
    pass
"""create a click command to add two numbers"""
@cli.command('add')
@click.argument('a',type=int)
@click.argument('b',type=int)
def add_command(a, b):
    """add two numbers"""
    click.echo(add(a, b))
"""create a click command to subtract two numbers"""
@cli.command('sub')
@click.argument('a',type=int)
@click.argument('b',type=int)
def sub_command(a,b):
    """substract two numbers"""
    click.echo(sub(a,b))

if __name__ == '__main__':
    cli()