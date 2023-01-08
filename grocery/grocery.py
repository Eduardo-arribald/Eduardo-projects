
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
            keys = list(lista.keys())
            keys.sort()
            #This function takes keys (i) from the dictionary called "lista", and
            #the value (dict[i]), deppending on the values(already sorted)
            #from the list called "keys".
            new_list = {i : lista[i] for i in keys}
            for i in new_list.keys():
                print(new_list.get(i), i)
            break

grocery_list()
