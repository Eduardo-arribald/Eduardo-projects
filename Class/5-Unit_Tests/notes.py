""" Unit Test

Is used when testing code.
Tests are made for returned values, not for printing or side effects.

> assert: a key function used to assert/claim that something is true.
If it is, nothing happens. But if itsn't true, it pop ups an error.
Error called "AssertionError".

>

- Modules:

> pytest: automates the testing of my code. Adapts some conventions
so I don't have to write some code parts by myself.
documentation: docs.pytest.org

"""

import pytest
from calculator import square
from hello import hello

#To run the tests in a better way and debug it, I can run in the prompt:
# pytest file_name.py
#And it will print the mistakes in the code. It only prints one mistake/passed per function.

def main():
    #test_square()
    #test_positives()
    #test_negatives()
    #test_zero()
    test_hello()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("3 squared was not 9")

    ns = [-3, -2, 0, 2, 3]

    print("Loop test:")

    for i in ns:
        try:
            assert square(i) == i*i
        except AssertionError:
            print(f"{i} squared was not {i*i}")


def test_positives():
    assert square(2) == 4
    assert square(3) == 9


def test_negatives():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

#Tests are made for returned values, not for printing or side effects.

def test_hello():
    assert hello("Eduardo") == "Hello, Eduardo"


if __name__=="__main__":
    main()

