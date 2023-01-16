
from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten("Eduardo") == "drd"


if __name__=="__main__":
    main()


