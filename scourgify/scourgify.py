
import csv
import sys

def main():
    file = sys.argv
    #file = [1, "before.csv", "after.csv"]
    process_file(file)


def process_file(x):
    if len(x) == 3 and x[1].endswith(".csv") and x[2].endswith(".csv"):
        new = x[2][:-4]
        new = new + ".txt"
        #print(new)
        with open(new, "w") as new_file:
            headers = ["first", "last", "house"]
            #writer = csv.DictWriter(new_file, fieldnames = headers)
            new_file.write(f"{headers[0]},{headers[1]},{headers[2]} \n")
            #try:
            with open(x[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last, first = row["name"].split(',')
                    first = first.lstrip()
                    house = row["house"]
                    #writer.writeheader()
                    #writer.writerow({
                    new_file.write(f"{first},{last},{house} \n")
                        #})
            #except:
                #sys.exit(f"Could not read {x[1]}")
    elif len(x) > 3:
        sys.exit("Too many command-line arguments")
    elif len(x) < 3:
        sys.exit("Too few command-line arguments")


main()