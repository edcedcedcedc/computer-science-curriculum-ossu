import threading

#101: P1 sets x to 100 and then P2 increments x to 101.
#121: P2 increments x to 11 and then P1 sets x to x * x.
#110: P2 changes x from 10 to 11 between the two times that
#P1 accesses the value of x during the evaluation of (* x x).
#11: P2 accesses x, then P1 sets x to 100, then P2 sets x.
#100: P1 accesses x (twice), then P2 sets x to 11, then P1 sets x.
#We can constrain the concurrency by using serialized procedures, which

x = 10

lock = threading.Lock()

def func1():
    global x
    try:
        lock.acquire()
        x = x * x
    finally:
        lock.release()

def func2():
    global x
    try:
        lock.acquire()
        x = x + 1
    finally:
        lock.release()

def parallelism():
    global x
    thread1 = threading.Thread(target=func1)
    thread2 = threading.Thread(target=func2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    return x

print(parallelism())


#the possibility P1