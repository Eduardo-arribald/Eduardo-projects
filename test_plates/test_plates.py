from plates import is_valid

def main():
    test_valids()
    test_invalids()


def test_valids():
    assert value("ECTO88") == True
    assert value("NRVOUS") == True

def test_invalids():
    assert value("CS05") == False
    assert value("CS50P2") == False
    assert value("PI3.14") == False
    assert value("H") == False
    assert value("OUTATIME") == False


if __name__ == "__main__":
    main()