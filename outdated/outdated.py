
def change_date():
    meses = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
        ]
    date = input("Date: ").split()
    date_1 = (''.join(date)).split("/")
    date_2 = list(''.join(date))

    print(date)
    print(date_1)
    print(date_2)
    if len(date) > 1:
        for i in range(len(date)):
            if date[i] in meses:
                date[i] = meses.index(date[i]) + 1
                print(date)

    elif "/" in list(''.join(date)):
        date = ''.join(date).split("/")
    #print(date)

change_date()