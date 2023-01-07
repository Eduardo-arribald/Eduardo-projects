
def main():
    t = input("What time is it? ")
    t = convert(t)
    if 7 <= t <=8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    n = (''.join(time.split())).split(":")
    h, m = n[0], n[1]
    new = round((int(h) + (int(m)/60)), 1)
    return new

if __name__ == "__main__":
    main()