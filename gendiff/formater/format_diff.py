"""Some description."""
from gendiff.formater.json import json_output
from gendiff.formater.plain import plain
from gendiff.formater.stylish import stylish

STYLISH_FORMAT = 'stylish'
PLAIN_FORMAT = 'plain'
JSON_FORMAT = 'json'


def format_diff_in_chosen_style(raw_diff, diff_format):
    """
    Format data in json.

    Args:
        raw_diff: parsed data
        diff_format: chosen format to output diff

    Returns:
        str: formatted diff
    """
    if diff_format == STYLISH_FORMAT:
        return stylish(raw_diff)
    elif diff_format == PLAIN_FORMAT:
        return plain(raw_diff)
    elif diff_format == JSON_FORMAT:
        return json_output(raw_diff)
