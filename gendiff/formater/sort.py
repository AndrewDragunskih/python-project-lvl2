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
        raw_data_sorted = {}
        all_keys = list(raw_data.keys())
        all_keys_sorted = sorted(all_keys, key=lambda key: key[2:])
        for some_key in all_keys_sorted:
            some_key_value = raw_data[some_key]
            if isinstance(some_key_value, dict):
                raw_data_sorted[some_key] = walk(some_key_value)
            else:
                raw_data_sorted[some_key] = some_key_value
        return raw_data_sorted
    return walk(raw_data_outer)
