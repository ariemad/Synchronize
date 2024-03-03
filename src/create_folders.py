import os
import json
import pathvalidate

from .helpers import *
from .paths import paths
from .error import *


def create_folders():
    with open(paths["config"], "r") as file:
        config = json.load(file)

    if not os.path.exists(config["source"]):
        throw_source_not_exist()

    if not os.path.exists(config["replica"]):
        os.makedirs(config["replica"])

    filePath = os.path.join(config["log"], paths["defaultLogFile"])
    if not os.path.exists(filePath):
        os.makedirs(os.path.dirname(config["log"]), exist_ok=True)
        with open(filePath, "a"):
            pass
