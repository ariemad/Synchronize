import os
import json
import shutil
import hashlib

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


def compare_json_files(file1_path, file2_path):
    with open(file1_path, "r") as file1:
        data1 = json.load(file1)

    with open(file2_path, "r") as file2:
        data2 = json.load(file2)

    print(data1)
    print(data2)

    return data1 == data2


def copy_file(source, destination):
    if os.path.isdir(destination):
        destination = os.path.join(destination, os.path.basename(source))
    with open(source, "rb") as src_file:
        with open(destination, "wb") as dest_file:
            dest_file.write(src_file.read())


def copy_folder(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)
        if os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item)
        else:
            shutil.copy2(source_item, destination_item)


def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()


def get_all_files(path, relative_to=None):
    file_paths = []
    # Walk through the directory tree
    for root, directories, files in os.walk(path):
        # Append file paths to the list
        for filename in files:
            file_path = os.path.join(root, filename)
            if relative_to:
                file_path = os.path.relpath(file_path, relative_to)
            file_paths.append(file_path)

    return file_paths


def compare_folders(folder1, folder2):
    files1 = get_all_files(folder1, folder1)
    files2 = get_all_files(folder2, folder2)

    if len(files1) != len(files2):
        return False

    if files1 != files2:
        return False

    for file in files1:
        md5_1 = calculate_md5(os.path.join(folder1, file))
        md5_2 = calculate_md5(os.path.join(folder2, file))
        if md5_1 != md5_2:
            return False

    return True
