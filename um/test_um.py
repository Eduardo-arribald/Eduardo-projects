from um import count
import pytest

#I got this correct
#x = "um?" # 1
#x_1 = "yummy" # 0
#x_2 = "Um" # 1
#I just need these too.
#x_3 = "hola tum, asdasd" # 0
#x_4 = "hola um, asdasd" # 1
#x_5 = "Um, thanks, um..." #2
#x_6 = "Um, thanks for the album." #1


def main():
    test_more_than_zero()
    test_zero()

def test_more_than_zero():
    assert count("um?") == 1
    assert count("Um") == 1
    assert count("hola um, asdasd") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album.") == 1

def test_zero():
    assert count("yummy") == 0
    assert count("hola, Tum Tum") == 0
    assert count("Great album") == 0

if __name__ == "__main__":
    main()
