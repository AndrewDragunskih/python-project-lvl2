"""Some description."""
from gendiff import change_status


def is_complex(some_data):
    """
    Check if data is dictionary.

    Args:
        some_data: data to check

    Returns:
        bool: data is a dictionary
    """
    return isinstance(some_data, dict)


def go_deeper(some_data):
    """
    Go deeper in complex value.

    Args:
        some_data: complex data

    Returns:
        list: difference
    """
    diff = []
    for some_key in some_data.keys():
        some_value = some_data[some_key]
        if is_complex(some_value):
            diff.append({
                'key': some_key,
                'status': change_status.NOT_CH,
                'value': go_deeper(some_value),
            })
        else:
            diff.append({
                'key': some_key,
                'status': change_status.NOT_CH,
                'value': some_value,
            })
    return diff


def parse_any_complex_data(some_key, first_data_value, second_data_value):
    """
    Parse data when one of data is complex.

    Args:
        some_key: current key
        first_data_value: first data to parse
        second_data_value: second data to parse

    Returns:
        list: difference
    """
    diff = []
    if is_complex(first_data_value):
        diff.append({
            'key': some_key,
            'status': change_status.UPD_FROM,
            'value': go_deeper(first_data_value),
        })
    else:
        diff.append({
            'key': some_key,
            'status': change_status.UPD_FROM,
            'value': first_data_value,
        })
    if is_complex(second_data_value):
        diff.append({
            'key': some_key,
            'status': change_status.UPD_TO,
            'value': go_deeper(second_data_value),
        })
    else:
        diff.append({
            'key': some_key,
            'status': change_status.UPD_TO,
            'value': second_data_value,
        })
    return diff


def parse_simple_data(some_key, first_data_value, second_data_value):
    """
    Parse data when data is simple.

    Args:
        some_key: current key
        first_data_value: first data to parse
        second_data_value: second data to parse

    Returns:
        list: difference
    """
    diff = []
    if first_data_value == second_data_value:
        diff.append({
            'key': some_key,
            'status': change_status.NOT_CH,
            'value': first_data_value,
        })
    else:
        diff.append({
            'key': some_key,
            'status': change_status.UPD_FROM,
            'value': first_data_value,
        })
        diff.append({
            'key': some_key,
            'status': change_status.UPD_TO,
            'value': second_data_value,
        })
    return diff


def parse_one_data(some_key, some_data, status, level):
    """
    Parse when key is in one data.

    Args:
        some_key: current key
        some_data: data to parse
        status: change status
        level: special flag to compare values

    Returns:
        list: difference
    """
    diff = []
    if is_complex(some_data[some_key]):
        diff.append({
            'key': some_key,
            'status': status if level == 1 else change_status.NOT_CH,
            'value': go_deeper(some_data[some_key]),
        })
    else:
        diff.append({
            'key': some_key,
            'status': status if level == 1 else change_status.NOT_CH,
            'value': some_data[some_key],
        })
    return diff


def parse_data(first_data_outer, second_data_outer):
    """
    Parse two data.

    Args:
        first_data_outer: first file to parse
        second_data_outer: second file to parse

    Returns:
        list: difference between files
    """
    def walk(first_data, second_data, level=1):
        diff = []
        for key in set(first_data.keys()) | set(second_data.keys()):
            if key in first_data.keys() and key not in second_data.keys():
                one_diff = parse_one_data(
                    key, first_data, change_status.RM, level,
                )
                diff.extend(one_diff)
            elif key in second_data.keys() and key not in first_data.keys():
                one_diff = parse_one_data(
                    key, second_data, change_status.ADD, level,
                )
                diff.extend(one_diff)
            elif is_complex(first_data[key]) and is_complex(second_data[key]):
                diff.append({
                    'key': key,
                    'status': change_status.NOT_CH,
                    'value': walk(first_data[key], second_data[key]),
                })
            elif is_complex(first_data[key]) or is_complex(second_data[key]):
                one_diff = parse_any_complex_data(
                    key, first_data[key], second_data[key],
                )
                diff.extend(one_diff)
            else:
                one_diff = parse_simple_data(
                    key, first_data[key], second_data[key],
                )
                diff.extend(one_diff)
        return diff
    return walk(first_data_outer, second_data_outer)
