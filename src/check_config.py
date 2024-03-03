import os
import json
import pathvalidate

from .helpers import *
from .paths import paths
from .error import *


def check_config():
    if not os.path.exists(paths["config"]):
        copy_file(paths["defaultConfig"], paths["config"])
        return

    with open(paths["config"], "r") as file:
        config = json.load(file)

    with open(paths["defaultConfig"], "r") as file:
        defaultConfig = json.load(file)

    missingKeys = []
    for key in defaultConfig:
        if key not in config:
            missingKeys.append(key)
    if len(missingKeys) > 0:
        throw_missing_keys(missingKeys)

    incorrectPaths = {}
    for key in ["source", "replica", "log"]:
        if not pathvalidate.is_valid_filepath(config[key]):
            incorrectPaths[key] = config[key]

    if len(incorrectPaths) > 0:
        throw_incorrect_paths(incorrectPaths)

    if not isinstance(config["interval"], int) or config["interval"] < 300:
        throw_incorrect_interval()
