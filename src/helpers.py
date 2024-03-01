import os
import json
from .paths import paths

def clean_up():
    if os.path.exists(paths['config']):
        os.remove(paths['config'])

def is_valid_json(file_path):
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        return True
    except ():
        return False

def copy_file(source, destination):
    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))
    with open(source, 'rb') as src_file:
        with open(destination, 'wb') as dest_file:
            dest_file.write(src_file.read())