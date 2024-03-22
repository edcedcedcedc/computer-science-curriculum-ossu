i = input("camelCase: ")
if i.islower():
    print("snake_case: ", i)
else:
    n = ""
    for w in i:
        if w.isupper():
            n += "_" + w.lower()
        else:
            n += w    
print(n)