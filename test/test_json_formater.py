from gendiff import generate_diff
from gendiff.open_files import open_file


def test_generate_diff_json():
    result_file = open('test/fixtures/result_json_output', 'r')
    result = result_file.read()
    result = result[:len(result) - 1]
    diff = generate_diff(
        open_file('test/fixtures/file1.json'),
        open_file('test/fixtures/file2.json'),
        'json',
    )
    assert diff == result
