
"""
> What will your software do? What features will it have? How will it be executed?
   I will make a program for countability administration of startups, in a simple and comprehensible way.
   Features:
   Presentation of assets, passives, and capital(elements of a general balance).
   This information will be easily watchable in an csv file.

> What new skills will you need to acquire? What topics will you need to research?
   Knowledge of all the information under a basic balance sheet and more about dictionaries' indexes. Also know more about the management
   of multiple while loops and how to break them.

> In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish less
  in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome?
   The best outcome would be a csv file in wich you could see all the information inputed, sorted and easily readable. You should be able of
   see and control everything from the program, without need of checking other app. This program shouldn't output errors and should consider
   all the possible answers from the users.
   A good outcome would be an csv with just the balance sheet of all the information inputed, sorted and easily readable.
   A better outcome would be a combination of these two.

Based in the book: Contabilidad para PYMES, FAECO.

   """
import datetime
import csv
import re
from tabulate import tabulate


def main():
    #Question 0: Are we working with a new file? (yes/no)
    new_file = input("Are we working with a new file?(yes/no) ").lower()
    #new_file = "no"
    #see_list_of_items: Whould you like to see a list of the availables accounts first? (yes/no)
    see_list_of_items = input("Whould you like to see a list of the availables accounts first?(yes/no) ").lower()

    watch_list_of_accounting_items(see_list_of_items)

    #Here the new file modifications begins.
    if new_file == "yes":
        #Creating the file
        actual_date = str(datetime.date.today())
        with open("Balance Sheet "+actual_date+".csv", "w", newline= "") as csvfile:
            #List of liabilities accounts
            liabilities_list = [
                "Circulating Liabilities", "Providers", "Bank loans ST",
                "Various creditors", "Other liabilities ST", "Long term and\ndeferred liabilities",
                "Bank loans LT", "Accounts payable", "Other liabilities LT",
                "Deferred liabilities", "Total Liabilities"]

            #List of equity accounts
            equity_list = ["Equity", "Social Capital",
                "Legal Reserve", "Retained earnings", "Total Equity", "Total Liabilities\nand Equity"]

            #List of assets accounts
            Assets_list = [
                "Circulating assets", "Cash", "Banks", "Investments ST",
                "Accounts receivable", "Stock", "Other circulating assets",
                "Fixed and deferred assets", "Accounts receivable LT", "Investments LT",
                "Buildings and land", "Machinery", "Equipment", "Accumulated amortization and depretiation",
                "Deferred assets", None, "Total assets", "Date:", f"Last modification\ndate: {actual_date}"]

            #Create a new dictionary with the three accounts, wich includes the totals and the dates of the balance sheet as well as the
            # last modification date of that report.
            #When we make a new balance sheet, we have to:
            # > create a new dictionary
            # > set the actual date as the report date
            # > set the last modification date
            # > open modification options in a while loop
            # > close the file

            balance_sheet = {
                "Assets": Assets_list,
                "Amount_1": [f"$ {0}"]*15 +["",f"$ {0}"]+[""]*2,
                "Liabilities and Equity": liabilities_list + equity_list + [""]*2,
                "Amount_2": [f"$ {0}"]*10 + [""]+ [f"$ {0}"]*6 + [""]*2
                }
            balance_sheet["Amount_2"][11] = ""
            make_another_modification = True
            while make_another_modification == True:
                #Question 1: What's the main account to modificate?
                account_1 = input("What's the main account to modificate? ")
                #account_1 = "Stock"
                #Question 2: Whats the effect account to modificate?
                account_2 = input("What's the effect account to modificate? ")
                #account_2 = "Providers"
                #Question 3: What's the amount in which you would like to change the balance?
                amount = checker_of_the_amount_inputed()
                #amount = int("100")
                balance_sheet = new_or_current_balance(balance_sheet, account_1, account_2, amount)
                while True:
                    #other_modification: Would you like to make another modification?
                    other_modification = ''.join(input("Would you like to make another modification?(yes/no) ").lower().split())
                    #other_modification = "no"
                    if other_modification == "yes":
                        break
                    elif other_modification == "no":
                        print("Saving changes...")
                        write = csv.writer(csvfile)
                        write.writerow(balance_sheet.keys())
                        for iteration in range(19):
                            write.writerow([val[iteration] for val in list(balance_sheet.values())])
                        return make_another_modification == False
                    else:
                        print("Answer not recognized.")



    #This begins the modifications of an old balance sheet.
    elif new_file == "no":
        file_found = False
        while file_found == False:
            #old_file_name: What's the name of the file? It has to be a .csv file.
            #old_file_name = "C:/Users/arria/OneDrive/Documentos/Python/CS50/Final project/Balance Sheet 2023-05-04.txt"
            old_file_name = input("What's the name of the file? It must be a .csv file with\nthe same format of accounts that this program creates. ")
            #old_file_name = "C:/Users/arria/OneDrive/Documentos/Python/CS50/Final project/Balance Sheet 2023-05-04.csv"

            try:
                #Open the file
                with open(old_file_name, 'r') as file:
                    reader = csv.DictReader(file)
                    assets = []
                    amount_1 = []
                    liabilities_equity = []
                    amount_2 = []

                    for record in reader:
                        assets.append(record["Assets"])
                        amount_1.append(record["Amount_1"])
                        liabilities_equity.append(record["Liabilities and Equity"])
                        amount_2.append(record["Amount_2"])


                    balance_sheet = {
                        "Assets": assets,
                        "Amount_1": amount_1,
                        "Liabilities and Equity": liabilities_equity,
                        "Amount_2": amount_2
                        }
                    actual_date = str(datetime.date.today())
                    balance_sheet["Assets"][18] = f"Last modification\ndate: {actual_date}"

                    make_another_modification = True
                    while make_another_modification == True:
                        #Question 1: What's the main account to modificate?
                        account_1 = input("What's the main account to modificate? ")
                        #account_1 = "Stock"
                        #Question 2: Whats the effect account to modificate?
                        account_2 = input("What's the effect account to modificate? ")
                        #account_2 = "Providers"
                        #Question 3: What's the amount in which you would like to change the balance?
                        amount = checker_of_the_amount_inputed()
                        #amount = int("100")
                        balance_sheet = new_or_current_balance(balance_sheet, account_1, account_2, amount)

                        while True:
                            #other_modification: Would you like to make another modification?
                            other_modification = input("Would you like to make another modification?(yes/no) ")
                            #other_modification = "no"
                            if other_modification.lower() == "yes":
                                break
                            elif other_modification.lower() =="no":
                                #Saving the dictionary
                                with open(old_file_name, mode='w') as outfile:
                                    print("Saving current balance sheet...")
                                    write = csv.writer(outfile)
                                    write.writerow(balance_sheet.keys())
                                    for iteration in range(19):
                                        write.writerow([val[iteration] for val in list(balance_sheet.values())])
                                return make_another_modification == False, file_found == True
                            else:
                                print("Answer not recognized.")
            except FileNotFoundError:
                while True:
                    x = input("File not found.\nDo you want to create a new file with the format required?(yes/no) ")
                    if x == "yes":
                        return file_found == True
                    elif x == "no":
                        break
                    else:
                        print("Answer not recognized.")


def checker_of_the_amount_inputed():
    while True:
        try:
            amount = int(input("What's the amount to add/substract? "))
            return amount
            #break
        except:
            print("Not a number.")


def watch_list_of_accounting_items(answer):
    breaker_of_list_loop = True
    if answer == "yes":
        while breaker_of_list_loop == True:
            #accounting_item: Which type of accounting item? Assets, Liabilities or Equity?
            accounting_item = input("Which type of accounting item? Assets, Liabilities or Equity? ").lower()
            assets_list = [
                "Circulating assets (Not mutable)", "Cash", "Banks", "Investments ST",
                "Accounts receivable", "Stock", "Other circulating assets",
                "Fixed and deferred assets (Not mutable)", "Accounts receivable LT", "Investments LT",
                "Buildings and land", "Machinery", "Equipment", "Accumulated amortization and depretiation",
                "Deferred assets", "Total Assets (Not mutable)"]
            liabilities_list = [
                "Circulating Liabilities (Not mutable)", "Providers", "Bank loans ST",
                "Various creditors", "Other liabilities ST", "Long term and deferred liabilities (Not mutable)",
                "Bank loans LT", "Accounts payable", "Other liabilities LT",
                "Deferred liabilities", "Total liabilities (Not mutable)"]
            equity_list = ["Equity (Not mutable)", "Social Capital",
                "Legal Reserve", "Retained earnings", "Total Equity (Not mutable)", "Total Liabilities and Equity (Not mutable)"]

            dict_of_accounts = {
                "assets": assets_list,
                "liabilities": liabilities_list,
                "equity": equity_list
                }

            wrong = 0
            #This for loop checks for the name of the accounting item.
            #If the accounting item isn't found, loop breaks and print an error message to restart the searching loop.
            for key in dict_of_accounts.keys():
                if accounting_item == key:
                    n = 1
                    for ac in range(len(dict_of_accounts[key])):
                        print(f"{n}) {dict_of_accounts[key][ac]}")
                        n += 1
                    while True:
                        #see_another_list: Would you like to see another list of accounts? (yes/no)
                        see_another_list = ''.join(input("Would you like to see another list of accounts? (yes/no) ").lower().split())
                        if see_another_list.lower() == "yes":
                            break
                        elif see_another_list.lower()=="no":
                            return breaker_of_list_loop == False
                        else:
                            print("Answer not recognized.")

                else:
                    wrong += 1
                    if wrong == 3:
                        print("Accounting item not found.")

                        while True:
                            #search_again: Would you like to search again?
                            search_again = ''.join(input("Do you want to search agan?(yes/no) ").lower().split())
                            if search_again == "yes":
                                break
                            elif search_again == "no":
                                return breaker_of_list_loop == False
                            else:
                                print("Answer not recognized.")



def new_or_current_balance(balance_sheet, account_1, account_2, amount):

    #Create the date object
    actual_date = actualization_date("yes")

    #This sets the date of the new balance sheet
    balance_sheet["Assets"][17] = f"Date: {actual_date}"

    #This makes the corresponding additions and substractions to the dictionary.
    add_or_substract(balance_sheet, amount, account_1, account_2)
    balance_sheet = dict(totals(balance_sheet))

    watch_balance_sheet = input("Do you want to see the current balance sheet? (yes/no) ")
    if watch_balance_sheet == "yes":
        balance_sheet["Assets"][13] = "Accumulated amortization\nand depretiation"
        print(tabulate(balance_sheet, headers = "keys", tablefmt= "rst"))
        balance_sheet["Assets"][13] = "Accumulated amortization and depretiation"
    return balance_sheet



def add_or_substract(data, amount, account_1, account_2):
    key_1, id_1 = search_for_index(data, account_1)
    key_2, id_2 = search_for_index(data, account_2)
    if key_2 != "Not found" and key_1 != "Not found":
        #If is in the same column
        if key_1 == key_2:
            #If there is not problem with the totals.
            if operation(data, key_1, id_1, amount) != False and operation(data, key_2, id_2, amount*(-1)) != False:
                #If both accounts belong to the assets
                if key_1 == "Assets":
                    #dictionary["Amount_1"][id]
                    data["Amount_1"][id_1] = operation(data, key_1, id_1, amount)
                    data["Amount_1"][id_2] = operation(data, key_2, id_2, amount*(-1))
                #If both accounts belong to the liabilities and equity
                elif key_1 == "Liabilities and Equity":
                    data["Amount_2"][id_1] = operation(data, key_1, id_1, amount)
                    data["Amount_2"][id_2] = operation(data, key_2, id_2, amount*(-1))

            else:
                raise ValueError("No negative values in accounts except for Accumulated amortization and depretiation.")
        #If is not in the same column
        else:
            #If there is not problem with the totals.
            if operation(data, key_1, id_1, amount) != False and operation(data, key_2, id_2, amount) != False:
                #If the first key is Assets
                if key_1 == "Assets":
                    data["Amount_1"][id_1] = operation(data, key_1, id_1, amount)
                    data["Amount_2"][id_2] = operation(data, key_2, id_2, amount)
                else:
                    data["Amount_2"][id_1] = operation(data, key_1, id_1, amount)
                    data["Amount_1"][id_2] = operation(data, key_2, id_2, amount)

            else:
                raise ValueError("No negative values in accounts except for Accumulated amortization and depretiation.")


    elif key_1 == "Not found":
        print("Account 1 not found")
    elif key_2 == "Not found":
        print("Account 2 not found")



def search_for_index(dictionary, item):
    not_found = 0
    if item == None or item == "":
        raise ValueError("Missing account")
    for key in dictionary.keys():
        lista = dictionary[key]
        for i in range(len(lista)):
            if item == lista[i] and item != "" and item != None:
                return key, i
            elif key == "Amount_2":
                not_found += 1
                if not_found == 19:
                    return "Not found", 0


def operation(dictionary, key, id, amount):
    if key == "Assets":
        inicial_amount = quit_money_format(dictionary["Amount_1"][id])
        final_amount = inicial_amount + amount
        if id == 13 and final_amount <= 0:
            return add_money_format(final_amount)
        elif id != 13 and final_amount >= 0:
            return add_money_format(final_amount)
        else:
            print("Only Accumulated amortization and depretiation can be negative. The rest of the acounts must be equal or superior to 0.\nNo changes were made.")
            return False

    elif key == "Liabilities and Equity":
        inicial_amount = quit_money_format(dictionary["Amount_2"][id])
        final_amount = inicial_amount + amount
        if final_amount >= 0:
            return add_money_format(final_amount)
        else:
            print("Only Accumulated amortization and depretiation can be negative. The rest of the acounts must be equal or superior to 0.\nNo changes were made.")
            return False

#Function 1 to test
def actualization_date(answer = "no"):
    answer = answer.lower().split()[-1]
    if answer == "yes":
        return str(datetime.date.today())
    else:
        return None


#Function 2 to test
def add_money_format(number:int):
    x = str(f"$ {number}")
    return x

#Function 3 to test
def quit_money_format(number:str):
    x = int((number.split("$"))[-1])
    return x

def totals(dictionary):
    #I define a dictionary with the start, end and number of the column amount where I want to add the numbers.
    amount_1 = {
        "CA": [dictionary["Amount_1"], 1, 7, 1],
        "FA": [dictionary["Amount_1"], 9, 16, 1],
    }

    amount_2 = {
        "CL": [dictionary["Amount_2"], 1, 5, 2],
        "LL": [dictionary["Amount_2"], 6, 10, 2],
        "Equity": [dictionary["Amount_2"], 12, 15, 2]

    }

    #Then I create a list of the two dictionaries to make this more workable.
    amounts = [amount_1, amount_2]

    #I make a list of the totals in an ascendent order.
    list_of_totals = []
    for amount_dict in range(len(amounts)):
        #print(amounts[amount_dict])
        d = amounts[amount_dict]
        for key in d.values():
            a = totals_2(key[0], key[1], key[2], key[3])
            list_of_totals.append(a)


    indexes_of_totals = [0, 7, 0, 5, 15]

    for total in range(len(list_of_totals)):
        for ident in range(len(indexes_of_totals)):
            if ident < 2:
                if ident == total:
                    dictionary["Amount_1"][indexes_of_totals[ident]] = add_money_format(list_of_totals[total])
            elif ident >= 2:
                if ident == total:
                    dictionary["Amount_2"][indexes_of_totals[ident]] = add_money_format(list_of_totals[total])

    #Total assets
    TA = list_of_totals[0] + list_of_totals[1]
    #Total liabilities
    TL = list_of_totals[2] + list_of_totals[3]
    #Liabilities + Equity
    L_plus_E = TL + list_of_totals[4]


    if TA == L_plus_E:
        dictionary["Amount_1"][16] = add_money_format(TA)
        dictionary["Amount_2"][10] = add_money_format(TL)
        dictionary["Amount_2"][16] = add_money_format(L_plus_E)
        return dictionary
    else:
        raise ValueError("Total Assets and Total Liabilities plus Equity are not equals.")

def totals_2(lista, inicial, final, account):
    total = 0
    cuentas_no_modificables = {
        "account_1":[0, 7, 15],
        "account_2":[0, 5, 10, 11, 15, 16]}

    for i in range(inicial, final):
        if account == 1 and i not in cuentas_no_modificables["account_1"]:
            x = quit_money_format(lista[i])
            total += x
        elif account == 2 and i not in cuentas_no_modificables["account_2"]:
            x = quit_money_format(lista[i])
            total += x
    return total


if __name__=="__main__":
    main()