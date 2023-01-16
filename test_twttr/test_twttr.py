
from twttr import shorten

def main():
    test_names()
    test_phrases()

def test_names():
    assert shorten("EDUARDO") == "DRD"
    assert shorten("ARANTZA") == "RNTZ"
    assert shorten("Humberto") == "Hmbrt"

def test_phrases():
    assert shorten("HOLA, MI AMORCITO") == "HL, M MRCT"
    assert shorten("BUENAS NOCHES!") == "BNS NCHS!"


if __name__=="__main__":
    main()


