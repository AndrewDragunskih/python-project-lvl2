"""Some description."""
from itertools import compress


def is_value_complex(value_to_check):
    """
    Is value a dictionary.

    Args:
        value_to_check: first data to check

    Returns:
        boolean: list of value(s) complexity
    """
    return isinstance(value_to_check, dict)


def is_data_has_key(key_to_find, first_data, second_data):
    """
    Define data contains the key.

    Args:
        key_to_find: key to find in data
        first_data: first data that may contain the key
        second_data: second data that may contain the key

    Returns:
        list: list of data that contian the key
    """
    if key_to_find in first_data.keys() and key_to_find in second_data.keys():
        return [True, True]
    elif key_to_find in first_data.keys():
        return [True, False]
    return [False, True]


def go_deeper(some_data):
    """
    Go deeper in complex value.

    Args:
        some_data: somethin

    Returns:
        dict: difference
    """
    diff = {}
    for some_key in set(some_data.keys()):
        some_value = some_data[some_key]
        new_key = '  {0}'.format(some_key)
        if is_value_complex(some_value):
            diff[new_key] = go_deeper(some_value)
        else:
            diff[new_key] = some_data[some_key]
    return diff


def parse_any_complex_data(some_key, first_data_value, second_data_value):
    """
    Parse data when one of data is complex.

    Args:
        some_key: current key
        first_data_value: first data to parse
        second_data_value: second data to parse

    Returns:
        dict: difference
    """
    diff = {}
    diff_sign = '-+'
    if is_value_complex(first_data_value):
        diff[diff_sign + some_key] = go_deeper(first_data_value)
    else:
        diff[diff_sign + some_key] = first_data_value
    diff_sign = '+-'
    if is_value_complex(second_data_value):
        diff[diff_sign + some_key] = go_deeper(second_data_value)
    else:
        diff[diff_sign + some_key] = second_data_value
    return diff


def parse_simple_data(some_key, first_data_value, second_data_value):
    """
    Parse data when data is simple.

    Args:
        some_key: current key
        first_data_value: first data to parse
        second_data_value: second data to parse

    Returns:
        dict: difference
    """
    diff = {}
    if first_data_value == second_data_value:
        diff['  {0}'.format(some_key)] = first_data_value
    else:
        diff_sign = '-+'
        diff[diff_sign + some_key] = first_data_value
        diff_sign = '+-'
        diff[diff_sign + some_key] = second_data_value
    return diff


def parse_one_data(some_key, first_data, second_data, level):
    """
    Parse when key is in one data.

    Args:
        some_key: current key
        first_data: first data to parse
        second_data: second data to parse
        level: special flag to compare values

    Returns:
        dict: difference
    """
    diff = {}
    data_has_key = is_data_has_key(some_key, first_data, second_data)
    some_data, = list(compress((first_data, second_data), data_has_key))
    diff_sign, = list(compress(('- ', '+ '), data_has_key))
    new_key = diff_sign + some_key if level == 1 else '  {0}'.format(some_key)
    if is_value_complex(some_data[some_key]):
        diff[new_key] = go_deeper(some_data[some_key])
    else:
        diff[new_key] = some_data[some_key]
    return diff


def parse_files(first_data_outer, second_data_outer):
    """
    Parse two files.

    Args:
        first_data_outer: first file to parse
        second_data_outer: second file to parse

    Returns:
        dict: difference between files
    """
    def walk(first_data, second_data, level=1):
        diff = {}
        for some_key in set(first_data.keys()) | set(second_data.keys()):
            if all(is_data_has_key(some_key, first_data, second_data)):
                first_data_value = first_data[some_key]
                second_data_value = second_data[some_key]
                value_is_comlpex = (
                    is_value_complex(first_data_value),
                    is_value_complex(second_data_value),
                )
                if all(value_is_comlpex):
                    diff['  {0}'.format(some_key)] = walk(
                        first_data_value, second_data_value,
                    )
                elif any(value_is_comlpex):
                    diff = {**diff, **parse_any_complex_data(
                        some_key, first_data_value, second_data_value,
                    )}
                else:
                    diff = {**diff, **parse_simple_data(
                        some_key, first_data_value, second_data_value,
                    )}
            else:
                diff = {**diff, **parse_one_data(
                    some_key, first_data, second_data, level,
                )}
        return diff
    return walk(first_data_outer, second_data_outer)
