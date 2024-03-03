import typer

from src.commands import command
from src.error import throw_and_exit
from src.check_config import check_config
from src.create_folders import create_folders


app = typer.Typer()


@app.command()
def start():
    command.start()


@app.command()
def show():
    command.show()


@app.command()
def set():
    command.set()


@app.callback()
def callback():
    """
    A directory synchronization tool.

    Created as an applicable test task for Veeam.
    """

    pass


if __name__ == "__main__":
    check_config()
    create_folders()
    app()
else:
    raise ImportError("Run this file directly. Do not import it")
