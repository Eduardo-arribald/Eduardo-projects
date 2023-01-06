
file = input("File name: ").split(".")

info = {
    {"termination":"gif", "type":"image/gif"},
    {"termination":"jpg", "type":"image/jpeg"},
    {"termination":"jpeg", "type":"image/jpeg"},
    {"termination":"png", "type":"image/png"},
    {"termination":"pdf", "type":"application/pdf"},
    {"termination":"txt", "type":"text/plain"},
    {"termination":"zip", "type":"application/zip"},
}

def main():
    checking

print(file)

def checking(doc):
    for kind in info:
    if file[i] == ".":
        file[i] = "/"
        file = ''.join(file)
        print(file)
        break
    elif "." not in file:
        print("application/octet-stream")
        break"""