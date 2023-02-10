
import sys
from tabulate import tabulate

def main():
    #file = sys.argv
    file = ["", "regular.csv"]
    check_for(file)

def check_for(x):
    #try:
    print("Paso 1:", x)
    if len(x) == 2 and x[1].endswith(".csv"):
        x = x[1]
        print("Paso 2:", x)
        table = []
        with open(x) as file:
            for line in file:
                table.append(line)
                print(type(line))

        print("Paso 4:", tabulate(table))
    elif len(x) < 2:
        sys.exit("Too feo commnand-line arguments")
    elif len(x) == 2 and not x[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif len(x) > 2:
        sys.exit("Too many arguments")
    #except FileNotFoundError:
        #sys.exit("File does not exist")

main()