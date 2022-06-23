"""Some description."""
import json
import os


def get_file_name(first_file, second_file):
    """
    Get name of the file with diff in json format.

    Args:
        first_file: first file path
        second_file: second_file path

    Returns:
        str: name of the file
    """
    return 'diff_{0}_and_{1}.json'.format(
        os.path.basename(first_file), os.path.basename(second_file),
    )


def json_output(raw_data, first_file, second_file):
    """
    Format data in json.

    Args:
        raw_data: parsed data
        first_file: first file path
        second_file: second_file path
    """
    file_name = get_file_name(first_file, second_file)
    with open(os.path.abspath(file_name), 'w') as write_file_json:
        json.dump(raw_data, write_file_json)
