"""Some description."""
import json
import os


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


def output_diff(arg, key, key_value):
    """
    Format difference with one string.

    Args:
        key: key to print
        key_value: value to print
        arg: argument of difference

    Returns:
        str: formatted difference
    """
    downcased_key_value = downcase_bool(key_value)
    return '  {0} {1}: {2}\n'.format(arg, key, downcased_key_value)


def generate_diff(first_file_path, second_file_path):
    """
    Print difference between two files.

    Args:
        first_file_path: path to first file
        second_file_path: path to second file

    Returns:
        str: formatted difference between files
    """
    with open(os.path.abspath(first_file_path), 'r') as read_file1:
        first_file = json.load(read_file1)
    with open(os.path.abspath(second_file_path), 'r') as read_file2:
        second_file = json.load(read_file2)
    unique_keys = set(first_file.keys()) | set(second_file.keys())
    unique_keys = list(unique_keys)
    unique_keys.sort()
    first_file_keys = set(first_file.keys()) - set(second_file.keys())
    second_file_keys = set(second_file.keys()) - set(first_file.keys())
    both_file_keys = set(first_file.keys()) & set(second_file.keys())
    diff = ''
    for key in unique_keys:
        if key in first_file_keys:
            diff = diff + output_diff('-', key, first_file[key])
        elif key in second_file_keys:
            diff = diff + output_diff('+', key, second_file[key])
        elif key in both_file_keys and first_file[key] == second_file[key]:
            diff = diff + output_diff(' ', key, second_file[key])
        else:
            diff = diff + output_diff('-', key, first_file[key])
            diff = diff + output_diff('+', key, second_file[key])
    return '{{\n{0}}}'.format(diff)
