import pytest

import os
import subprocess

from src.paths import paths
from src.helpers import *

commandValidate = ["python", "synchronize.py", "validate"]

# Tests


def test_create_config_if_not_exist():
    subprocess.run(commandValidate, stdout=subprocess.PIPE)
    assert os.path.exists(paths["config"]), f"File '{paths['config']}' does not exist"


def test_json_file_validity():
    subprocess.run(commandValidate, stdout=subprocess.PIPE)

    assert is_valid_json(
        paths["config"]
    ), f"File '{paths['config']}' is not a valid JSON file"


def test_missing_keys():

    copy_file("tests/testConfigData/missingKeysConfig.json", paths["config"])

    out = subprocess.run(commandValidate, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Missing Keys"


def test_missing_keys2():

    copy_file("tests/testConfigData/missingKeysConfig2.json", paths["config"])

    out = subprocess.run(commandValidate, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Missing Keys"


def test_incorrect_path():

    copy_file("tests/testConfigData/incorrectPathConfig.json", paths["config"])

    out = subprocess.run(commandValidate, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Incorrect Path"


def test_incorrect_path2():

    copy_file("tests/testConfigData/incorrectPathConfig2.json", paths["config"])

    out = subprocess.run(commandValidate, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Incorrect Path"


def test_incorrect_path3():

    copy_file("tests/testConfigData/incorrectPathConfig3.json", paths["config"])

    out = subprocess.run(commandValidate, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Incorrect Path"


def test_incorrect_interval():

    copy_file("tests/testConfigData/incorrectInterval.json", paths["config"])

    out = subprocess.run(commandValidate, stdout=subprocess.PIPE)

    message = out.stdout.splitlines()[-1].decode("utf-8")

    assert message == "Error: Interval value not accepted"


# Do before and after tests


@pytest.fixture(autouse=True)
def before_and_after_test():
    clean_up(paths["config"])
    yield
    clean_up(paths["config"])
