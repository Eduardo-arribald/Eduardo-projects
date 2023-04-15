from jar import convert
import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert str(jar.capacity) == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar.deposit(14)


def test_withdraw():
    jar = Jar()
    jar.withdraw(1)
    assert str(jar) ==

if __name__ == "__main__":
    main()