
import sys
from tabulate import tabulate

def main():
    file = sys.argv
    #file = ["", "regular.csv"]
    check_for(file)

def check_for(x):
    try:
        #print("Paso 1:", x)
        if len(x) == 2 and x[1].endswith(".csv"):
            x = x[1]
            #print("Paso 2:", x)
            table = []
            heads = 1
            with open(x) as file:
                for line in file:
                    y = line.split(",")
                    #y[0] = ''.join(['|'])
                    #table.append(y)
                    #print(type(y))
                    if heads == 1:
                        headers = y
                        
                        print(headers)
                        heads -= 1
                        #y[0] = ''.join(['|'])
                    else:
                        table.append(y)
                        #print(type(y))

            #print("Paso 4:")
            print(tabulate(
                table, headers, tablefmt="grid"
                ))
        elif len(x) < 2:
            sys.exit("Too feo commnand-line arguments")
        elif len(x) == 2 and not x[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        elif len(x) > 2:
            sys.exit("Too many arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")

main()