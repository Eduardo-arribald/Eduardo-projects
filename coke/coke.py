


def main():
    money = 0
    while True:
        x = 50 #The cost of a soda
        #Amount due:
        print(f"Amount due: {x-money}")
        #The input to put the coin.
        coin = input("Insert Coin: ")
        #This adds the coin introduced to the money that's already in the machine.
        money = money + check_coins(coin)
        #This checs if the amount payed is equal or above 50.
        if money >= 50:
            #Prints the change based on the money introduced. 
            print(f"Change Owed: {money - x}")
            break

def check_coins(c):
    coins = ["25", "10", "5"]
    if c in coins:
        c = int(c)
        return c
    else:
        return 0

main()