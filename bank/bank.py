greet = input("Greeting: ").lower().split()

print(list(greet))
print(str(list(greet)))

if "hello" in greet:
    print("$0")