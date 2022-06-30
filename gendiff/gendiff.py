"""Some description."""
import os

from gendiff.formater.format_diff import format_diff_in_chosen_style
from gendiff.open_files import open_file
from gendiff.parser import parse_files


def generate_diff(first_data_path, second_data_path, diff_format='stylish'):
    """
    Print difference between two files.

    Args:
        first_data_path: path to the first data
        second_data_path: path to the second data
        diff_format: return diff in this style

    Returns:
        str: formatted difference between files
    """
    if os.path.isfile(first_data_path) and os.path.isfile(second_data_path):
        first_data = open_file(first_data_path)
        second_data = open_file(second_data_path)
    else:
        first_data = first_data_path
        second_data = second_data_path
    raw_diff = parse_files(first_data, second_data)
    return format_diff_in_chosen_style(raw_diff, diff_format)
