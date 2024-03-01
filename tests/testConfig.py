import pytest

import os
import subprocess

from src.paths import paths
from src.helpers import *

commandSimple = ["python", "synchronize.py"]

# Tests


def test_create_config_if_not_exist():
    subprocess.run(commandSimple, stdout=subprocess.PIPE)
    assert os.path.exists(paths["config"]), f"File '{paths['config']}' does not exist"


def test_json_file_validity():
    subprocess.run(commandSimple, stdout=subprocess.PIPE)

    assert is_valid_json(
        paths["config"]
    ), f"File '{paths['config']}' is not a valid JSON file"


def test_missing_keys():

    copy_file("tests/testData/missingKeysConfig.json", paths["config"])

    out = subprocess.run(commandSimple, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Missing Keys"


def test_missing_keys2():

    copy_file("tests/testData/missingKeysConfig2.json", paths["config"])

    out = subprocess.run(commandSimple, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Missing Keys"


def test_incorrect_path():

    copy_file("tests/testData/incorrectPathConfig.json", paths["config"])

    out = subprocess.run(commandSimple, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Incorrect Path"


def test_incorrect_path2():

    copy_file("tests/testData/incorrectPathConfig2.json", paths["config"])

    out = subprocess.run(commandSimple, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Incorrect Path"


def test_incorrect_path3():

    copy_file("tests/testData/incorrectPathConfig3.json", paths["config"])

    out = subprocess.run(commandSimple, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Incorrect Path"


def test_incorrect_interval():

    copy_file("tests/testData/incorrectPathConfig3.json", paths["config"])

    out = subprocess.run(commandSimple, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Incorrect Path"


# Do before and after tests


@pytest.fixture(autouse=True)
def before_and_after_test():
    clean_up()
    yield
    clean_up()
