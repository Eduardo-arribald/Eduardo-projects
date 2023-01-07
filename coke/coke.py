
def main():
    money = 0
    while True:
        x = 50
        print(f"Amount due: {x}")
        coin = input("Insert Coin: ")
        check_coins(coin)
        
        break

def check_coins(c):
    coins = ["25", "10", "5"]
    if c in coins:
        c = int(c)


main()