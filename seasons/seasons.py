from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    print(get_minutes(input("Date of Birth: ")))
    #print(get_minutes("2022-04-15"))

    #Test by my own

    #print("1")
    #print(get_minutes("1999-01-01")) #Outputs: Five hundred twenty-five thousand, six hundred minutes
    #print("2")
    #print(get_minutes("1999-12-31")) #Outputs: One thousand, four hundred forty minutes
    #print("3")
    #print(get_minutes("1970-01-01")) #Outputs: Fifteen million, seven hundred seventy-eight thousand eighty minutes
    #print(get_minutes("January 1, 1999"))



def get_minutes(date_time): d #, todays = "2000-01-01"):
    try:
        born_date = date.fromisoformat(date_time)
        today = date.today()
        today = date.fromisoformat(str(today))
        #today = date.fromisoformat(todays) #Test date
        delta = today - born_date
        delta = int(delta.days)*24*60
        minutos = p.number_to_words(delta).capitalize()
        if " and " in minutos:
            minutos = minutos.replace(" and ", " ")
        return (f"{minutos} minutes")
    except ValueError:
        sys.exit("Invalid date")



if __name__ == "__main__":
    main()

