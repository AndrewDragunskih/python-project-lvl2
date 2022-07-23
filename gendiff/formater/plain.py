"""Some description."""
from gendiff.build_diff import ADDED, NESTED, NOT_CHANGED, REMOVED, UPDATED


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
    if isinstance(some_data['old_value'], dict):
        old_value = '[complex value]'
    else:
        old_value = format_value(some_data['old_value'])
    if isinstance(some_data['new_value'], dict):
        new_value = '[complex value]'
    else:
        new_value = format_value(some_data['new_value'])

    return "Property '{0}' was updated. From {1} to {2}".format(
        current_path,
        old_value,
        new_value,
    )


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
        diff = '{0}[complex value]'.format(diff)
    else:
        diff = '{0}{1}'.format(diff, format_value(some_value))
    return diff


def value_is_removed(current_path):
    """
    Return formatted difference when the value was removed.

    Args:
        current_path : full path to the key of value

    Returns:
        str: formatted diff
    """
    return "Property '{0}' was removed".format(current_path)


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
        diff = value_is_updated(some_data, current_path)
    elif some_data['diff_type'] == ADDED:
        diff = value_is_added(some_data, current_path)
    elif some_data['diff_type'] == REMOVED:
        diff = value_is_removed(current_path)
    return diff


def plain(raw_data_outer):
    """
    Format difference in strings.

    Args:
        raw_data_outer: data from parser

    Returns:
        str: difference between files in str format
    """
    formatted_diff = []

    def walk(raw_data, full_path=''):
        raw_data_sorted = []
        raw_data_sorted.extend(sorted(
            raw_data, key=lambda key_name: key_name['key'],
        ))
        for some_data in raw_data_sorted:
            current_path = full_path + some_data['key']
            if some_data['diff_type'] == NESTED:
                walk(
                    some_data['children'],
                    '{0}.'.format(current_path),
                )
            elif some_data['diff_type'] != NOT_CHANGED:
                formatted_diff.append(value_is_changed(
                    some_data, current_path,
                ))
        return '\n'.join(formatted_diff)
    return walk(raw_data_outer)
