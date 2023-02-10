
import csv
import sys

def main():
    #file = sys.argv()
    f = [1, "before.csv", "after.csv"]
    read_file(f)


def read_file(x):
    wili = []
    if len(x) == 3 and x[1].endswith(".csv") and x[2].endswith(".csv"):
        with open(x[2], "w") as new_file:
            headers = ["first", "last", "house"]
            writer = csv.DictWriter(new_file, fieldnames = ["first", "last", "house"])

            with open(x[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last, first = row["name"].split(',')
                    first = first.lstrip()
                    house = row["house"]
                    #print(row["name"], "=", first)
                    #print(row)
                    writer.writerow({
                        "first":first,
                        "last":last,
                        "house": house
                        })
            print(writer[1])

#    name = input("What's your name? ")
#    home = input("What's your home? ")
#    with open("students.csv", "w") as file:
#        writer = csv.DictWriter(file, fieldnames = ["name", "home"])
#        writer.writerow({"name":name, "home":home})


main()