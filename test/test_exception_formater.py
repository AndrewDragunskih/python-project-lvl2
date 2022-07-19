import pytest
from gendiff.formater.format_diff import format_diff_in_chosen_style


def test_exception_formater_wrong_type():
    with pytest.raises(ValueError) as exc:
        format_diff_in_chosen_style({'test_data': 'test_data'}, 'line_format')
    assert str(exc.value) == 'Not supported formater type - "line_format"'
