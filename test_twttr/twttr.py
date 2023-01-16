
def main():
    tweet = input()
    print(shorten(tweet))


def shorten(word:str):
    vowels = ("a", "e", "i", "o", "u")
    numbs = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    word = list(' '.join(word.split()))
    n = []
    for l in range(len(word)):
        if word[l].lower() not in vowels or word[l] not in numbs:
        #if word[l].isdigit():
            n.append(word[l])
    return (''.join(n))



if __name__ == "__main__":
    main()


