
def grocery_list():
    count = {}
    while True:
        try:
            order = input("Item: ").strip()
            if order in count.keys()
                count[order] += 1
            else:
                
                print(count)
                break

        except EOFError:
            print(sep = "\n")

            break #print("\nTotal: "+ "$" + format(count, ".2f"))

grocery_list()