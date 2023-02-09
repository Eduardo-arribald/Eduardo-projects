import sys


def main():
    
    search_for(x)


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