
def grocery_list():
    count = {}
    while True:
        try:
            order = input("Item: ").strip()
            
            break

        except EOFError:
            print(sep = "\n")

            break #print("\nTotal: "+ "$" + format(count, ".2f"))

grocery_list()