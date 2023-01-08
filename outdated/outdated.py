
def change_date():
    meses = [
        "January", "February", "March",    "April",
        "May", "June", "July", "August", "September",
        "October", "November", "December"
        ]

    date = input("Date: ").split()
    if len(date) > 1:
        for i in range(len(date)):
            if date[i] in meses:
    elif "/" in list(date):
        date.split("/")

