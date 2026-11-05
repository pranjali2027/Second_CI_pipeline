import importlib

module = importlib.import_module("37_rotate_string")


def test_normal_rotation():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotation_by_one():
    assert module.rotate_string("hello", 1) == "ohell"


def test_rotation_by_full_length():
    assert module.rotate_string("python", 6) == "python"


def test_rotation_greater_than_length():
    assert module.rotate_string("abcd", 6) == "cdab"


def test_empty_string():
    assert module.rotate_string("", 3) == ""