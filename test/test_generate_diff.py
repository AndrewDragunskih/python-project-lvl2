from hexlet_python_package.gendiff import generate_diff

def test_generate_diff_json():
    result_file = open('test/fixtures/result','r')
    result = result_file.read()
    result = result[:len(result)-1]
    assert generate_diff('test/fixtures/file1.json', 'test/fixtures/file2.json') == result
    result_file.close()

def test_generate_diff_yaml():
    result_file = open('test/fixtures/result','r')
    result = result_file.read()
    result = result[:len(result)-1]
    assert generate_diff('test/fixtures/file1.yaml', 'test/fixtures/file2.yml') == result
    result_file.close()
