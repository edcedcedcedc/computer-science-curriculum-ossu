i = input("Greeting:").lower().strip()
if i.startswith("hello"):
    print("$0")
elif i.startswith("h") and i is not "hello":
    print("$20")
else:
    print("$100")