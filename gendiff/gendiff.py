"""Some description."""
import json
import os

import yaml
from gendiff.build_diff import get_diff
from gendiff.formater.format_diff import format_diff_in_chosen_style
from yaml.loader import SafeLoader

JSON_TYPE = ['.json']
YAML_TYPE = ['.yaml', '.yml']


def parse_file(data_from_file, file_type):
    """
    Parse data in str format.

    Args:
        data_from_file: data to parse
        file_type: path to file

    Returns:
        data: parsed data
    """
    if file_type in JSON_TYPE:
        return json.loads(data_from_file)
    if file_type in YAML_TYPE:
        return yaml.loads(data_from_file, Loader=SafeLoader)


def get_data_from_file(file_path):
    """
    Get data from yaml, yaml or json file. Return data in str format.

    Args:
        file_path: path to file

    Returns:
        data_from_file: data from opened file
        file_type: type of opened file
    """
    with open(os.path.abspath(file_path), 'r') as opened_file:
        data_from_file = opened_file.read()
        file_type = os.path.splitext(file_path)[1]
    return data_from_file, file_type


def generate_diff(first_file_path, second_file_path, diff_format='stylish'):
    """
    Print difference between two files.

    Args:
        first_file_path: path to the first data
        second_file_path: path to the second data
        diff_format: return diff in this style

    Returns:
        str: formatted difference between files
    """
    first_data = parse_file(*get_data_from_file(first_file_path))
    second_data = parse_file(*get_data_from_file(second_file_path))
    raw_diff = get_diff(first_data, second_data)
    return format_diff_in_chosen_style(raw_diff, diff_format)
