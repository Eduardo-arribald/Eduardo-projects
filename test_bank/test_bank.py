from bank import value

def main():
    test_names()
    test_phrases()
    #test_numbers()

def test_names():
    assert shorten("EDUARDO") == "DRD"
    assert shorten("ARANTZA") == "RNTZ"
    assert shorten("777 Humberto") == "777 Hmbrt"
