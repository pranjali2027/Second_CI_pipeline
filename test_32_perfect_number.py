
import importlib

module = importlib.import_module("32_perfect_number")

def test_perfect_number():
    assert module.is_perfect(6) is True

def test_another_perfect_number():
    assert module.is_perfect(28) is True

def test_not_perfect_number():
    assert module.is_perfect(10) is False

def test_zero():
    assert module.is_perfect(0) is False