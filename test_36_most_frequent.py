import importlib

module = importlib.import_module("36_most_frequent")


def test_normal_list():
    assert module.most_frequent([1, 2, 2, 3, 2]) == 2


def test_repeated_elements():
    assert module.most_frequent([5, 5, 3, 3, 5]) == 5


def test_single_element():
    assert module.most_frequent([7]) == 7


def test_empty_list():
    assert module.most_frequent([]) is None


def test_negative_numbers():
    assert module.most_frequent([-1, -2, -1, -3]) == -1