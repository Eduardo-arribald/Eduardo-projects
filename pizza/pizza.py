
import sys
import tabulate

def main():
    file = sys.argv
    check_for(file)

def check_for(x):
    try:
        if len(x) == 2 and x[1].endswith(".csv"):
            x = x[1]
            with open(file) as file:
                for line in file:

        elif len(x) < 2:
            sys.exit("Too feo commnand-line arguments")
        elif len(x) == 2 and not x[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        elif len(x) > 2:
            sys.exit("Too many arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")