""" 
goal/understanding: 
return longest substring in alphabetical order

strategy:
assume first letter is in order 
compare it with next letter if it's greater then current 
accumulate to a variable till hit false 
from the next letter the same process till hit false in a new variable
compare the old accumulation length with new accumulation length

implimentation:
below

evaluation:
no assumption needed just comparation and only then accumulate 


re-understanding:
start with first letter 
compare current letter with next letter 
if current letter is less then next letter 
accumulate to current
compare current length with depot length 
    if current greater then depot change depot 
else current letter is greater then next letter
accumulate to current
because the current letter is true, I compared it in previous iteration 
for example 'beggha' h-a is false, current i is 'h'


 """

input_str = "abcbcd"

depo_str = ""

current_str = ""


for i in range(len(input_str)):

    if i == len(input_str) - 1:

        if input_str[i] >= input_str[i - 1]:

            if len(current_str) > len(depo_str):

                depo_str = current_str

            print(depo_str)

        else:

            print(depo_str)

    elif input_str[i] <= input_str[i + 1]:

        current_str += input_str[i]

        if len(current_str) > len(depo_str):

            depo_str = current_str

    else:

        current_str += input_str[i]

        if len(current_str) > len(depo_str):

            depo_str = current_str

        current_str = ""