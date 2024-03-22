""" 
goal/understanding:
    prompt for an n, randomly generate another n in the range 1 no n inclusive 
    promt for a guess, if smaller then n too small, greater too large, the same just right 
strategy:
prompt for number
validate
generate random
promp for guess
condition guess
print
break
implimentation:



evaluation:



 """

import random

while True:
    try:
        n = int(input("Level:"))
        r = random.randint(1, n)
        while True:
            try:
                g = int(input("Guess:"))
                if g > r:
                    print("Too large!")
                elif g < r:
                    print("Too small!")
                else:
                    print("Just right!")
                    exit()
            except ValueError:
                pass
    except ValueError:
        pass
