fname = input("Enter filename:")
if fname != "mbox-short.txt":
    fname = "mbox-short.txt"
fhandle = open(fname)
dict = dict()
largevalue = 0
largekey = ""
for i in fhandle:
    if i.startswith("From "):
        key = i.split()[1]
        """  if key not in dict:
                dict[key] = 1
            else:
                dict[key] += 1 """
        dict[key] = dict.get(key,0) + 1
for key,value in dict.items():
    if value > largevalue:
        largevalue = value
        largekey = key
print(largekey, largevalue)   