"""Some description."""
ADDED = 'added'
NESTED = 'nested'
NOT_CHANGED = 'not changed'
REMOVED = 'removed'
UPDATED = 'updated'


def is_complex(some_data):
    """
    Check if data is dictionary.

    Args:
        some_data: data to check

    Returns:
        bool: data is a dictionary
    """
    return isinstance(some_data, dict)


def get_one_complex_data_diff(some_key, first_data_value, second_data_value):
    """
    Parse data when one of data is complex.

    Args:
        some_key: current key
        first_data_value: first data to parse
        second_data_value: second data to parse

    Returns:
        list: difference
    """
    return {
        'key': some_key,
        'diff_type': UPDATED,
        'children': False,
        'old_value': first_data_value,
        'new_value': second_data_value,
    }


def get_both_simple_data_diff(some_key, first_data_value, second_data_value):
    """
    Parse data when data is simple.

    Args:
        some_key: current key
        first_data_value: first data to parse
        second_data_value: second data to parse

    Returns:
        list: difference
    """
    return {
        'key': some_key,
        'diff_type': NOT_CHANGED,
        'children': False,
        'old_value': first_data_value,
        'new_value': second_data_value,
    }


def get_one_data_diff(some_key, some_data, diff_type):
    """
    Get diff when key is in one data.

    Args:
        some_key: current key
        some_data: data to parse
        diff_type: change diff_type

    Returns:
        list: difference
    """
    return {
        'key': some_key,
        'diff_type': diff_type,
        'children': False,
        'old_value': some_data[some_key],
        'new_value': some_data[some_key],
    }


def get_diff(first_data_outer, second_data_outer):
    """
    Parse two data.

    Args:
        first_data_outer: first file to parse
        second_data_outer: second file to parse

    Returns:
        list: difference between files
    """
    def walk(first_data, second_data):
        diff = []
        for key in set(first_data.keys()) | set(second_data.keys()):
            if key in first_data and key not in second_data:
                one_diff = get_one_data_diff(
                    key, first_data, REMOVED,
                )
                diff.append(one_diff)
            elif key in second_data and key not in first_data:
                one_diff = get_one_data_diff(
                    key, second_data, ADDED,
                )
                diff.append(one_diff)
            elif is_complex(first_data[key]) and is_complex(second_data[key]):
                one_diff = walk(first_data[key], second_data[key])
                diff.append({
                    'key': key,
                    'diff_type': NESTED,
                    'children': one_diff,
                })
            elif first_data[key] != second_data[key]:
                one_diff = get_one_complex_data_diff(
                    key, first_data[key], second_data[key],
                )
                diff.append(one_diff)
            else:
                one_diff = get_both_simple_data_diff(
                    key, first_data[key], second_data[key],
                )
                diff.append(one_diff)
        return diff
    return walk(first_data_outer, second_data_outer)
