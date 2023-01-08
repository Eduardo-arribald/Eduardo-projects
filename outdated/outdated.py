
def change_date():
    meses = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
        ]
    date = input("Date: ").split()
    if len(date) > 0:
        for i in range(len(date)):
            for n in range(len(meses)):
                if date[i] == meses[n]:
                    date[i] == n+1
    elif "/" in list(date):
        date.split("/")
    print(date)

change_date()