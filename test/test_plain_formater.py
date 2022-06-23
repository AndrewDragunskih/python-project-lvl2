from gendiff import generate_diff
from gendiff.formater.plain import plain

def test_generate_diff():
    result_file = open('test/fixtures/result_plain','r')
    result = result_file.read()
    result_file.close()
    raw_data = generate_diff('test/fixtures/file1.json', 'test/fixtures/file2.json')
    assert plain(raw_data) == result
