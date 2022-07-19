from gendiff import generate_diff


def test_generate_diff_stylish():
    with open('test/fixtures/result_stylish', 'r') as result_file:
        res = result_file.read()
        res = res[:len(res) - 1]
    diff = generate_diff(
        'test/fixtures/file1.json', 'test/fixtures/file2.json', 'stylish',
    )
    assert diff == res
