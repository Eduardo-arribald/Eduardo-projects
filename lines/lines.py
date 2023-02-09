import sys


def main():
    #Argument 0 is this file name itself.
    #Argument 1 is the file that I need to count for.
    #print(sys.argv[0])
    if len(sys.argv) > 1:
        x = sys.argv[1]
        print(x)
        #search_for(x)

    else:
        sys.exit("Too few arguments.")


def search_for(file):
    count = 0
    with open(file) as file:
        for line in file:
            x = line.lstrip()
            #print(x)
            if x != '' and not x.startswith("#"):
                print(x)
                #y = list(''.join(x))
                #print(y)
                #if file != '#':
                #print(line)
                count +=1
        print(str(count))

main()