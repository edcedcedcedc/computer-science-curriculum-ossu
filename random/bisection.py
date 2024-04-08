""" 
goal/understanding:
0.1
find a value using bisection search and predict the power of the program 
0.2
the time complexity of this is log2(1000) so around 9 iterations 
strategy:
initialize a random variable between 0-100
print variable 
use bisection search to find the value
print searching process 

implimentation:


evaluation:


 """
import random

random_value = random.randrange(1000)
print('random value', random_value)
low = 0
high = 1000
average = lambda high, low: int((high + low)/2)
value = average(high, low)
guesses = 0

while value != random_value:
    guesses +=1 
    if value > random_value:
        high = value
    elif value < random_value:
        low = value 
    value = average(high, low)
    print('high',high, 'low', low,'value', value)

print('random_value',random_value, 'value',value, 'guesses',guesses)