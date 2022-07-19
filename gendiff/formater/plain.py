"""Some description."""
from gendiff.build_diff import ADDED, NESTED, REMOVED, UPDATED
from gendiff.formater.sort import sort_raw_data


def format_value(some_value):
    """
    Format value to str.

    Args:
        some_value : value to format

    Returns:
        str: formatted value
    """
    if str(some_value) in {'True', 'False', '0'}:
        return str(some_value).lower()
    elif some_value is None:
        return 'null'
    return "'{0}'".format(some_value)


def value_is_updated(some_data, current_path):
    """
    Return formatted difference when the value was updated.

    Args:
        some_data : data that was updated
        current_path : full path to the key of value

    Returns:
        str: formatted diff
    """
    some_value = some_data['old_value']
    diff = "Property '{0}' was updated. ".format(current_path)
    if isinstance(some_value, dict):
        diff = "Property '{0}' was updated. From [complex value] to ".format(
            current_path,
        )
    else:
        diff = "Property '{0}' was updated. From {1} to ".format(
            current_path,
            format_value(some_value),
        )
    some_value = some_data['new_value']
    if isinstance(some_value, dict):
        diff = '{0}[complex value]\n'.format(diff)
    else:
        diff = '{0}{1}\n'.format(diff, format_value(some_value))
    return diff


def value_is_added(some_data, current_path):
    """
    Return formatted difference when the value was added.

    Args:
        some_data : data that was added
        current_path : full path to the key of value

    Returns:
        str: formatted diff
    """
    some_value = some_data['new_value']
    diff = "Property '{0}' was added with value: ".format(current_path)
    if isinstance(some_value, dict):
        diff = '{0}[complex value]\n'.format(diff)
    else:
        diff = '{0}{1}\n'.format(diff, format_value(some_value))
    return diff


def value_is_removed(current_path):
    """
    Return formatted difference when the value was removed.

    Args:
        current_path : full path to the key of value

    Returns:
        str: formatted diff
    """
    return "Property '{0}' was removed\n".format(current_path)


def value_is_changed(some_data, current_path):
    """
    Return formatted difference when the value was changed.

    Args:
        some_data : data that was changed
        current_path : full path to the key of value

    Returns:
        str: formatted diff
    """
    diff = ''
    if some_data['diff_type'] == UPDATED:
        diff += value_is_updated(some_data, current_path)
    elif some_data['diff_type'] == ADDED:
        diff += value_is_added(some_data, current_path)
    elif some_data['diff_type'] == REMOVED:
        diff += value_is_removed(current_path)
    return diff


def plain(raw_data_outer):
    """
    Format difference in strings.

    Args:
        raw_data_outer: data from parser

    Returns:
        str: difference between files in str format
    """
    def walk(raw_data, full_path='', formatted_diff=''):
        for some_data in raw_data:
            current_path = full_path + some_data['key']
            if some_data['diff_type'] == NESTED:
                formatted_diff = walk(
                    some_data['children'],
                    '{0}.'.format(current_path),
                    formatted_diff,
                )
            else:
                formatted_diff += value_is_changed(
                    some_data, current_path,
                )
        return formatted_diff
    formatted_diff = walk(sort_raw_data(raw_data_outer))
    return formatted_diff[:len(formatted_diff) - 1]
