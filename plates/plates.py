
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
    punctuations = (
        '-', '.', ',', '?', '!', '*', '+', '/', '', ' '
    )
    numbers = (
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    )
    #I take off the spaces before and after the text.
    s = s.split() #A list of the word given.
    if len(s) >= 2: #This corrects if the user gives me more than one word
        print("Two much words")
        return False
    else:
        s = list(''.join(s))
        print(s)
        if 2 <= len(s) <= 6: #This checks the lenght of the word.
            if s[0].lower() and s[1].lower() in alpha: #Check if the first two are letters.
                ya = []
                for i in range(len(s)):
                    if s[i] not in punctuations:
                        if s[-i-1] in numbers and s[-i] not in numbers:
                            return False
                        else:
                            ya.append(s[i])
                            if len(ya) == len(s):
                                print("Se armó")
                                return True
                            else:
                                print("Casi")
                                return False
                    else:
                        return False
        else:
            return False

main()
