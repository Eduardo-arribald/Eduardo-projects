

def main():
    words = input("Input: ")
    #delete_vowels(words)
    print ("Output", delete_vowels(words))

def delete_vowels(w):
    vowels = ("a", "e", "i", "o", "u")
    w = list(''.join(w.split()))
    print(w)
    for l in range(len(w)):
        if w[l] in vowels:
            w.pop(l, inplace = True)
            print(w[l])
    return (''.join(w))

main()