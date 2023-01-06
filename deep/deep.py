
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
yes = ["42", "forty two", "forty-two"]
no = ["50", "fifty"]

if answer in yes:
    print("Yes")
elif answer in no:
    print("No")

