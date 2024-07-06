integers = [1, 2, 3, 4, 5]


def square(x):
    return x * x


def squares(param):
    if len(param) == 1:
        return param
    else:
        value = param.pop()
        return squares(param) + [square(value)]




def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        value2 = fib(n - 2) + fib(n - 1)
        return value2

#0 1 1 2 3 5 8 11
print(fib(10))
