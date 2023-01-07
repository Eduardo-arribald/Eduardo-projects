
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
    if s[1] is not None:
        return False
    else:
        s = list(s)
        if s[0:2].lower() not in alpha:
            print("No")
            return False

main()
