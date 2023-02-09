import sys
import csv

count = 0
with open("example.py") as file:
    for line in file:
        x = line.split()
        if len(x) > 0: #and x[0] != '#':
            y = list(''.join(x))
            #print(y)
            if y[0] != '#':
                #print(line)
                count +=1

word = 'Eduardo'

w.lstrip()
w.startswith()

#print(str(count))