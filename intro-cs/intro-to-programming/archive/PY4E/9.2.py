""" 
read input 
open handler 
read file, iterate over it
parse by line that starts with 
split 
look up for word index 
iterate over dictionary 
add key 
count how many times key occurs
print key, value
 """
""" dict = dict()
fname = input("Enter filename:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhandle = open(fname)
for i in fhandle:
    if i.startswith("From "):
        key = i.split()[2]
        print(key)
        dict[key] = dict.get(key,0) + 1 """
