
def change_date():
    while True:
        try:
            meses = [
                "January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"
                ]
            date = input("Date: ").split()
            date_1 = ('/'.join(date)).split("/")
            date = (','.join(date_1)).split(",")
            #print(date)
            if date[0] in meses:
                date[0] = meses.index(date[0]) + 1
                to_int(date)
                return print(f"{date[2]:02}-{date[1]:02}-{date[0]:02}")

            elif date[1] or date[2] in meses:
                continue
            elif int(date[0]) > 12 or int(date[1]) > 31:
                continue
            else:
                to_int(date)
                return print(f"{date[2]:02}-{date[1]:02}-{date[0]:02}")
        except:
            continue

def to_int(lista:list):
    for i in range(len(lista)):
        lista[i] = int(lista[i])

change_date()