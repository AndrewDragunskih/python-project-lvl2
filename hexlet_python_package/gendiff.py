"""Some description."""
import json
import os

import yaml
from hexlet_python_package.parser import parse_files
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


def generate_diff(first_file_path, second_file_path):
    """
    Print difference between two files.

    Args:
        first_file_path: path to first file
        second_file_path: path to second file

    Returns:
        str: formatted difference between files
    """
    first_file = open_file(first_file_path)
    second_file = open_file(second_file_path)
    return parse_files(first_file, second_file)

if __name__ == '__main__':
    generate_diff()
