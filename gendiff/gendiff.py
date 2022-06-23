"""Some description."""
import json
import os

import yaml
from gendiff.formater.json import json_output
from gendiff.formater.plain import plain
from gendiff.formater.stylish import stylish
from gendiff.parser import parse_files
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


def generate_diff(first_file_path, second_file_path, diff_format='stylish'):
    """
    Print difference between two files.

    Args:
        diff_format: return diff in this style
        first_file_path: path to first file
        second_file_path: path to second file

    Returns:
        str: formatted difference between files
    """
    first_file = open_file(first_file_path)
    second_file = open_file(second_file_path)
    raw_diff = parse_files(first_file, second_file)
    if diff_format == 'stylish':
        return stylish(raw_diff)
    elif diff_format == 'plain':
        return plain(raw_diff)
    elif diff_format == 'json':
        json_output(raw_diff, first_file_path, second_file_path)
