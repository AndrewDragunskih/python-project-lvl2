from gendiff import generate_diff
from gendiff.formater.stylish import stylish

def test_generate_diff():
    result_file = open('test/fixtures/result_stylish','r')
    result = result_file.read()
    result = result[:len(result)-1]
    result_file.close()
    data = generate_diff(
        'stylish', 'test/fixtures/file1.json', 'test/fixtures/file2.json'
    )
    assert data == result
