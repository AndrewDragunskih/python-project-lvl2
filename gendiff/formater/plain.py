"""Some description."""
from gendiff import change_status
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
    if some_data['status'] == change_status.UPD_FROM:
        diff = "Property '{0}' was updated.".format(current_path)
        if isinstance(some_data['value'], list):
            diff = '{0} From [complex value] to'.format(diff)
        else:
            diff = '{0} From {1} to'.format(
                diff, format_value(some_data['value']),
            )
    else:
        if isinstance(some_data['value'], list):
            diff = ' [complex value]\n'
        else:
            diff = ' {0}\n'.format(format_value(some_data['value']))
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
    some_value = some_data['value']
    diff = "Property '{0}' was added with value:".format(current_path)
    if isinstance(some_value, list):
        diff = '{0} [complex value]\n'.format(diff)
    else:
        diff = '{0} {1}\n'.format(diff, format_value(some_value))
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
    if some_data['status'] in {change_status.UPD_TO, change_status.UPD_FROM}:
        diff += value_is_updated(some_data, current_path)
    elif some_data['status'] == change_status.ADD:
        diff += value_is_added(some_data, current_path)
    else:
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
            if some_data['status'] == change_status.NOT_CH:
                if isinstance(some_data['value'], list):
                    formatted_diff = walk(
                        some_data['value'],
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
