x,y = input().split()
for i in range(int(x)):
    for j in range(int(y)):
        if j == len(range(int(y))) - 1:
           print('#')
        else:
           print('#', end='')