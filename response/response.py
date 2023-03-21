from validator_collection import checkers


def main():
    #emails = ["arriaga_@outlook.com", "malan@harvard.edu", "malan@@@harvard.edu", "arriaga_@outlook..com"]
    #checker(emails)
    print(checker(input("What's your email address? ")))


def checker(email):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
