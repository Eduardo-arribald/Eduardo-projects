
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

yes = [42, "Forty Two", "forty-two"]

if answer in yes:
    print("Yes")
elif answer == 50:
    print("No")