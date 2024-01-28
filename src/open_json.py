import json
import os

from URL import URL
from config import ROOT_DIR

OPERATION = os.path.join(ROOT_DIR, "operations.json")


def open_json_file():
    with open(OPERATION, encoding="UTF8") as file:
        operations = json.load(file)

    return operations
