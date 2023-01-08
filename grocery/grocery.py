
def grocery_list():
    lista = {}
    while True:
        try:
            order = input("")
            print(order)
            if order in lista.keys():
                lista[order] += 1
            else:
                lista[order] = 1
                #print(lista)
                #break

        except EOFError:
            #print(sep = "\n")
            for i in lista.keys():
                print(lista.get(i), i)
            break #print("\nTotal: "+ "$" + format(count, ".2f"))


grocery_list()