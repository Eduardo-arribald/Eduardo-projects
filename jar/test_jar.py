from jar import Jar
import pytest

def test_init():
    jar_1 = Jar()
    assert str(jar_1.capacity) == 12
    assert str(jar_1.size) == 0

def test_str():
    jar_2 = Jar()
    assert str(jar_2) == ""
    jar_2.deposit(1)
    assert str(jar_2) == "🍪"
    jar_2.deposit(11)
    assert str(jar_2) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar_3 = Jar()
    with pytest.raises(ValueError):
        jar_3.deposit(14) == ValueError


def test_withdraw():
    jar_4 = Jar()
    with pytest.raises(ValueError):
        jar_4.withdraw(1) == ValueError

if __name__ == "__main__":
    main()