
def main():
    x = input().split()
    for i in x:
        if i in [":)", ":("]:
            x[i] = convert(i)
    print(' '.join(x))


def convert(face):
    if ":)" == face:
        return 🙂
    elif ":(" == face:
        return 🙁

main()