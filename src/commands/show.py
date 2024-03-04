import json
import os

from src.paths import paths


def showLog():
    with open(paths["config"], "r") as file:
        config = json.load(file)

    logPath = os.path.join(config["log"], paths["defaultLogFile"])
    with open(logPath, "r") as file:
        content = file.read()

    print(content)


def showConfig():
    with open(paths["config"], "r") as file:
        content = file.read()

    print(content)
