
def main():
    t = input("What time is it? ")
    t = convert(t)
    

def convert(time):
    n = (''.join(time.split())).split(":")
    h, m = n[0], n[1]
    new = round((int(h) + (int(m)/60)), 1)
    return new

if __name__ == "__main__":
    main()