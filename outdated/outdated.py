
def change_date():
    meses = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
        ]
    date = input("Date: ").split()
    print(date)
    date_1 = (''.join(date)).split("/")
    date_2 = list(''.join(date))
    print(date_1)
    print(date_2)
    if len(date) > 1:
        for i in range(len(date)):
            for n in range(len(meses)):
                if date[i] == meses[n]:
                    date[i] == n+1

    elif "/" in list(''.join(date)):
        date = ''.join(date).split("/")
    print(date)

change_date()