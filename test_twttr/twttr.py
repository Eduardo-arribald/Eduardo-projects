
def main():
    tweet = input()
    print(shorten(tweet))


def shorten(word:str):
    vowels = ("a", "e", "i", "o", "u")
    word = list(' '.join(word.split()))
    n = []
    for l in range(len(word)):
        if word[l].lower() not in vowels or word[l].isdigit():
            n.append(word[l])
    return (''.join(n))



if __name__ == "__main__":
    main()


