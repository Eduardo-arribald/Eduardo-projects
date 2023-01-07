
def main():
    x = str(input()).split()
    #print(x)
    for i in range(len(x)):
        if x[i] == ':)' or x[i] == ':(':
            x[i] = convert(x[i])
    print(' '.join(x))

def convert(face:str):
    if ':)' == face:
        return '🙂'
    elif ':(' == face:
        return '🙁'

main()