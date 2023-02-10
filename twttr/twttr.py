

def main():
    words = input("Input: ")
    #delete_vowels(words)
    print("Output", delete_vowels(words))

def delete_vowels(w):
    vowels = ("a", "e", "i", "o", "u")
    w = list(' '.join(w.split()))
    n = []
    for l in range(len(w)):
        if w[l].lower() not in vowels:
            n.append(w[l])
    return (''.join(n))

main()