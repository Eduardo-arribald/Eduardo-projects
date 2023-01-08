
def grocery_list():
    count = {}
    while True:
        try:
            order = input("Item: ").strip()
            count[order] += 1
            print(count)
            break

        except EOFError:
            print(sep = "\n")

            break #print("\nTotal: "+ "$" + format(count, ".2f"))

grocery_list()