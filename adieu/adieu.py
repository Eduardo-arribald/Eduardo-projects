
import inflect

p = inflect.engine()

thing = "example"
idea = " digit"

names = []

while True:
    try:
        x = input("Name: ")
        names.append(x)

        #print("Did you want ", p.a(thing), "or", p.an(idea))
        #break
    except:
        print("Adieu, adieu", end = "")
        for i in range(len(names)):
            if len(names) == 1:
                print(", to " + names[i])
            elif len(names) > 1 and names[i] != names[-1]:
                print(f", to {names[i]}", end = "")
            elif len(names) > 1 and names[i] == names[-1]:
                print(f" and {names[i]}")
        break