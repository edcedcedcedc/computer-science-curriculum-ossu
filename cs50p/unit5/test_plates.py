from plates import is_valid


def test_valid_cases():
    assert is_valid("CS50") == True
    assert is_valid("Hel23") == True


def test_at_least_two_letters():
    assert is_valid("ee") == True
    assert is_valid("22") == False


def test_interval():
    assert is_valid("testte") == True
    assert is_valid("testtea") == False


def test_point_comma_space():
    assert is_valid("test.") == False
    assert is_valid("test,") == False
    assert is_valid("test ") == False


def test_digit_zero():
    assert is_valid("cs050") == False


def test_digit_between():
    assert is_valid("cs50m") == False


def test_digit_between_zero():
    assert is_valid("cs050m") == False
