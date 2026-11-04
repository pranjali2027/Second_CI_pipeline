import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating():
    assert module.first_non_repeating_char("swiss") == "w"


def test_no_non_repeating():
    assert module.first_non_repeating_char("aabbcc") is None


def test_empty_string():
    assert module.first_non_repeating_char("") is None


def test_simple_string():
    assert module.first_non_repeating_char("hello") == "h"


def test_single_character():
    assert module.first_non_repeating_char("a") == "a"