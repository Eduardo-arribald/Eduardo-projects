
from twttr import shorten

def main():
    test_names()
    test_phrases()
    #test_numbers()

def test_names():
    assert shorten("EDUARDO") == "DRD"
    assert shorten("ARANTZA") == "RNTZ"
    assert shorten("777 Humberto") == " Hmbrt"

def test_phrases():
    assert shorten("HOLA, MI AMORCITO") == "HL, M MRCT"
    assert shorten("BUENAS NOCHES!") == "BNS NCHS!"
    #assert shorten("2 tacos, por favor") == " tcs, pr fvr"

#def test_numbers():
    #assert shorten("2 tacos, por favor") == " tcs, pr fvr"
    #assert shorten("Gano 3000 pesos al mes") == "Gn  pss l ms"


if __name__=="__main__":
    main()


