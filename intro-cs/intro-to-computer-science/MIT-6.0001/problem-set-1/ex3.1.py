""" 
brute force algorithm or exaustive enumeration 
with incremental and decrimental functions of the loop examples
 """

""" x = int(input("Enter an integer: "))
ans = 0
while ans**3 < abs(x):
    print(abs(x) - ans**3)
    ans = ans + 1
if ans**3 != abs(x):
    print(x, "is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of", x, "is", ans)
 """

x = int(input("Enter an integer: "))
ans = 0
while abs(x) - ans**3 > 0:
    ans = ans + 1
if ans**3 != abs(x):
    print(x, "is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of", x, "is", ans)


