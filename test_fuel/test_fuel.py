from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_errors_1()
    test_errors_2()
    test_gauge()


def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_errors_1():
    with pytest.raises(ValueError):
        convert("5/4") == ValueError


def test_errors_2():
    with pytest.raises(ZeroDivisionError):
        convert("9:60 AM to 5:60 PM") == ZeroDivisionError


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"


if __name__ == "__main__":
    main()