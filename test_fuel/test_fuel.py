from fuel import convert, gauge

def main():
    test_valids()
    test_invalids()


def test_valids():
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True


if __name__ == "__main__":
    main()