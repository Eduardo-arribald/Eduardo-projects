

x = "Holamundo"

x = list(x.split())


new = []

for i in range(len(x)):
    if x[i].isupper():
        x[i] = "_"+ x[i].lower()
        print("upper" + L[0])


