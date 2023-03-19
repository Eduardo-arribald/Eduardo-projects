from numb3rs import validate

def main():
    test_validate_true()
    test_validate_false()


def test_validate_true():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("250.0.0.0") == True


def test_validate_false():
    assert validate("cat") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False



if __name__ == "__main__":
    main()