from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("5/4") == ValueError
    assert convert("4/0") == ZeroDivisionError


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"

if __name__ == "__main__":
    main()