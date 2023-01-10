
import inflect

p = inflect.engine()

thing = "car"

idea = " digit"

print("Did you want ", p.a(thing), "or", p.an(idea))
