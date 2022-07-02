"""Some description."""
import json
import os

import yaml
from gendiff.formater.format_diff import format_diff_in_chosen_style
from gendiff.parser import parse_data
from yaml.loader import SafeLoader

JSON_TYPE = ['json']
YAML_TYPE = ['yaml', 'yml']


def parse_file(file_path, opened_file):
    """
    Parse data from yaml, yaml or json file.

    Args:
        file_path: path to file
        opened_file: file to parse

    Returns:
        data: parsed data
    """
    file_type = os.path.basename(file_path).split('.')[-1]
    if file_type in JSON_TYPE:
        return json.load(opened_file)
    if file_type in YAML_TYPE:
        return yaml.load(opened_file, Loader=SafeLoader)


def get_data_from_file(file_path):
    """
    Get data from yaml, yaml or json file.

    Args:
        file_path: path to file

    Returns:
        data: parsed data
    """
    with open(os.path.abspath(file_path), 'r') as read_file:
        return parse_file(file_path, read_file)


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
    first_data = get_data_from_file(first_file_path)
    second_data = get_data_from_file(second_file_path)
    raw_diff = parse_data(first_data, second_data)
    return format_diff_in_chosen_style(raw_diff, diff_format)
