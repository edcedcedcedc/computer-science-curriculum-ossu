i = input("Expression: ").split()
if i[1] == "+":
    print("{:.1f}".format(float(i[0]) + float(i[2])))
elif i[1] == '-':
    print("{:.1f}".format(float(i[0]) - float(i[2])))
elif i[1] == '/':
    print("{:.1f}".format(float(i[0]) / float(i[2])))
else:
    print("{:.1f}".format(float(i[0]) * float(i[2])))