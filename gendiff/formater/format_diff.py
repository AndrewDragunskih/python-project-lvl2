"""Some description."""
from gendiff.formater.json import json_output
from gendiff.formater.plain import plain
from gendiff.formater.stylish import stylish


def format_diff_in_chosen_style(raw_diff, diff_format):
    """
    Format data in json.

    Args:
        raw_diff: parsed data
        diff_format: chosen format to output diff

    Returns:
        str: formatted diff
    """
    if diff_format == 'stylish':
        return stylish(raw_diff)
    elif diff_format == 'plain':
        return plain(raw_diff)
    elif diff_format == 'json':
        return json_output(raw_diff)
