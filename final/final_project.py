
"""
> What will your software do? What features will it have? How will it be executed?
   I will make a program for countability administration of startups, in a simple and comprehensible way.
   Features:
   Presentation of assets, passives, and capital(elements of a general balance) and information of a statement of income.
   This information will be easily watchable in an excel file.

> What new skills will you need to acquire? What topics will you need to research?
   Knowledge of all the information under a basic balance sheet and a statement of income.

> In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish less
  in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome?
   The best outcome would be an excel sheet in wich you could see all the information inputed, sorted and easily readable.
   A good outcome would be an excel sheet with just the statement of income of all the information inputed, sorted and easily readable.
   A better outcome would be a combination of these two.

Based in the book: Contabilidad para PYMES, FAECO.

libraries:
import xlsxwriter as xl
import openpyxl as op
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles.borders import Border, Side
from openpyxl.styles import Font
from openpyxl.worksheet.filters import AutoFilter
   """
import xlsxwriter as xl
import openpyxl as op
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles.borders import Border, Side
from openpyxl.styles import Font
from openpyxl.worksheet.filters import AutoFilter


def main():
    print("Hi, this is an Enterpreneur Simple Administration Program, or ESAP.", n/,
          "You can enter information about your company to get a simple administrative", n/,
          "visualizer of your Balance Sheet and your Income statement that will be returned in", n/,
          "a excel file if prefered, and you can manage dates and amounts entered to get the", n/,
          "financial control of your company.")
    question_1 = input("Is this a new report? (yes/no)").lower()
    dates(question_1)
    question_2 = input("Are we working with Assets, Liabilities or Equity?")

#These three functions will have to be tested with pytest.
#


def search_for():
    #A function that will search for the right accounting item in a given range.
    #This given range
    print("idk what this is going to do.")

def clasify_assets_liabilities_equity():
    #This function clasifies the amount entered based on the information given by the
    #user.

    print("idk what this is going to do x2.")

def dates_boolean(question_1):
    if question_1 == "yes":
        return True
    else:
        return False

def dates(question_1):
    if dates_boolean(question_1):
        print("idk what this is going to do x3.")


if __name__ == "__main__":
    main()