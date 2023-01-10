
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
        