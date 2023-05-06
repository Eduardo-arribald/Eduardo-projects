from project import checker_of_the_amount_inputed, search_for_index, actualization_date, add_money_format, quit_money_format
import pytest

liabilities_list = [
    "Circulating Liabilities", "Providers", "Bank loans ST",
    "Various creditors", "Other liabilities ST", "Long term and\ndeferred liabilities",
    "Bank loans LT", "Accounts payable", "Other liabilities LT",
    "Deferred liabilities", "Total Liabilities"]
equity_list = ["Equity", "Social Capital",
    "Legal Reserve", "Retained earnings", "Total Equity", "Total Liabilities\nand Equity"]
Assets_list = [
    "Circulating assets", "Cash", "Banks", "Investments ST",
    "Accounts receivable", "Stock", "Other circulating assets",
    "Fixed and deferred assets", "Accounts receivable LT", "Investments LT",
    "Buildings and land", "Machinery", "Equipment", "Accumulated amortization and depretiation",
    "Deferred assets", None, "Total assets", "Date:", f"Last modification\ndate: {actual_date}"]
balance_sheet = {
    "Assets": Assets_list,
    "Amount_1": [f"$ {0}"]*15 +["",f"$ {0}"]+[""]*2,
    "Liabilities and Equity": liabilities_list + equity_list + [""]*2,
    "Amount_2": [f"$ {0}"]*10 + [""]+ [f"$ {0}"]*6 + [""]*2
    }
    balance_sheet["Amount_2"][11] = ""

def test_search_for_index():
    assert search_for_index(balance_sheet, "Cash") == "Assets", 0
    assert search_for_index(balance_sheet, "Machinery") == "Assets", 11


def test_function_2():
    ...


def test_function_n():
    ...
