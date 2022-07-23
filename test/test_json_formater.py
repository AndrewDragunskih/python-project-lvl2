from gendiff.build_diff import get_diff
from gendiff.formater.format_diff import (
    JSON_FORMAT,
    format_diff_in_chosen_style,
)
from gendiff.formater.sort import sort_raw_data
from gendiff.gendiff import get_data_from_file, parse_data


def test_format_diff_json():
    with open('test/fixtures/result_json_output', 'r') as result_file:
        res = result_file.read()
        res = res[:len(res) - 1]
    first_data = parse_data(*get_data_from_file('test/fixtures/file1.json'))
    second_data = parse_data(*get_data_from_file('test/fixtures/file2.json'))
    diff = get_diff(first_data, second_data)
    diff = sort_raw_data(diff)
    assert format_diff_in_chosen_style(diff, JSON_FORMAT) == res
