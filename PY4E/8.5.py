inp = input("Enter file name:")
if len(inp) < 1: inp = "mbox-short.txt"
fhandle = open(inp)
c= 0
for i in fhandle:
    if i.startswith("From "):
        lst = i.split()
        print(lst[1])
        c += 1
print(f"There were {c} lines in the file with From as the first word")
    
