
def change_date():
    meses = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
        ]
    date = input("Date: ").split()
    date_1 = ('/'.join(date)).split("/")
    date = (','.join(date_1)).split(",")
    print(date)
    if date[0] in meses:
        date[i] = meses.index(date[i]) + 1

    elif date[1] or date[2] in meses:
        continue

change_date()