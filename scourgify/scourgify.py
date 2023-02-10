
import csv

with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "name": row['name'],
                "home": row['home'],
                })

    name = input("What's your name? ")
    home = input("What's your home? ")
    with open("students.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "home"])
        writer.writerow({"name":name, "home":home})
