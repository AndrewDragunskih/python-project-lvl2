import pytest
from gendiff.gendiff import parse_data


def test_exception_parse_data_wrong_type():
    with pytest.raises(ValueError) as exc:
        parse_data('test_string', 'jsn')
    assert str(exc.value) == 'Not supported format - "jsn"'
