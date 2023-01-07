
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
                    print(s[i])
                    print(s[-(i+2)], s[-(i+1)])
                    if s[i] not in punctuations:
                        if s[-(i+2)] in numbers and s[-(i+1)] not in numbers:
                            print("There are numbers in the middle.")
                            return False
                        else:
                            ya.append(s[i])
                            if len(ya) == len(s):
                                print("Se armó")
                                return True
                            else:
                                print("They aren't the same lenght.")
                                return False
                    else:
                        print("You wrote a punctuation symbol.")
                        return False
            else:
                print("The first two are not letters.")
        else:
            print("You over passed the maximum or forgot about the minimum.")
            return False

main()
