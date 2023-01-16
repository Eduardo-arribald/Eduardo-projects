
from twttr import shorten

def main():
    test_names()
    test_phrases()

def test_names():
    assert shorten("Eduardo") == "drd"
    assert shorten("Arantza") == "rntza"
    assert shorten("Humberto") == "Hmbrt"

def test_phrases():
    assert shorten("Hola, mi amorcito") == "Hl, m mrct"
    assert shorten()


if __name__=="__main__":
    main()


