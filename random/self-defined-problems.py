#problem 0
#square a list of numbers using recursion
 
from datetime import datetime


integers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

def squares(param):
    if len(param) == 1:
        return param
    else:
        current = param.pop()
        return squares(param) + [square(current)]

#print(squares(integers))

#problem 1
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

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

#problem 4
#write a permutation function using recursion 

#problem 5
#impliment memoization to problem 1

#understanding
#a memo wrapper around fib
#domain numbers and dictionary range fn
#fib memo handles cache checking and calls fib

#strategy
#check the cache in fib memo each recursive call
#on the return from the recursive call append to assoc 

def fib_memo(n,cache,calls):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n
    else:
        result = fib_memo(n - 2, cache, calls + 1) + fib_memo(n - 1, cache, calls + 1)
        cache[n] = result
        return result



#problem 6
#get the arithmetic sum of an arithmetic sequence using arithmetic sum formula 

#understanding
#input n as the length of the list 
#k, k+1, k+2, k+3, k+n-1 - ascending
#k+n-1, k+n-2,k+n-3,k+n-4 - descending
#k+n-1 last element, k first element 
#k=1
#n=5
#1+(5-1),1+(5-2),1+(5-3),1+(5-4),1+(5-5)
#S_n = n/2(2a + (n - 1))

def problem6():
    n = int(input())
    a = 1
    sum1 = round(n/2 * (2*a + (n - 1)))
    print(sum1)


#problem 6a
#extend problem6 by using i to shift positive 

def problem6a():
    n = int(input())
    i = int(input())
    a = 1
    sum1= round((n + i)/2 * (2*a + ((n + i) - 1)))
    print(sum1)

#problem 6b
#modify problem 6b to shift i negative 

def problem6b():
    n = int(input())
    i = int(input())
    a = 1
    sum1= round((n - i)/2 * (2*a + ((n - i) - 1)))
    print(sum1)



#problem 6c 
""" 
#understanding:
you are given an array of length n that contains integers starting from k
and increasing by 1 for each element

a = k,k+1,k+2,k+n-1

for a given index i  1<= i <= n split the array into two parts

the sum of the first i elements  S1 = a_1 + a_2 + a_3 +...+ a_i
the sum of the remaining elements from i + 1 to n, S2 = a_i+1,a_i+2,a_n

for each possible index i calculate the absolute difference x = |S1 - S2|
find the index i that minimizes x

#strategy:
n - length
k - start
i - index
sum1 = round((n - i / 2) * (2*a + ((n - i) - 1)))
"""
def problem6c():
    n = int(input())
    a = int(input())
    mininum = float('inf')
    for i in range(n):
        sum1 = round((i / 2) * (2*a + (i - 1)))
        sum2 = round((n / 2) * (2*a + (n - 1))) - sum1
        adiff = abs(sum1 - sum2)
        if adiff < mininum:
            mininum = adiff
    print(mininum)
#problem 6d:
#extend problme 6c with binary search and bonuses :)
#

def problem6d():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        low = 1
        high = n
        min = float('inf')
        sumt = n * (2 * k + (n - 1)) // 2
        while low <= high:
            mid = (low + high) // 2
            sum1 = mid * (2 * k + (mid - 1)) // 2
            sum2 = sumt - sum1
            if sum1 < sum2:
                low = mid + 1
            else:
                high = mid - 1
            diff = abs(sum1 - sum2)
            if diff < min:
                min = diff    
        print(min)
problem6d()
