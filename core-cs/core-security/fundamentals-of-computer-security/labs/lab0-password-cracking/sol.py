from hashall import toy_hash
from hashbig import *
from itertools import product
import string
import os

# return password, where toy_hash(password) = <HASH_OUTPUT_BY_GRADESCOPE>

""" 
Password is lowercase letters a-z.

You don't know the length upfront 
(maybe try from 1 up to a reasonable max, like 8 or 10, depending on expected difficulty).

Hash is truncated SHA256 (48 bits → 12 hex digits).

So the search space is exactly what you thought: 26^L for a word of length L.

1 hex = 4 bits 



 """


def problem_2a(target=""):
    MAX_L = 7
    a_z = string.ascii_lowercase
    for L in range(1, MAX_L + 1):
        for candidate in product(a_z, repeat=L):
            password = "".join(candidate)
            if target == "":
                if toy_hash(password.encode("ascii")).hex() == "3a7bd3e2360a":
                    return password
            elif toy_hash(password.encode("ascii")).hex() == target:
                return password


# return password, where toy_hash(password) is in hashes.txt
def problem_2c():
    password = None
    with open("hashes.txt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            print(line)
            password = problem_2a("59830ebc3a41")
            return password


print(problem_2c())


# return probability of being in bin k
def problem_3a(B, N):
    prob = None
    return prob


# return probability of both balls being in bin k
def problem_3b(B, N):
    prob = None
    return prob


# return number of ball pairs
def problem_3c(B):
    prob = None
    return prob


# return reasonable upper bound
def problem_3d(B, N):
    prob = None
    return prob


# return reasonable upper bound
def problem_3e(L, N):
    prob = None
    return prob


# return h1,h2 where H(h1) == H(h2)
def problem_4b():
    h1 = None
    h2 = None
    return h1, h2
