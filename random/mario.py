y = int(input())
for i in range(y):
    print((y - i) * " ", end='',sep='')
    for j in range(i+1):
        if j == len(range(i+1)) - 1:
           print('#' + 2 * " ", end='', sep='')
           for j in range(i+1):
               if j == len(range(i+1)) - 1:
                  print('#')
               else:
                  print('#', end='')
        else:
           print('#', end='')