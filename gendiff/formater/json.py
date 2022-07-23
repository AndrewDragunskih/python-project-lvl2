"""Some description."""
import json


def json_output(raw_data):
    """
    Format data in json.

    Args:
        raw_data: parsed data

    Returns:
        json: sorted diff in json format
    """
    return json.dumps(raw_data, indent=2)
