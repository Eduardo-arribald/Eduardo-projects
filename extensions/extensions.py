

file = ''.join((input("File name: ").lower().split()))

#print(file)

file = file.split(".")

#print(file[-1])

info = {
    "gif":"image/gif",
    "jpg":"image/jpeg",
    "jpeg":"image/jpeg",
    "png":"image/png",
    "pdf":"application/pdf",
    "txt":"text/plain",
    "zip":"application/zip",
}

def checking(doc):
    if doc[-1] in info.keys():
        for k in info:
            match doc[-1]:
                case k:
                    print(info.get(k))
                    break
    else:
        print("application/octet-stream")

checking(file)