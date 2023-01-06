
file = list(input("File name: "))


for i in range(len(file)):
    if file[i] == ".":
        file[i] = "/"
    else:
        continue



print(str(file))
