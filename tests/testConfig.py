import pytest

import json
import os
import subprocess

commandSimple = 'python synchronize.py'
configPath = "./config.json"
defaultConfigPath = "./data/defaultConfig.json"

# Helpers

def clean_up():
    if os.path.exists(configPath):
        os.remove(configPath)

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



            
# Tests


def test_create_config_if_not_exist():
    # clean_up()  
    subprocess.run(commandSimple, shell=True)
    assert os.path.exists(configPath), f"File '{configPath}' does not exist"


def test_json_file_validity():
    assert is_valid_json(configPath), f"File '{configPath}' is not a valid JSON file"



def test_missing_keys():
    clean_up() 

    copy_file("tests/testData/missingKeysConfig.json", configPath)

    out = subprocess.run(['python', 'synchronize.py', 'throw'], 
                                       check=True, 
                                       stdout=subprocess.PIPE, )

    message = out.stdout.splitlines()[-1]

    assert message == 'Error: Missing Keys'

def test_more_keys2():
    clean_up() 

    copy_file("tests/testData/missingKeysConfig2.json", configPath)

    out = subprocess.run(['python', 'synchronize.py', 'throw'], 
                                       check=True, 
                                       stdout=subprocess.PIPE, )

    message = out.stdout.splitlines()[-1]

    assert message == 'Error: Missing Keys'

def test_incorrect_path():
    clean_up() 

    copy_file("tests/testData/incorrectPathConfig.json", configPath)

    out = subprocess.run(['python', 'synchronize.py', 'throw'], 
                                       check=True, 
                                       stdout=subprocess.PIPE, )

    message = out.stdout.splitlines()[-1]

    assert message == 'Error: Path does not exist'

def test_incorrect_path2():
    clean_up() 

    copy_file("tests/testData/incorrectPathConfig2.json", configPath)

    out = subprocess.run(['python', 'synchronize.py', 'throw'], 
                                       check=True, 
                                       stdout=subprocess.PIPE, )

    message = out.stdout.splitlines()[-1]

    assert message == 'Error: Path does not exist'

def test_incorrect_path3():
    clean_up() 

    copy_file("tests/testData/incorrectPathConfig3.json", configPath)

    out = subprocess.run(['python', 'synchronize.py', 'throw'], 
                                       check=True, 
                                       stdout=subprocess.PIPE, )

    message = out.stdout.splitlines()[-1]

    assert message == 'Error: Path does not exist'

def test_incorrect_interval():
    clean_up() 

    copy_file("tests/testData/incorrectPathConfig3.json", configPath)

    out = subprocess.run(['python', 'synchronize.py', 'throw'], 
                                       check=True, 
                                       stdout=subprocess.PIPE, )

    message = out.stdout.splitlines()[-1]

    assert message == 'Error: Interval value is not correct'

# Do before and after tests

@pytest.fixture(autouse=True)
def before_and_after_test():
    clean_up()
    yield
    clean_up()