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

    if not os.path.exists(config["log"]):
        os.makedirs(config["log"])
