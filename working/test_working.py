from working import convert

def main():



def true_test():
    assert convert("9:00 AM to 5:00 PM") == "9:00 AM to 17:00 PM"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == ""


if __name__ == "__main__":
    main()