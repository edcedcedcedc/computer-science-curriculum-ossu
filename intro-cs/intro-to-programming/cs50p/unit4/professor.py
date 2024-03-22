""" 
understanding/goal:

A proffesor plus game where I have to randomly generate x and y, 
depending on 3 lvls,each lvl n represent number of digits , propose the problems
give three tries, help if greater then three, represent the score out of 10, so 10 problems

review understanding after finishing writing code and all correct answers:

Accepts an n in the range of inclusive 1-3 which are the number of digits to a random generated
two numbers for addition.
The incorrect answers i.e numbers and strings are interpreted as EEE.
The key logic feature is that EEE when sums to 3 should subract the main while t variable 
other wise it creates an infinite loop in context of EEE.


strategy:

get lvl while loop
get lvl exceptions 
generate random ints based on lvl
main game loop 
propose problems get lvl
count problems
main game loop exceptions reprompt
EEE reprompt condition and hint if > 3
print result 
if problems > 10 print score 

implementation:

evaluation:

review with main loop ordering.
review with i in all program.
review with t 
review with s
incorrect logic of EEE if all three attempts were incorrect 
 """

import random


def main():
    s = 0
    c = 0
    t = 10
    l = get_level()
    while True:
        try:
            x = generate_integer(l)
            y = generate_integer(l)
            if t == 0:
                print("Score:", s)
                exit()
            i = int(input(f"{x} + {y} = "))
            t -= 1
            if x + y == i:
                s += 1
                continue
            else:
                raise ValueError
        except ValueError:
            while True:
                try:
                    print("EEE")
                    c += 1
                    i = int(input(f"{x} + {y} = "))
                    if c == 2:
                        print("EEE")
                        print(f"{x} + {y} = {x + y}")
                        c = 0
                        break
                    elif x + y == i:
                        s += 1
                        break
                except ValueError:
                    if c == 2:
                        print(f"{x} + {y} = {x + y}")
                        t -= 1
                        c = 0
                        break
                else:
                    pass


def get_level():
    while True:
        try:
            i = int(input("Level: "))
            if i > 3:
                raise ValueError
            elif i < 1:
                raise ValueError
            else:
                return i
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
