
import inflect

p = inflect.engine()

thing = "example"
idea = " digit"

names = []

while True:
    try:
        x = input("Name: ")
        names.append(x)

        print("Did you want ", p.a(thing), "or", p.an(idea))
        break
    except:
        print("Adieu, adieu, to", end = " ")
        for i in names:
            if len(names) == 1:
                print(names[0])
            elif len(names) > 1:
                print(names)