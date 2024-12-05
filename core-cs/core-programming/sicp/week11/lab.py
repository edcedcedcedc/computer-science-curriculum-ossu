import time


""" 
exercise 1 delay thunk; function type as return value and int type value 

"""

def ex1():
    def delay(thunk, seconds=0.1):
        def delayed_computation():
            time.sleep(seconds)
            return thunk()
        return delayed_computation

    def force(thunk):
        return thunk()

    delayed_value = delay(lambda: 1 + 27)
    forced_value = force(delayed_value)

    
    print("Type of delayed_value:", type(delayed_value))
    print("Type of forced_value:", type(forced_value))
    print("Delayed value (function):", delayed_value)
    print("Forced value (evaluated):", forced_value)

"""  
ex 2 representation of a stream; lazy evaluation 

"""
class Stream:
    def __init__(self, head, tail):
        self.head = head       
        self.tail = tail

    def __repr__(self):
        return f"Stream({self.head}, <tail>)"

    def get_tail(self):
        if callable(self.tail):
            self.tail = self.tail()
        return self.tail

def cons_stream(head, tail):
    return Stream(head, tail)

def generate_numbers(n):
    return cons_stream(n,lambda:generate_numbers(n + 1))

#finite stream

fin_stream = cons_stream(1, lambda: cons_stream(2, lambda: cons_stream(3, lambda: [])))

fin_stream1 = fin_stream
print(fin_stream1.head) 

fin_stream2 = fin_stream1.get_tail()
print(fin_stream2.head)

fin_stream3 = fin_stream2.get_tail()
print(fin_stream3.head)

#infinite stream

inf_stream1 = generate_numbers(1)
print(inf_stream1.head)

stream2 = inf_stream1.get_tail()
print(stream2.head)

stream3 = stream2.get_tail()
print(stream3.head)

#generator; another form of lazy evaluation 

def generator(n):
    for i in range(n):
        yield i

for x in generator(10):
    print(x)



# lazy squares

class LazySquares:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

lazy_squares = LazySquares(5)

print(next(lazy_squares))
print(next(lazy_squares))
print(next(lazy_squares))




""" 
ex 3 

 """

# Eager computation
def enumerate_interval(low, high):
    if low > high:
        return [] 
    return [low] + enumerate_interval(low + 1, high)

def delay(expr):
    return lambda: expr  # thunk

def stream_enumerate_interval(low, high):
    if low > high:
        return 
    yield low 
    yield from stream_enumerate_interval(low + 1, high)

 # Thunk that stores a fully computed list
delayed_list = delay(enumerate_interval(1, 3)) 

# A generator for lazy iteration
stream = stream_enumerate_interval(1, 3)  

# Accessing delayed values, for all the values computed at once and stored in a thunk
print("Delayed list computation (thunk):", delayed_list()) 

# Accessing stream values, that are computed one at a time
print("Stream values (lazy):")
for val in stream:
    print(val)  