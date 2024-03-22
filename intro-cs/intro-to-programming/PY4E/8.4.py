read = input("Enter file name:")
if read != "romeo.txt":
    read = "romeo.txt"
fhandle = open(read)
str = fhandle.read().split()
new_lst = list()
for i in range(len(str)):
    if len(new_lst) == 0:
        new_lst.append(str[i])   
    else:     
        for j in range(len(new_lst)):
            if str[i] == new_lst[j]:
                 break
            elif j == len(new_lst) - 1:
                new_lst.append(str[i])
new_lst.sort()
print(new_lst)

    