import typer

from src.commands import command
from src.error import throw_and_exit
from src.check_config import check_config
from src.create_folders import create_folders


app = typer.Typer()


@app.command()
def start(
    repeat: bool = typer.Option(
        False, "--repeat", "-r", help="Repeat according to interval "
    ),
    print: bool = typer.Option(
        False, "--print", "-p", help="Prints log to the terminal "
    ),
):
    command.validate()
    command.start(repeat, print)


@app.command()
def validate():
    command.validate()
    print("Config is valid.")


@app.command()
def showlog():
    command.showLog()


@app.command()
def showconfig():
    command.showConfig()


@app.command()
def set(
    source: str = typer.Option(None, "--source", help="Source path"),
    replica: str = typer.Option(None, "--replica", help="Replica path"),
    log: str = typer.Option(None, "--log", help="Logs path"),
    interval: int = typer.Option(None, "--interval", help="Interval"),
):
    command.set(source, replica, log, interval)


@app.callback()
def callback():
    """
    A directory synchronization tool.

    Created as an applicable test task for Veeam.
    """

    pass


if __name__ == "__main__":

    app()
else:
    raise ImportError("Run this file directly. Do not import it")
