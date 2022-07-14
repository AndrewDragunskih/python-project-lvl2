"""Some description."""
from gendiff.build_diff import ADDED, NOT_CHANGED, REMOVED, UPDATED
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


def format_one_data(raw_data_outer, level_outer=1):
    """
    Format dictionary (complex value) is stylish format.

    Args:
        raw_data_outer : dictionary to format
        level_outer : to define indent

    Returns:
        str: formatted key
    """
    def _inner(raw_data, level=1):
        res = ''
        for key in raw_data.keys():
            indent = ' ' * (4 * level)
            if isinstance(raw_data[key], dict):
                res += '\n{0}{1}: {{{2}\n{0}}}'.format(
                    indent, key, _inner(raw_data[key], level + 1),
                )
            else:
                res += '\n{0}{1}: {2}'.format(indent, key, raw_data[key])
        return res
    if isinstance(raw_data_outer, dict):
        indent_outer = ' ' * (4 * (level_outer - 1))
        return '{{{0}\n{1}}}'.format(
            _inner(raw_data_outer, level_outer),
            indent_outer,
        )
    return format_value(raw_data_outer)


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
            if some_data['children']:
                res += '{0}{1}{2}: {{\n{3}{0}  }}\n'.format(
                    indent,
                    format_status(some_data['status']),
                    some_data['key'],
                    walk(some_data['old_value'], level + 1),
                )
            elif some_data['status'] == UPDATED:
                res += '{0}{1}{2}: {3}\n'.format(
                    indent,
                    format_status(REMOVED),
                    some_data['key'],
                    format_one_data(some_data['old_value'], level + 1),
                )
                res += '{0}{1}{2}: {3}\n'.format(
                    indent,
                    format_status(ADDED),
                    some_data['key'],
                    format_one_data(some_data['new_value'], level + 1),
                )
            elif some_data['status'] == ADDED:
                res += '{0}{1}{2}: {3}\n'.format(
                    indent,
                    format_status(ADDED),
                    some_data['key'],
                    format_one_data(some_data['new_value'], level + 1),
                )
            else:
                res += '{0}{1}{2}: {3}\n'.format(
                    indent,
                    format_status(some_data['status']),
                    some_data['key'],
                    format_one_data(some_data['old_value'], level + 1),
                )
        return res
    return '{{\n{0}}}'.format(walk(sort_raw_data(raw_data_outer)))
