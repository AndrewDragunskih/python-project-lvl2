"""Some description."""
import json

from gendiff.formater.sort import sort_raw_data


def json_output(raw_data):
    """
    Format data in json.

    Args:
        raw_data: parsed data

    Returns:
        json: sorted diff in json format
    """
    return json.dumps(sort_raw_data(raw_data))
