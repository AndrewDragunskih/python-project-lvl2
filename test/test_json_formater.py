from gendiff import generate_diff


def test_generate_diff():
    result_file = open('test/fixtures/result_json_output', 'r')
    result_fixture = result_file.read()
    result_fixture = result_fixture[:len(result_fixture) - 1]
    diff = generate_diff(
        'test/fixtures/file1.json', 'test/fixtures/file2.json', 'json',
    )
    assert diff == result_fixture
