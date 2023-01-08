

def felipe():
    count = 0
    while True:
        try:
            order = raw_input("Item: ").strip().title()
            menu = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
                }
            if menu.get(order) == None:
                continue
            else:
                count += menu.get(order)
                print("Total: "+ "$" + format(count, ".2f"))
        except EOFError:
            break

felipe()