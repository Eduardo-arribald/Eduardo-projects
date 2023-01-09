
def change_date():
    while True:
        try:
            meses = [
                "January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"
                ]
            d = input("Date: ")
            date = d.split()
            #print(date)

            if string_and_slashes(d):
                date = ('/'.join(date)).split("/")
                date = (','.join(date))
                #print(date)
                date = date.split(",")
                #print(date)
                if "" in date:
                    date.remove("")
                int(date[1])
                conditions(date)
                break
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

def conditions(x:list):
    date = x
    meses = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
        ]
    if date[0] in meses:
        date[0] = meses.index(date[0]) + 1
        to_int(date)
        if month_day(date):
            return print(f"{date[2]:02}-{date[0]:02}-{date[1]:02}")
    elif date[0] in small():
        date[0] = small().index(date[0]) + 1
        to_int(date)
        if month_day(date):
            return print(f"{date[2]:02}-{date[0]:02}-{date[1]:02}")
    elif month_day(date):
        to_int(date)
        return print(f"{date[2]:02}-{date[0]:02}-{date[1]:02}")


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

def string_and_slashes(data:str):
    try:
        x = data.split()
        #print(x)
        x = (''.join(x)).split("/")
        if len(x) > 1:
            #print(x)
            #try:
            int(x[0])
            int(x[1])
            int(x[2])
            return True
        else:
            return True
    except ValueError or IndexError:
        return False
    except:
        return False




#string_and_slashes()

change_date()

