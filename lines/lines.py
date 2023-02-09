import sys


def main():
    #Argument 0 is this file name itself.
    #Argument 1 is the file that I need to count for.
    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        x = sys.argv[1]
        #print(x)
        search_for(x)
    elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
        print("Not a python file")
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
    else:
        sys.exit("Too few arguments")


def search_for(file):
    count = 0
    try:
        with open(file) as file:
            for line in file:
                x = line.lstrip()
                #print(x)
                if x != '' and not x.startswith("#"):
                    #print(x)
                    #y = list(''.join(x))
                    #print(y)
                    #if file != '#':
                    #print(line)
                    count +=1
            print(str(count))
    except FileNotFoundError:
        print("File does not exist")


main()