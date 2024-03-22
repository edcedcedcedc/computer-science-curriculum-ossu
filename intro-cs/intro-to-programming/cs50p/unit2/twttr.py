i = input("Input: ")
c = 'aeiouAEIOU'
r = ""
for l in i:
    if l not in c:
        r += l
        r.strip()
print("Output:",r)