from twttr import shorten


def test_upper_string():
    assert shorten("TEST") == "TST"


def test_digit_string():
    assert shorten("CS50") == "CS50"


def test_punctuation():
    assert shorten("test.test") == "tst.tst"


def test_lower_string():
    assert shorten("test") == "tst"
