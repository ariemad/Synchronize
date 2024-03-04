import json
import uuid
import time

from src.paths import paths
from src.helpers import *
from src.log import log


def change_name_on_replica(checksums, path_with_dir, path_without_dir, logPath, print):
    md5 = calculate_md5(path_with_dir)
    randomFileName = str(uuid.uuid4())

    # Prev path split
    with_dir, base_filename = os.path.split(path_with_dir)
    without_dir, base_filename = os.path.split(path_without_dir)

    # New path creation
    new_filename_with_dir = os.path.join(with_dir, randomFileName)
    new_filename_without_dir = os.path.join(without_dir, randomFileName)

    if checksums[md5]["origin"] == path_with_dir:
        checksums[md5]["origin"] = new_filename_with_dir
        os.rename(path_with_dir, new_filename_with_dir)
        log("Rename", path_with_dir, new_filename_with_dir, logPath, print)

    if path_without_dir in checksums[md5]["replicaSet"]:
        checksums[md5]["replicaSet"].remove(path_without_dir)
        checksums[md5]["replicaSet"].add(new_filename_without_dir)
        if not os.path.exists(new_filename_with_dir):
            os.rename(path_with_dir, new_filename_with_dir)
            log("Rename", path_with_dir, new_filename_with_dir, logPath, print)

    return checksums


def synchronize(config, print):

    ##Checksums object creation

    checksums = dict()

    filesReplica = get_all_files(config["replica"], config["replica"])

    for file in filesReplica:
        filePath = os.path.join(config["replica"], file)
        md5 = calculate_md5(filePath)
        if not md5 in checksums:
            checksums[md5] = {
                "origin": filePath,
                "replicaSet": set(),
                "sourceSet": set(),
            }
        checksums[md5]["replicaSet"].add(file)

    sourceReplica = get_all_files(config["source"], config["source"])

    for file in sourceReplica:
        filePath = os.path.join(config["source"], file)
        md5 = calculate_md5(filePath)
        if not md5 in checksums:
            checksums[md5] = {
                "origin": filePath,
                "replicaSet": set(),
                "sourceSet": set(),
            }
        checksums[md5]["sourceSet"].add(file)

    ## File manipulation

    for md5 in checksums:
        # Remove common elements
        tempReplica = checksums[md5]["replicaSet"].copy()

        checksums[md5]["replicaSet"] -= checksums[md5]["sourceSet"]
        checksums[md5]["sourceSet"] -= tempReplica

        for file in checksums[md5]["sourceSet"]:
            filePath = os.path.join(config["replica"], file)
            if os.path.exists(filePath):
                checksums = change_name_on_replica(
                    checksums, filePath, file, config["log"], print
                )

            copy_file(checksums[md5]["origin"], filePath)
            log("Copy", checksums[md5]["origin"], filePath, config["log"], print)

        for file in checksums[md5]["replicaSet"]:
            filePath = os.path.join(config["replica"], file)
            os.remove(filePath)
            log("Remove", filePath, None, config["log"], print)


def start(repeat, print):
    with open(paths["config"], "r") as file:
        config = json.load(file)

    if repeat:
        while True:
            synchronize(config, print)
            time.sleep(config["interval"])
    else:
        synchronize(config, print)
