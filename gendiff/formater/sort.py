"""Some description."""


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
            if some_data['children']:
                some_data['old_value'] = walk(some_data['old_value'])
                some_data['new_value'] = walk(some_data['new_value'])
        return raw_data_sorted
    return walk(raw_data_outer)
