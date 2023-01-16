from bank import value

def main():
    test_hello()
    test_rest()
    #test_numbers()

def test_hello():
    assert value("Hello") == 0
    assert value("Hi!") == 20

def test_rest():
    assert value("Good evening!") == 100
    assert value("Good morning!") == 100

if __name__ == "__main__":
    main()