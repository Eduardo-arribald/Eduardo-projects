

camel = input("camelCase: ").split()

camel = list(''.join(camel))

for i in range(len(camel)):
    if camel[i].isupper() and camel[i] != camel[0]:
        camel[i] = "_"+ camel[i].lower()

print("snake_case:", ''.join(camel))


