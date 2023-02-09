import sys
import csv

count = 0
with open("fuel.py") as file:
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

word = '     Eduardo'

#print(word.lstrip()) #Removes spaces from the left.

#print(word.startswith('E'))

print(str(count))