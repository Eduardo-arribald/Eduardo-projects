import sys

count = 0

def serach_for(file):
    with open("example.py") as file:
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