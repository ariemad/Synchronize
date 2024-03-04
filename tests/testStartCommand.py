import pytest

import os
import subprocess

from src.paths import paths
from src.helpers import *

command = ["python", "synchronize.py", "start"]


def test_copy_test_case():
    copy_folder("tests/testStartCommandData/TestCase1", "./")

    assert os.path.exists("./source/"), f"Folder 'source' does exist"
    assert os.path.exists("./replica/"), f"Folder 'replica' does exist"


def test_calculate_md5():
    md5 = calculate_md5("tests/testStartCommandData/uniqueFiles/1.txt")

    assert md5 == "d1965bbe240fb008bce41d8b7ce96335", "Md5 Checksum does not match"


def test_get_all_files():
    copy_folder("tests/testStartCommandData/TestCase1", "./")

    files = get_all_files("./source")

    expected = [
        "./source/1.txt",
        "./source/a/2.txt",
        "./source/a/b/3.txt",
        "./source/c/4.txt",
        "./source/c/d/e/5.txt",
    ]

    assert sorted(files) == sorted(expected), "Files are not equal"


def test_get_all_files2():
    copy_folder("tests/testStartCommandData/TestCase1", "./")

    filesSource = get_all_files("./source/", relative_to="./source/")
    filesReplica = get_all_files("./replica/", relative_to="./replica/")

    assert filesSource == filesReplica, "Files are not equal"


def test_compare_folders():
    copy_folder("tests/testStartCommandData/TestCase1", "./")

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


# Same MD5, No folders


def test_sync_1():
    copy_folder("tests/testStartCommandData/TestCase2", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


def test_sync_2():
    copy_folder("tests/testStartCommandData/TestCase3", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


def test_sync_3():
    copy_folder("tests/testStartCommandData/TestCase4", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


def test_sync_4():
    copy_folder("tests/testStartCommandData/TestCase5", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


# Same MD5, With folders


def test_sync_5():
    copy_folder("tests/testStartCommandData/TestCase6", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


def test_sync_6():
    copy_folder("tests/testStartCommandData/TestCase7", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


def test_sync_7():
    copy_folder("tests/testStartCommandData/TestCase8", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


def test_sync_8():
    copy_folder("tests/testStartCommandData/TestCase9", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


# Different MD5


def test_sync_9():
    copy_folder("tests/testStartCommandData/TestCase10", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


def test_sync_10():
    copy_folder("tests/testStartCommandData/TestCase11", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


def test_sync_11():
    copy_folder("tests/testStartCommandData/TestCase12", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


def test_sync_12():
    copy_folder("tests/testStartCommandData/TestCase13", "./")

    if not os.path.exists("./source/"):
        os.makedirs("./source/")
    if not os.path.exists("./replica/"):
        os.makedirs("./replica/")

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
    )

    assert compare_folders("./source/", "./replica/"), "Folders are not equal"


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
