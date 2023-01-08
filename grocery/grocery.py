
def grocery_list():
    lista = {}
    while True:
        try:
            order = input().upper()
            #print(order)
            if order in lista.keys():
                lista[order] += 1
            else:
                lista[order] = 1
                #print(lista)
                #break

        except EOFError:
            #print(sep = "\n")
            for i in lista.keys():
                print(lista.get(i), i, end = "")
            break

grocery_list()