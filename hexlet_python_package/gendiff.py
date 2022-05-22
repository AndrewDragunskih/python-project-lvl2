"""Some description."""
import json
import os

import yaml
from hexlet_python_package.parser import parse_files
from yaml.loader import SafeLoader


def downcase_bool(key_value):
    """
    Downcase True oe False to print.

    Args:
        key_value : value to downcase

    Returns:
        str: dowcased value
    """
    if key_value is True or key_value is False:
        key_value = str(key_value)
        return key_value.lower()
    return key_value


def format_diffs(diffs):
    """
    Format difference.

    Args:
        diffs: differnce

    Returns:
        str: formatted difference
    """
    formatted_diffs = ''
    for diff in diffs:
        downcased_bool = downcase_bool(diff[2])
        curr_diff = '  {0} {1}: {2}\n'.format(diff[0], diff[1], downcased_bool)
        formatted_diffs += curr_diff
    return '{{\n{0}}}'.format(formatted_diffs)


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
    diffs = parse_files(first_file, second_file)
    return format_diffs(diffs)
