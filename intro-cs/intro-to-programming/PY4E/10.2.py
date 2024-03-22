fname = input("Input the filename: ")
if fname != "mbox-short.txt":
    fname = 'mbox-short.txt'
fhandle = open(fname)
lst = list()
tuple = tuple()
dict = dict()
for i in fhandle:
    if i.startswith("From "):
        key = i.split()[5].split(":")[0]
        dict[key] = dict.get(key, 0) + 1       
dict_sorted = sorted(dict.items())

""" dict_sorted_swapped = sorted(map(lambda tuple: (tuple[1],tuple[0]), dict.items())) """


list(map(lambda tuple: print(tuple[0],tuple[1]), dict_sorted))
