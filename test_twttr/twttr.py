
def main():
    tweet = input()
    print(sorten(tweet))


def shorten(word:str):
    vowels = ("a", "e", "i", "o", "u")
    word = list(' '.join(word.split()))
    n = []
    for l in range(len(w)):
        if w[l].lower() not in vowels:
            n.append(w[l])
    return (''.join(n))



if __name__ == "__main__":
    main()


