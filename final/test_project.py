from project import checker_of_the_amount_inputed, search_for_index, actualization_date, add_money_format, quit_money_format
import pytest

def test_search_for_index():
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


def test_function_2():
    ...


def test_function_n():
    ...
