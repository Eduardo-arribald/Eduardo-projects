
def main():
    x = str(input()).split()
    #print(x)
    for i in x:
        if i == ':)' or i == ':(':
            print(type(i))
            i = convert(i)
    print(' '.join(x))

def convert(face:str):
    if ':)' == face:
        return ':-)'
    elif ':(' == face:
        return ':-('

main()