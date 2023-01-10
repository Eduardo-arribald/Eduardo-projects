
import inflect

p = inflect.engine()

thing = "example"
idea = " digit"

x = input("Name: ")




print("Did you want ", p.a(thing), "or", p.an(idea))
