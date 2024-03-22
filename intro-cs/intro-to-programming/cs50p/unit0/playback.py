t = input().split()
n = ""
for i in range(len(t)):
    if i == 0 and i == len(t) - 1:
        n = t[i]
    elif i == len(t) - 1:
        n += t[i] 
    else:
        n += t[i] + "..."
print(n)