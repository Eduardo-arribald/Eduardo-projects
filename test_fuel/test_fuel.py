from fuel import convert, gauge

def main():
    test_valids()
    test_invalids()


def test_convert():
    assert convert("ECTO88") == True
    assert convert("NRVOUS") == True

def test_gauge():
    assert gauge("ECTO88") == True
    assert gauge("NRVOUS") == True


if __name__ == "__main__":
    main()