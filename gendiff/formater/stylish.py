"""Some description."""
from gendiff.formater.sort import sort_raw_data

NOT_CHANGED = 'not changed'
UPDATED = 'updated'
ADDED = 'added'
REMOVED = 'removed'


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
    return str(some_value)


def format_status(status):
    """
    Format status to output is stylish format.

    Args:
        status : key status

    Returns:
        str: formatted key
    """
    status_base = {
        NOT_CHANGED: '  ',
        ADDED: '+ ',
        REMOVED: '- ',
        UPDATED: '',
    }
    return status_base[status]


def format_dict(raw_data, level=1):
    """
    Format dictionary (complex value) is stylish format.

    Args:
        raw_data : dictionary to format
        level : to define indent

    Returns:
        str: formatted key
    """
    res = ''
    for key in raw_data.keys():
        indent = ' ' * (4 * level)
        if isinstance(raw_data, dict) and isinstance(raw_data[key], dict):
            res += '{0}{1}: {{\n{2}{0}}}\n'.format(
                indent, key, format_dict(raw_data[key], level + 1),
            )
        elif isinstance(raw_data, dict):
            res += '{0}{1}: {2}\n'.format(indent, key, raw_data[key])
        else:
            res += '{0}{1}: {2}'.format(indent, key, raw_data[key])
    return res


def format_tuple(raw_data, level=1):
    """
    Format tuple (changed values) is stylish format.

    Args:
        raw_data : dictionary to format
        level : to define indent

    Returns:
        str: formatted key
    """
    res = ''
    indent = ' ' * (4 * level)
    if isinstance(raw_data, dict):
        res += '{{\n{0}{1}}}\n'.format(format_dict(raw_data, level + 1), indent)
    else:
        res += '{0}\n'.format(format_value(raw_data))
    return res


def stylish(raw_data_outer):
    """
    Format data in str.

    Args:
        raw_data_outer: first file to parse

    Returns:
        str: difference between files in str format
    """
    def walk(raw_data, level=1, res=''):
        for some_data in raw_data:
            indent = ' ' * (4 * level - 2)
            if isinstance(some_data['value'], dict):
                res += '{0}{1}{2}: {{\n{3}{0}  }}\n'.format(
                    indent,
                    format_status(some_data['status']),
                    some_data['key'],
                    format_dict(some_data['value'], level + 1),
                )
            elif isinstance(some_data['value'], tuple):
                res += '{0}{1}{2}: {3}'.format(
                    indent,
                    format_status(REMOVED),
                    some_data['key'],
                    format_tuple(
                        some_data['value'][0],
                        level,
                    ),
                )
                res += '{0}{1}{2}: {3}'.format(
                    indent,
                    format_status(ADDED),
                    some_data['key'],
                    format_tuple(
                        some_data['value'][1],
                        level,
                    ),
                )
            elif isinstance(some_data['value'], list) is False:
                res += '{0}{1}{2}: {3}\n'.format(
                    indent,
                    format_status(some_data['status']),
                    some_data['key'],
                    format_value(some_data['value']),
                )
            else:
                res += '{0}{1}{2}: {{\n{3}{0}  }}\n'.format(
                    indent,
                    format_status(some_data['status']),
                    some_data['key'],
                    walk(some_data['value'], level + 1),
                )
        return res
    return '{{\n{0}}}'.format(walk(sort_raw_data(raw_data_outer)))
