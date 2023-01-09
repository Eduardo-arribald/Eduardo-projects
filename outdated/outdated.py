
def change_date():
    while True:
        try:
            meses = [
                "January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"
                ]
            date = input("Date: ").split()
            print(date)
            date_check = (''.join(date)).split("/")
            print(date_check)
            if date_check[0] == str and int[date_check[0:2]] is int:
                date = ('/'.join(date)).split("/")
                date = (','.join(date))
                #print(date)
                date = date.split(",")
                #print(date)
                if "" in date:
                    date.remove("")

                if date[0] in meses:
                    date[0] = meses.index(date[0]) + 1
                    to_int(date)
                    if month_day(date):
                        return print(f"{date[2]:02}-{date[0]:02}-{date[1]:02}", end = "")
                elif date[0] in small():
                    date[0] = small().index(date[0]) + 1
                    to_int(date)
                    if month_day(date):
                        return print(f"{date[2]:02}-{date[0]:02}-{date[1]:02}", end = "")
                elif month_day(date):
                    to_int(date)
                    return print(f"{date[2]:02}-{date[0]:02}-{date[1]:02}", end = "")
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

def small():
    meses = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
        ]
    small = []
    for i in range(len(meses)):
        small.append(meses[i][0:3])
    #print(small)
    return small

#change_date()

x = "October29/1999".split()
print(x)


x = (''.join(x)).split("/")
print(x)


#if date_check[0] == str and int[date_check[0:2]] is int:

