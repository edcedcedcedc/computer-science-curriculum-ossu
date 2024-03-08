""" 
understanding/goal:
input Name: 0 n-1 names, 
output Adieu, adieu, to name, name, and name


strategy:

if names == 2 insert and before the last name 


implementing:


evaluation:
len i - 2 == i then last i is i + 1
 """

prefx = "Adieu, adieu, to "
postfx = "and "
l = []
s = ""

while True:
    try:
        i = input("Name:")
        if len(i) == 0:
            raise EOFError
        else:
            l.append(i)
    except EOFError:
        if len(l) - 1 == 0:
            print(prefx + l[0])
        elif len(l) - 1 == 1:
            print(prefx + l[0].strip() + " " + postfx + l[1])
        else:
            for i in range(len(l)):
                s = s + l[i].strip() + "," + " "
                if len(l) - 1 == 0:
                    print(prefx + l[i])
                elif len(l) - 1 == 1:
                    print(prefx + l[i].strip() + " " + postfx + l[i + 1])
                elif len(l) - 2 == i:
                    print(prefx + s + postfx + l[i + 1])
                    break
        exit()
