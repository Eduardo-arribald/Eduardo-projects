
file = input("File name: ").split(".")

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
    for k in info:
        if k == doc[1]:
            print(info.get(k))
            break
        elif doc[1] not in info.keys():
            print("application/octet-stream")

checking(file)