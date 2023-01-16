from plates import is_valid

def main():
    test_valids()
    test_invalids()


def test_valids():
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True



def test_invalids():
    assert is_valid("CS05") == False
    assert is_valid("CS50P2") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("3") == False
    assert is_valid("OUTATIME") == False


if __name__ == "__main__":
    main()