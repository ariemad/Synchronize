import json

from src.paths import paths
from src.helpers import *


def synchronize():
    checksums = dict()

    with open(paths["config"], "r") as file:
        config = json.load(file)

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

    for md5 in checksums:
        # Remove common elements
        tempReplica = checksums[md5]["replicaSet"].copy()

        checksums[md5]["replicaSet"] -= checksums[md5]["sourceSet"]
        checksums[md5]["sourceSet"] -= tempReplica

        # There must be a file renaming script here

        for file in checksums[md5]["sourceSet"]:
            filePath = os.path.join(config["replica"], file)
            copy_file(checksums[md5]["origin"], filePath)

        for file in checksums[md5]["replicaSet"]:
            filePath = os.path.join(config["replica"], file)
            os.remove(filePath)


def start():
    synchronize()
