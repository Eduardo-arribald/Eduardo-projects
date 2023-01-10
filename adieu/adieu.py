
import inflect

p = inflect.engine()

thing = "example"

idea = " digit"

print("Did you want ", p.a(thing), "or", p.an(idea))
