"""Some description."""
from gendiff.formater.sort import sort_raw_data


def format_value(some_value):
    """
    Format value to str.

    Args:
        some_value : value to format

    Returns:
        str: formatted value
    """
    if some_value is True:
        return 'true'
    elif some_value is False:
        return 'false'
    elif some_value is None:
        return 'null'
    return "'{0}'".format(some_value)


def value_is_updated(sign, some_value, current_path):
    """
    Return formatted difference when the value was updated.

    Args:
        sign : type of value update
        some_value : vale that was updated
        current_path : full path to the key of value

    Returns:
        str: formatted diff
    """
    if sign == '-+':
        diff = "Property '{0}' was updated.".format(current_path)
        if isinstance(some_value, dict):
            diff = '{0} From [complex value] to'.format(diff)
        else:
            diff = '{0} From {1} to'.format(diff, format_value(some_value))
    else:
        if isinstance(some_value, dict):
            diff = ' [complex value]\n'
        else:
            diff = ' {0}\n'.format(format_value(some_value))
    return diff


def value_is_added(some_value, current_path):
    """
    Return formatted difference when the value was added.

    Args:
        some_value : vale that was updated
        current_path : full path to the key of value

    Returns:
        str: formatted diff
    """
    diff = "Property '{0}' was added with value:".format(current_path)
    if isinstance(some_value, dict):
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


def value_is_changed(sign, some_value, current_path):
    """
    Return formatted difference when the value was changed.

    Args:
        sign : type of value update
        some_value : vale that was updated
        current_path : full path to the key of value

    Returns:
        str: formatted diff
    """
    diff = ''
    if sign in {'-+', '+-'}:
        diff += value_is_updated(sign, some_value, current_path)
    elif sign == '+ ':
        diff += value_is_added(some_value, current_path)
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
        for some_key, some_value in raw_data.items():
            sign = some_key[:2]
            current_path = full_path + some_key[2:]
            if sign == '  ':
                if isinstance(some_value, dict):
                    formatted_diff = walk(
                        some_value, '{0}.'.format(current_path), formatted_diff,
                    )
            else:
                formatted_diff += value_is_changed(
                    sign, some_value, current_path,
                )
        return formatted_diff
    return walk(sort_raw_data(raw_data_outer))
