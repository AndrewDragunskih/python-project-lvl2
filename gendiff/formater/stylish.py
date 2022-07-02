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
        change_status.NOT_CH: '  ',
        change_status.UPD_FROM: '- ',
        change_status.UPD_TO: '+ ',
        change_status.ADD: '+ ',
        change_status.RM: '- ',
    }
    return status_base[status]


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
            res += '{0}{1}{2}: '.format(
                indent, format_status(some_data['status']), some_data['key'],
            )
            if isinstance(some_data['value'], list) is False:
                res += '{0}\n'.format(format_value(some_data['value']))
            else:
                res = '{0}{1}\n'.format(res, '{')
                res += walk(some_data['value'], level + 1)
                res = '{0}{1}  {2}\n'.format(res, indent, '}')
        return res
    return '{{\n{0}}}'.format(walk(sort_raw_data(raw_data_outer)))
