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
    return str(some_value)


def format_key(some_key):
    """
    Format key in case of changing value.

    Args:
        some_key : key to format

    Returns:
        str: formatted key
    """
    if str(some_key)[:2] == '-+':
        return '- {0}'.format(some_key[2:])
    elif str(some_key)[:2] == '+-':
        return '+ {0}'.format(some_key[2:])
    return str(some_key)


def stylish(raw_data_outer):
    """
    Format data in str.

    Args:
        raw_data_outer: first file to parse

    Returns:
        str: difference between files in str format
    """

    def walk(raw_data, level=1, res=''):
        for some_key, some_value in raw_data.items():
            indent = ' ' * (4 * level - 2)
            res += '{0}{1}: '.format(indent, format_key(some_key))
            if isinstance(some_value, dict) is False:
                res += '{0}\n'.format(format_value(some_value))
            else:
                res = '{0}{1}\n'.format(res, '{')
                res += walk(some_value, level + 1)
                res = '{0}{1}  {2}\n'.format(res, indent, '}')
        return res
    return '{{\n{0}}}'.format(walk(sort_raw_data(raw_data_outer)))
