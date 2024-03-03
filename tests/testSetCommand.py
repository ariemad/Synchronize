import pytest

import os
import subprocess

from src.paths import paths
from src.helpers import *

commandValidate = ["python", "synchronize.py", "validate"]

# Command only changes parameter without validating it.


def test_set_source():
    copy_file(paths["defaultConfig"], paths["config"])

    subprocess.run(
        ["python", "synchronize.py", "set", "--source", "./otherSource/"],
        stdout=subprocess.PIPE,
    )

    assert compare_json_files(
        paths["config"], "tests/testSetCommandData/changeSource.json"
    ), "Json files not match"


def test_set_replica():
    copy_file(paths["defaultConfig"], paths["config"])

    subprocess.run(
        ["python", "synchronize.py", "set", "--replica=./otherReplica/"],
        stdout=subprocess.PIPE,
    )

    assert compare_json_files(
        paths["config"], "tests/testSetCommandData/changeReplica.json"
    ), "Json files not match"


def test_set_logs():
    copy_file(paths["defaultConfig"], paths["config"])

    subprocess.run(
        ["python", "synchronize.py", "set", "--log=./logsOther/"],
        stdout=subprocess.PIPE,
    )

    assert compare_json_files(
        paths["config"], "tests/testSetCommandData/changeLogs.json"
    ), "Json files not match"


def test_set_interval():
    copy_file(paths["defaultConfig"], paths["config"])

    subprocess.run(
        ["python", "synchronize.py", "set", "--interval=12345"],
        stdout=subprocess.PIPE,
    )

    assert compare_json_files(
        paths["config"], "tests/testSetCommandData/changeInterval.json"
    ), "Json files not match"


def test_set_all():
    copy_file(paths["defaultConfig"], paths["config"])

    subprocess.run(
        [
            "python",
            "synchronize.py",
            "set",
            "--source=./otherSource/",
            "--replica=./otherReplica/",
            "--log=./logsOther/",
            "--interval=12345",
        ],
        stdout=subprocess.PIPE,
    )

    assert compare_json_files(
        paths["config"], "tests/testSetCommandData/changeAll.json"
    ), "Json files not match"


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
