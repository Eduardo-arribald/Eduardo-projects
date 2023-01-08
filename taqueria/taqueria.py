

def felipe():
    while True:
        order = input("Item: ").strip().title()
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
            return print("Total: "+ "$" + str(round(menu.get(order),3)))

felipe()