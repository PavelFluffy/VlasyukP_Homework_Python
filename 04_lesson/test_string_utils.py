import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Gello", "Gello"),
    ("   Hel lo", "Hel lo"),
    ("  123asd", "123asd"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Hello  ", "Hello  "),
    ("123asd  ", "123asd  "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("Hello", "H", True),
    ("Hello", "T", False),
])
def test_contains_positive(input_str, input_sym, expected):
    assert string_utils.contains(input_str, input_sym) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("", "", True),
    ("", "123", False),
])
def test_contains_negative(input_str, input_sym, expected):
    assert string_utils.contains(input_str, input_sym) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("Hello", "o", "Hell"),
    ("Hello 123", "123", "Hello "),
    ("Hello", "l", "Heo"),
])
def test_delete_symbol_positive(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ("Hello", "", "Hello"),
    ("", "", ""),
    ("", "a", ""),
])
def test_delete_symbol_negative(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected
