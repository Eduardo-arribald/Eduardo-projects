
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
                if month_day(date):
                    return print(f"{date[2]:02}-{date[1]:02}-{date[0]:02}")
            elif month_day(date):
                to_int(date)
                return print(f"{date[2]:02}-{date[1]:02}-{date[0]:02}")
        except:
            #continue
            break

def to_int(lista:list):
    for i in range(len(lista)):
        lista[i] = int(lista[i])

def month_day(lista:list):
    if int(lista[0]) > 12 or int(lista[1]) > 31:
        return False
    else:
        return True

def months_small(lista:list):
    meses = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
        ]
    small = []
    for i in range(len(meses)):
        

#change_date()