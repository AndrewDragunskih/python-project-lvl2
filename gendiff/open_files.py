"""Some description."""
import json
import os

import yaml
from yaml.loader import SafeLoader


def open_file(file_path):
    """
    Open .json or .yaml files.

    Args:
        file_path: path to file

    Returns:
        file: opened file
    """
    if file_path[-4:] == 'json':
        with open(os.path.abspath(file_path), 'r') as read_file_json:
            opened_file = json.load(read_file_json)
    if file_path[-4:] == 'yaml' or file_path[-3:] == 'yml':
        with open(os.path.abspath(file_path), 'r') as read_file_yaml:
            opened_file = yaml.load(read_file_yaml, Loader=SafeLoader)
    return opened_file
