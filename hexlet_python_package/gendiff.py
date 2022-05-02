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


def format_one_diff(key, key_value, arg):
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


def format_two_diffs(key, key_value1, key_value2):
    """
    Format difference with two strings.

    Args:
        key: key to print
        key_value1: value to print
        key_value2: value to print

    Returns:
        str: formatted difference
    """
    formatted_string = format_one_diff(key, key_value1, '-')
    formatted_string = formatted_string + format_one_diff(key, key_value2, '+')
    return formatted_string


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
    first_file_keys = list(first_file.keys())
    with open(os.path.abspath(second_file_path), 'r') as read_file2:
        second_file = json.load(read_file2)
    second_file_keys = list(second_file.keys())
    unique_keys_sorted = sorted(list(set(first_file_keys + second_file_keys)))
    diffs = '{\n'
    for key in unique_keys_sorted:
        if key in first_file_keys and key in second_file_keys:
            if first_file[key] == second_file[key]:
                diffs = diffs + format_one_diff(key, first_file[key], ' ')
                continue
            else:
                diffs = diffs + format_two_diffs(key, first_file[key], second_file[key])
                continue
        if key in first_file_keys and not (key in second_file_keys):
            diffs = diffs + format_one_diff(key, first_file[key], '-')
            continue
        if not (key in first_file_keys) and key in second_file_keys:
            diffs = diffs + format_one_diff(key, second_file[key], '+')
    diffs = '{0}\n}'.format(diffs)
    return diffs
