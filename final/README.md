# Entrepreneur Balance Sheet Program

#### Description:

This is an Enterpreneur Balance Sheet Program, or EBSP. You can enter information about your company to get a simple administrative visualizer of your Balance Sheet that will be returned in a csv file, and you can manage dates and amounts entered to get the financial control of your company. I have to say that accouting items can't be changed to keep the simplicity of the program.

- How does the program work?

The program prompts questions to the user to guide him thru the changes of the balance sheet. Firts, it asks if the user wants to create a new file or work with an old one, after this it asks if the user wants to see the list of some of the existing accounting items. This items belong to assets, liabilities and equity, and the user can see this items and their accounts as many times as he/she wants, before making any change. From this point, the amount manipulation begins and the program takes information of the two accounts and the amount to be added/substracted. This additions and substractions respect the basic rules of the balance sheets wich say that an efect in an account has the same effect in another account, and the symbol of this effect depends of the location of the first item versus the second one.

Once a change is made, the program gives the option to the user to see the balance sheet with the last modifications, and lastly if the user wants to make another modification. If not, the changes are saved and the file is closed.

- Wrong inputs

I worked hard to cover as many wrong answers as I could, but because I made this project in five days, I am mostly sure that not all user mistakes are covered. Despite this, the most basic errors(from my point of view) were covered like in yes/no questions and inexisting account names or file names. One user error that I wasn't sure about how to cover was a file without the format that my program creates, I have an idea of how to deal with it(wich involves "try" and "except" functions) but I just make the program to reject any error not mentioned here in old files printing "file not found".

- Functions:
    - Checker_of_amount_inputed(): Asks the user for an amount and if not a number, displays an error message and prompt the question again to the user.
    - Watch list of accounting items(answer): Depending on answer(yes/no), this prints the list of items of the three big parts of the balance sheet: assets, liabilities and equity. It recognizes wrong answers and gives the option to the user to search again or just to skip.
    - New_or_current_balance(balance_sheet, account_1, account_2, amount): This makes all the adding and substracting with a given dictionary and gives the option to the user to see the balance sheet after changes were made.
    - add_or_substract(data, amount, account_1, account_2): This makes all the addition and substraction given a dictionary, the accounts and the amount. Print error messages for inexisting accounts.
    - operation(dictionary, key, id, amount): Taking the dictionary, key, id and amount, this function checks if the amount is less than zero for accounts different from Accumulated amortization and depretiation.
    - actualization_date(answer): Given a yes/no answer, if answer == yes, returns the actual date in yyyy-mm-dd format.
    - add_money_format(number): Takes an int and returns as a string with "$" symbol on the side.
    - quit_money_format(number): Takes an str made of a "$" symbol and a number to the right and returns that number as an int.
    - totals(dictionay): Makes the addition of the subtotals and totals accounts and checks if Assets = Equity + Liabilities is correct.
    - totals_2(lista, inicial, final, account): Takes a list, its first and final index and the account name(can be "assets" or "liabilities and equity"), and makes the sum of the subtotals. This lists(lista) are the subtotals of the balance sheet.

- Final comments

I would like to say that some fun and hard time working with this project because of it's incremental difficulty when I firts started it, and I hope that somebody finds it useful one day.
