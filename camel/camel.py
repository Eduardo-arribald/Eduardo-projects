

x = "hola, mundo"

x = x.split()

new = []

for i in range(len(x)):
    L = x[i].split()
    if L[0].isupper():
        L[0] = "_"+ L[0].lower()
    

