"""Some description."""
from gendiff.build_diff import NESTED


def sort_raw_data(raw_data_outer):
    """
    Sort data in stylish formater.

    Args:
        raw_data_outer : not formatted data

    Returns:
        dict: formatted data
    """

    def walk(raw_data):
        raw_data_sorted = []
        raw_data_sorted.extend(sorted(
            raw_data, key=lambda key_name: key_name['key'],
        ))
        for some_data in raw_data:
            if some_data['diff_type'] == NESTED:
                some_data['children'] = walk(some_data['children'])
        return raw_data_sorted
    return walk(raw_data_outer)
