from numb3rs import validate



def test_not_numeric():
    assert validate("cat") == False

def test_4bytes_all_in_range():
    assert validate("255.255.255.255") == True

def test_1byte_out_of_range():
    assert validate("255.259.257.258") == False



