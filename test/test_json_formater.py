import os

from gendiff import generate_diff
from gendiff.formater.json import json_output
from gendiff.formater.sort import sort_raw_data

def test_generate_diff():
    result_file = open('test/fixtures/result_json_output','r')
    result_fixture = result_file.read()
    result_fixture = result_fixture[:len(result_fixture)-1]
    result_file.close()
    raw_data = generate_diff('test/fixtures/file1.json', 'test/fixtures/file2.json')
    json_output(sort_raw_data(raw_data), 'test/fixtures/file1.json', 'test/fixtures/file2.json')
    result_file = open(os.path.abspath('diff_file1.json_and_file2.json.json'),'r')
    result_json = result_file.read()
    result_file.close()
    assert result_json == result_fixture
