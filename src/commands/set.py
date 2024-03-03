import json

from src.paths import paths


def set(source, replica, log, interval):

    options = {
        "source": source,
        "replica": replica,
        "log": log,
        "interval": interval,
    }

    print(options)

    with open(paths["config"], "r") as file:
        config = json.load(file)

    for key in options:
        if options[key] and key in config:
            config[key] = options[key]

    with open(paths["config"], "w") as file:
        json.dump(config, file, indent=4)
