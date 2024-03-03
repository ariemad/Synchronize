import os
import json
import shutil

from .paths import paths


def clean_up(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


def clean_up_all(paths):
    for path in paths:
        clean_up(path)


def is_valid_json(file_path):
    try:
        with open(file_path, "r") as f:
            json.load(f)
        return True
    except ():
        return False


def copy_file(source, destination):
    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))
    with open(source, "rb") as src_file:
        with open(destination, "wb") as dest_file:
            dest_file.write(src_file.read())
