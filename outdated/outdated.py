
def change_date():
    meses = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
        ]
    date = input("Date: ").split()
    date_1 = ('/'.join(date)).split("/")
    date = (','.join(date_1)).split(",")
    print(date)
    for i in range(len(date)):
        if date[i] in meses:
            date[i] = meses.index(date[i]) + 1
            #print(date)

    #print(date)

change_date()