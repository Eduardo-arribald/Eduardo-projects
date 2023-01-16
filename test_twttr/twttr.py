
def main():
    tweet = input()
    print(shorten(tweet))


def shorten(word:str):
    vowels = ("A", "E", "I", "O", "U")
    word = list(' '.join(word.split()))
    n = []
    for l in range(len(word)):
        if word[l] not in vowels:
            n.append(word[l])
    return (''.join(n))



if __name__ == "__main__":
    main()


