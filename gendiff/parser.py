"""Some description."""


def go_deeper(some_data):
    """
    Go deeper in complex value.

    Args:
        some_data: somethin

    Returns:
        list: difference
    """
    diff = []
    for some_key in some_data.keys():
        some_value = some_data[some_key]
        if isinstance(some_value, dict):
            diff.append({
                'key': some_key,
                'status': 'not changed',
                'value': go_deeper(some_value),
            })
        else:
            diff.append({
                'key': some_key,
                'status': 'not changed',
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
    if isinstance(first_data_value, dict):
        diff.append({
            'key': some_key,
            'status': 'upd from',
            'value': go_deeper(first_data_value),
        })
    else:
        diff.append({
            'key': some_key,
            'status': 'upd from',
            'value': first_data_value,
        })
    if isinstance(second_data_value, dict):
        diff.append({
            'key': some_key,
            'status': 'upd to',
            'value': go_deeper(second_data_value),
        })
    else:
        diff.append({
            'key': some_key,
            'status': 'upd to',
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
            'status': 'not changed',
            'value': first_data_value,
        })
    else:
        diff.append({
            'key': some_key,
            'status': 'upd from',
            'value': first_data_value,
        })
        diff.append({
            'key': some_key,
            'status': 'upd to',
            'value': second_data_value,
        })
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
        list: difference
    """
    diff = []
    if some_key in first_data.keys():
        some_data = first_data
        status = 'removed'
    else:
        some_data = second_data
        status = 'added'
    if isinstance(some_data[some_key], dict):
        diff.append({
            'key': some_key,
            'status': status if level == 1 else 'not changed',
            'value': go_deeper(some_data[some_key]),
        })
    else:
        diff.append({
            'key': some_key,
            'status': status if level == 1 else 'not changed',
            'value': some_data[some_key],
        })
    return diff


def parse_files(first_data_outer, second_data_outer):
    """
    Parse two files.

    Args:
        first_data_outer: first file to parse
        second_data_outer: second file to parse

    Returns:
        list: difference between files
    """
    def walk(first_data, second_data, level=1):
        diff = []
        for key in set(first_data.keys()) | set(second_data.keys()):
            if key in first_data.keys() and key in second_data.keys():
                is_first_data_comlpex = isinstance(first_data[key], dict)
                is_second_data_complex = isinstance(second_data[key], dict)
                if is_first_data_comlpex and is_second_data_complex:
                    diff.append({
                        'key': key,
                        'status': 'not changed',
                        'value': walk(first_data[key], second_data[key]),
                    })
                elif is_first_data_comlpex or is_second_data_complex:
                    one_diff = parse_any_complex_data(
                        key, first_data[key], second_data[key],
                    )
                    diff.extend(one_diff)
                else:
                    one_diff = parse_simple_data(
                        key, first_data[key], second_data[key],
                    )
                    diff.extend(one_diff)
            else:
                one_diff = parse_one_data(
                    key, first_data, second_data, level,
                )
                diff.extend(one_diff)
        return diff
    return walk(first_data_outer, second_data_outer)
