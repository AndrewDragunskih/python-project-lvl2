from gendiff import generate_diff
from gendiff.formater.plain import plain

def test_generate_diff():
    result_file = open('test/fixtures/result_plain','r')
    result = result_file.read()
    result_file.close()
    data = generate_diff(
        'plain', 'test/fixtures/file1.json', 'test/fixtures/file2.json'
    )
    assert data == result
