from gendiff import generate_diff
from gendiff.open_files import open_file


def test_generate_diff_plain():
    result_file = open('test/fixtures/result_plain', 'r')
    result = result_file.read()
    result = result[:len(result) - 1]
    result_file.close()
    diff = generate_diff(
        open_file('test/fixtures/file1.json'),
        open_file('test/fixtures/file2.json'),
        'plain',
    )
    assert diff == result
