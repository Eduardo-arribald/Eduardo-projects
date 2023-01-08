
def grocery_list():
    lista = {}
    while True:
        try:
            order = input("Item: ").strip()
            if order in lista.keys():
                lista[order] += 1
            else:
                lista[order] == 1
                print(lista)
                break

        except EOFError:
            #print(sep = "\n")

            break #print("\nTotal: "+ "$" + format(count, ".2f"))

jola = {}

jola["hola"] = 1
jola["hola"] += 1

print(jola["hola"])

#grocery_list()