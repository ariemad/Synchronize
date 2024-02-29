import typer

from src.commands import command


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

if __name__ == "__main__":
    app()
else:
    raise ImportError("Run this file directly. Do not import it")