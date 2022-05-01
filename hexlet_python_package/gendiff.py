"""Some description."""
import json
import os

def downcase_bool(value):
    if value is True or value is False:
        value = str(value)
        return value.lower()
    return value


def print_one_diff(key, value, arg):
    result = '  {} {}: {}\n'.format(arg, key, downcase_bool(value))
    return result


def print_two_diffs(key, value1, value2):
    result1 = print_one_diff(key, value1, '-')
    result2 = print_one_diff(key, value2, '+')
    return result1 + result2


def generate_diff(first_file_path, second_file_path):
    """Some desription."""
    first_file = json.load(open(os.path.abspath(first_file_path)))
    second_file = json.load(open(os.path.abspath(second_file_path)))
    first_file_keys = list(first_file.keys())
    second_file_keys = list(second_file.keys())
    unique_keys = list(set(first_file_keys + second_file_keys))
    unique_keys_sorted = sorted(unique_keys)
    result = '{\n'
    for key in unique_keys_sorted:
        if key in first_file_keys and key in second_file_keys:
           if first_file[key] == second_file[key]:
               result = result + print_one_diff(key, first_file[key],' ')
               continue
           else:
               result = result + print_two_diffs(key, first_file[key], second_file[key])
               continue
        if key in first_file_keys and not (key in second_file_keys):
           result = result + print_one_diff(key, first_file[key],'-')
           continue
        if not(key in first_file_keys) and key in second_file_keys:
           result = result + print_one_diff(key, second_file[key],'+')
           continue
    result = result + '}'
    return result
