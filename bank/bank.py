
greet = input("Greeting: ").lower().split()

first = list(greet[0])[0:5]

hello = list("hello")

if hello == first:
    print("$0")
elif first[0]=="h":
    print("$20")
else:
    print("$100")

