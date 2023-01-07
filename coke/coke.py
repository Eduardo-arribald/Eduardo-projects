
def main():
    money = 0
    while True:
        x = 50
        print(f"Amount due: {x-money}")
        coin = input("Insert Coin: ")
        money = money + check_coins(coin)
        if money >= 50:
            print(f"Change Owerd: {money - x}")
            break

def check_coins(c):
    coins = ["25", "10", "5"]
    if c in coins:
        c = int(c)
        return c

main()