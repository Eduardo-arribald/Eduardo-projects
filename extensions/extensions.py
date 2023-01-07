

file = ''.join((input("File name: ").lower().split()))

file = file.split(".")

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
        if doc[2] is not None:
            match doc[2]:
                case k
                print(info.get(k))
                break
            case _:
                continue
        elif k == doc[1]:
            print(info.get(k))
            break
        elif doc[1] and doc[2] not in info.keys():
            print("application/octet-stream")
            break

checking(file)