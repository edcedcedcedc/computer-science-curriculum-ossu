x = 123456
epsilon = 0.01
step = epsilon**3
numGuesses = 0
ans = 0.0
""" 
goal/understanding:
0.1
for example
if lim of (ans^2 -4) ans -> 0 then f(x) -> 4 
if lim of (ans^2 -4) ans -> 4 then f(x) -> 0
0.2
if lim of (ans^2 -4) ans -> 1 then f(x) -> 3 and ans -> 1
0.3
the number of iteration depend on how close ans is to 0



 """

while abs(ans**2 - x) > epsilon and ans*ans < x:
    ans += step
    numGuesses += 1
print ('numGuesses =', numGuesses)
if abs(ans**2 - x) > epsilon:
    print ('Failed on square root of', x)
else:
 print (ans, 'is close to square root of', x)