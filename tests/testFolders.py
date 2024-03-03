import pytest

import os
import subprocess

from src.paths import paths
from src.helpers import *

commandSimple = ["python", "synchronize.py", "validate"]

# Tests


def test_folder_creation():
    copy_file(paths["defaultConfig"], paths["config"])
    os.makedirs(paths["defaultSource"])
    os.makedirs(paths["defaultReplica"])

    assert os.path.exists(paths["config"]), f"File '{paths['config']}' does not exist"
    assert os.path.exists(
        paths["defaultSource"]
    ), f"File '{paths['config']}' does not exist"
    assert os.path.exists(
        paths["defaultReplica"]
    ), f"File '{paths['config']}' does not exist"


def test_clean_up_all():
    copy_file(paths["defaultConfig"], paths["config"])
    os.makedirs(paths["defaultSource"])
    os.makedirs(paths["defaultReplica"])

    paths_to_clean = [paths["config"], paths["defaultSource"], paths["defaultReplica"]]
    clean_up_all(paths_to_clean)

    assert not os.path.exists(paths["config"]), f"File '{paths['config']}' does exist"
    assert not os.path.exists(
        paths["defaultSource"]
    ), f"File '{paths['config']}' does exist"
    assert not os.path.exists(
        paths["defaultReplica"]
    ), f"File '{paths['config']}' does exist"


def test_folder_source_not_exist():
    out = subprocess.run(commandSimple, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Folder source does not exist"


def test_create_folders_if_not_exist():
    os.makedirs(paths["defaultSource"])

    subprocess.run(commandSimple, stdout=subprocess.PIPE)

    assert os.path.exists(
        paths["defaultReplica"]
    ), f"File '{paths['defaultReplica']}' does not exist"
    assert os.path.exists(
        paths["defaultLog"]
    ), f"File '{paths['defaultLog']}' does not exist"


def test_create_replica():
    os.makedirs(paths["defaultSource"])
    os.makedirs(paths["defaultLog"])

    subprocess.run(commandSimple, stdout=subprocess.PIPE)

    assert os.path.exists(
        paths["defaultReplica"]
    ), f"File '{paths['defaultReplica']}' does not exist"


def test_create_logs():
    os.makedirs(paths["defaultSource"])
    os.makedirs(paths["defaultReplica"])

    subprocess.run(commandSimple, stdout=subprocess.PIPE)

    assert os.path.exists(
        paths["defaultLog"]
    ), f"File '{paths['defaultLog']}' does not exist"


# Do before and after tests

paths_to_clean = [
    paths["config"],
    paths["defaultSource"],
    paths["defaultReplica"],
    paths["defaultLog"],
]


@pytest.fixture(autouse=True)
def before_and_after_test():
    clean_up_all(paths_to_clean)
    yield
    clean_up_all(paths_to_clean)
