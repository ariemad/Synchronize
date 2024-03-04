import typer

from src.commands import command
from src.error import throw_and_exit
from src.check_config import check_config
from src.create_folders import create_folders


app = typer.Typer()


@app.command()
def start(
    repeat: bool = typer.Option(
        False,
        "--repeat",
        "-r",
        help="Runs the synchronization tool periodically, according to time interval ",
    ),
    print: bool = typer.Option(
        False, "--print", "-p", help="Prints the logs to the terminal "
    ),
):
    """
    Runs the synchronization script.
    """
    command.validate()
    command.start(repeat, print)


@app.command()
def validate():
    """
    Validates the config file.
    Informs the user if there is any incorrect value.
    """
    command.validate()
    print("Config is valid.")


@app.command()
def showlog():
    """
    Shows logs.
    """
    command.showLog()


@app.command()
def showconfig():
    """
    Shows config.
    """
    command.showConfig()


@app.command()
def set(
    source: str = typer.Option(None, "--source", help="Defines the source path"),
    replica: str = typer.Option(None, "--replica", help=" Defines the replica path"),
    log: str = typer.Option(None, "--log", help="Defines the log path"),
    interval: int = typer.Option(
        None,
        "--interval",
        help="Defines the synchronization interval in seconds (minimum of 10 seconds)",
    ),
):
    """
    Changes a value in the config.
    """
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
