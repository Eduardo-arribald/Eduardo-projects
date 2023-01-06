
greet = input("Greeting: ").lower().split()

first = list(greet[0])[0:5]

hello = list("hello")

print(first)

if hello == first:
    print("simon")
elif first[0]=="h":
    print("también")
else:
    print("mal")

#greet_list = list(greet)


#print(greet_list[0])
#print(str(list(greet)))

#if ["hello", "hello", "hello.", "hello"] in greet:
    #print("$0")

