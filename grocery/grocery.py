
def grocery_list():
    lista = {}
    while True:
        try:
            order = input("Item: ").strip()
            if order in lista.keys():
                lista[order] += 1
            else:
                lista[order] == 1
                #print(lista)
                #break

        except EOFError:
            #print(sep = "\n")
            #print(lista)
            break #print("\nTotal: "+ "$" + format(count, ".2f"))

jola = {}

jola["hola"] = 1
jola["hola"] += 1

#print(jola["hola"])

#for i in jola.keys()
 #   print(jola.keys(i), jola.get(i))

#print(jola)

#grocery_list()