import os
import paths
import json

def clean_up():
    if os.path.exists(paths['defaultConfig']):
        os.remove(paths['defaultConfig'])

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