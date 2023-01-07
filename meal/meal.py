
def main():
    t = convert(input("What time is it? "))
    if 7 <= t <=8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")


def convert(time):
    n = time.split()
    h, m = n[0].split(":")
    if n[-1] == "p.m.":
        return round((12 + int(h) + (int(m)/60)), 2)
    else:
        return round((int(h) + (int(m)/60)), 2)

if __name__ == "__main__":
    main()