from hexlet_python_package.gendiff import generate_diff
from hexlet_python_package.formater.stylish import stylish

def test_generate_diff():
    result_file = open('test/fixtures/result_stylish','r')
    result = result_file.read()
    result = result[:len(result)-1]
    result_file.close()
    print(result)
    raw_data = generate_diff('test/fixtures/file1.json', 'test/fixtures/file2.json')
    assert stylish(raw_data) == result
