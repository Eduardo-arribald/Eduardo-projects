
def main():
    t = input("What time is it? ")
    t = convert_2(t)
    if 7 <= t <=8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    n = (''.join(time.split())).split(":")
    h, m = n[0], n[1]
    new = round((int(h) + (int(m)/60)), 2)
    return new

def convert_2(time):
    n = time.split()
    print(n)
    h, m = n[0].split(":")
    if n[1] is not None:
        match n[1]:
            case "p.m.":
                return round((12 + int(h) + (int(m)/60)), 2)
            case "a.m.":
                return round((int(h) + (int(m)/60)), 2)
    else:
        return round((int(h) + (int(m)/60)), 2)

if __name__ == "__main__":
    main()