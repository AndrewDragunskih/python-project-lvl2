"""Some description."""


def parse_files(first_file, second_file):
    """
    Parse two files.

    Args:
        first_file: first file to parse
        second_file: second file to parse

    Returns:
        list: difference between files
    """
    unique_keys = set(first_file.keys()) | set(second_file.keys())
    unique_keys = list(unique_keys)
    unique_keys.sort()
    first_file_keys = set(first_file.keys()) - set(second_file.keys())
    second_file_keys = set(second_file.keys()) - set(first_file.keys())
    both_file_keys = set(first_file.keys()) & set(second_file.keys())
    diff = []
    for key in unique_keys:
        if key in first_file_keys:
            diff.append(['-', key, first_file[key]])
        elif key in second_file_keys:
            diff.append(['+', key, second_file[key]])
        elif key in both_file_keys and first_file[key] == second_file[key]:
            diff.append([' ', key, second_file[key]])
        else:
            diff.append(['-', key, first_file[key]])
            diff.append(['+', key, second_file[key]])
    return diff
