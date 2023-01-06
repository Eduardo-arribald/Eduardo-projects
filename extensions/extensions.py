
file = list(input("File name: "))


for i in range(len(file)):
    if file[i] == ".":
        file[i] = "/"
        file = ''.join(file)
        print(file)
        break
    elif "." not in file:
        print("application/octet-stream")
        break
    else:
        continue

