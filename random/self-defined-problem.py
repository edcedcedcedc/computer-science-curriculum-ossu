#problem 0
#square a list of numbers using recursion
 
integers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

def squares(param):
    if len(param) == 1:
        return param
    else:
        current = param.pop()
        return squares(param) + [square(current)]

print(squares(integers))

#problem 1
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        value2 = fib(n - 2) + fib(n - 1)
        return value2

#0 1 1 2 3 5 8 11
#print(fib(10))


#problem 2
#stick the previous element to current element using recursion, return a string

def sticker(para):
    if len(para) == 1:
        return para
    else:
        return para + sticker(para[1:])

#print(sticker('ab'))

#problem 2a
#what's the complexity of problem2 ?

#Because the substring is being created on each recursive that is n * n, so n^2

#problem 3
#extend problem 1 to return a list instead of a string, i.e each element must me isolated
#example ab => [ab, abb]


