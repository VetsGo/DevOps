import click

@click.group()
def cli():
    """CLI-утиліта для демонстрації Click"""
    pass

@cli.command()
@click.option('--name', prompt="Введіть ім’я", help='Ім’я користувача')
def say(name):
    """Виводить ім’я або повідомлення, якщо воно починається з p/P."""
    if name.lower().startswith('p'):
        click.echo("Ім’я не підходить")
    else:
        click.echo(name)

if __name__ == '__main__':
    cli()