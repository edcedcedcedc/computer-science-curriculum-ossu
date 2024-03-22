from um import count


def test_ums():
    assert count("yummy") == 0
    assert count("um....um") == 2
    assert count("um um umum") == 2
    assert count("um.um um umum u.m") == 3
    assert count("Um") == 1
