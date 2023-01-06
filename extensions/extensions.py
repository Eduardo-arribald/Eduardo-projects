
file = list(input("File name: "))


for i in range(len(file)):
    if file[i] == ".":
        file[i] = "/"
        break
    else:
        continue

file = ''.join(file)

print(file)
