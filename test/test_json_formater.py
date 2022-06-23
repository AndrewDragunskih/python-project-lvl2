import json
import os

from gendiff import generate_diff
from gendiff.formater.json import json_output
from gendiff.formater.sort import sort_raw_data

def test_generate_diff():
    with open('test/fixtures/result_json_output','r') as read_file_json:
            result_fixture = json.load(read_file_json)
    generate_diff('test/fixtures/file1.json', 'test/fixtures/file2.json', 'json')
    with open('diff_file1.json_and_file2.json.json','r') as read_file_json:
            result_json = json.load(read_file_json)
    print(type(result_json))
    assert result_json == result_fixture
