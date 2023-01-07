
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    alpha = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z'
    )
    #I take off the spaces before and after the text.
    s = s.split() #A list of the word given.
    if len(s) >= 2:
        return False
    else:
        s = list(''.join(s))
        print(s)
        if 2 <= s <= 6:
            if s[0].lower() and s[1].lower() in alpha:
                #print("yes")
                    return True
        else:
            #print("no")
            return False

main()
