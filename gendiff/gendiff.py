"""Some description."""
import yaml
from gendiff.formater.format_diff import format_diff_in_chosen_style
from gendiff.parser import parse_files


def generate_diff(first_data, second_data, diff_format='stylish'):
    """
    Print difference between two files.

    Args:
        first_data: data from first file
        second_data: data from second file
        diff_format: return diff in this style

    Returns:
        str: formatted difference between files
    """
    raw_diff = parse_files(first_data, second_data)
    return format_diff_in_chosen_style(raw_diff, diff_format)
