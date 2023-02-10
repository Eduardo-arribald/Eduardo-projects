
import csv
import sys

def main():
    #file = sys.argv()
    file = [1, "before.csv", "hola.csv", "Si"]
    print(len(file))
    process_file(file)


def process_file(x):
    try:
        if len(x) > 3:
            sys.exit("Too many command-line arguments")
        elif len(x) < 3:
            sys.exit("Too few command-line arguments")

        elif len(x) == 3 and x[1].endswith(".csv") and x[2].endswith(".csv"):
            with open(x[2], "w") as new_file:
                headers = ["first", "last", "house"]
                writer = csv.DictWriter(new_file, fieldnames = headers)

                with open(x[1]) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        last, first = row["name"].split(',')
                        first = first.lstrip()
                        house = row["house"]
                        #print(row["name"], "=", first)
                        #print(row)
                        writer.writeheader()
                        writer.writerow({
                            "first":first,
                            "last":last,
                            "house": house
                            })

    except:
        sys.exit(f"Could not read {x[1]}")


main()