import os
from datetime import datetime

from src.paths import paths


def log(action, source, dest, logPath, printToConsole):
    if action not in ["Rename", "Copy", "Remove"]:
        raise ValueError("Parameter must be one of 'Rename', 'Copy', or 'Remove'")

    logPath = os.path.join(logPath, paths["defaultLogFile"])

    current_timestamp = datetime.now()
    formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

    logMessage = formatted_timestamp + action.rjust(10) + "".rjust(4) + source

    if action != "Remove":
        logMessage += "".rjust(4) + dest

    with open(logPath, "a") as file:
        file.write(logMessage + "\n")

    if printToConsole:
        print(logMessage)
