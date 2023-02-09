import sys
import csv

count = 0
with open("fuel.py") as file:
    for line in file:
        x = line.split()
        if x[0] is not None:
            count +=1

print(str(count))