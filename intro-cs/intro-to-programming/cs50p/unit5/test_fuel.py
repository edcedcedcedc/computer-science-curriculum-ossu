from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("4/4") == 100


def test_value_error():
    with pytest.raises(ValueError):
        assert convert("5/4")


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        assert convert("5/0")


def test_f():
    assert gauge(99) == "F"


def test_e():
    assert gauge(1) == "E"


def test_percent():
    assert gauge(50) == "50%"
