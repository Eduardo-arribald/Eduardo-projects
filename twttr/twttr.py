

def main():
    words = input("Input: ")
    print ("Output", delete_vowels(words))

def delete_vowels(w):
    vowels = ("a", "e", "i", "o", "u")
    w = list(''.join(w.split()))
    for l in range(len(w)):
        if w[l] in vowels:
            w[l] = None
    return ''.join(w)

main()