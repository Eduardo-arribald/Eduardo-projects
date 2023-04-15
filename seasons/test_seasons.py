from seasons import get_minutes
import pytest

def main():
    test_true_values()
    #test_true_values_1999()

    test_false_values()
    test_false_values_2()
    test_false_values_3()

def test_true_values():
    #One year ago from today.
    assert get_minutes("2022-04-15") == "Five hundred twenty-five thousand, six hundred minutes"
    #Two years ago from today.
    assert get_minutes("2021-04-15") == "One million, fifty-one thousand, two hundred minutes"

"""
def test_true_values_1999():
    #Assuming today's date is January 1, 2000:
    assert get_minutes("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_minutes("1999-12-31") == "One thousand, four hundred forty minutes"
    assert get_minutes("1970-01-01") == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
"""

def test_false_values():
    with pytest.raises(SystemExit) as sample:
        get_minutes("January 1, 1999")
    assert sample.type == SystemExit
    assert sample.value.code == "Invalid date"


def test_false_values_2():
    with pytest.raises(SystemExit) as sample:
        get_minutes("Great album")
    assert sample.type == SystemExit
    assert sample.value.code == "Invalid date"

def test_false_values_3():
    with pytest.raises(SystemExit) as sample:
        get_minutes("hola, Tum Tum")
    assert sample.type == SystemExit
    assert sample.value.code == "Invalid date"


if __name__ == "__main__":
    main()
