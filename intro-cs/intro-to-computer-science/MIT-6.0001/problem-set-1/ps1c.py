""" 
goal/understanding: 
0.3
the best savings rate as a function of starting salary
house price 1kk
in 36 months
best savings rate = best portion_saved
two decimal of accuracy
so an integer in range 0 and 10000
and then convert it to decimal percentage 
to use when we are calculating the current_savings after 36 months 
current_saving might be within 100$ of required down_payment so -100 +100 from 250k
0.4
monthly_rate -> infinity then months(monthly_rate) -> 0
monthly_rate -> 0 months(monthly_rate) -> infinity
0.5
I need to find the minimum salary to be able to invest in the portion down payment and get it done in 36 months 
for example with 10k it's impossible 


strategy:
0.1
bisection search ?
0.2
example of bisection search - divides the searched magnitude and compares it with sought
if value is greater then sought value set it to be the new high point for the interval
if the value is less then sought value set it to be the new low point for the interval

implimentation:
0.3
low = 0.0 
high = max(0,10000)
average = (high + low)/2
rate = average/10000
steps = 0
0.4
if months > 36 or amount < 249900
low = average 
if months < 36 or amount > 250100
high = average 

if m

0.5 33 2544
months are less 
5000 new high point 
5000 + 0/2/10000

0.25
months are too high
2500 new low point 
5000 + 2500/2/10000

0.375
months are too high
3750 new low point
5000 + 3750/2/10000

0.4375
months are too high
4375 new low point
5000 + 4375/2/10000

0.4687
months are too low
4375 new high point
4687 + 4375/2/10000

0.4531

textbook example of bisection search: 
months 
x = -25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print ('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print ('numGuesses =', numGuesses)
print (ans, 'is close to square root of', x)

evaluation:



 """
def main():
    annual_salary = int(input('Enter starting salary: '))
    monthly_rate, steps = best_savings_rate(annual_salary)

    if monthly_rate and steps is not None:
        print('Best savings rate: ', monthly_rate,"\n",'Steps in bisection search: ', steps, sep="")
    else:
        print('It is not possible to pay the down payment in three years.')

def best_savings_rate(annual_salary):
    low = 0
    high = 10000
    steps = 0
    epsilon = 100
    is_savings_possible = lambda average: False if average == 9999 else True

    while True:
        steps += 1
        average = int((high + low)/2)
        monthly_rate = float(average/10000)
        months, current_savings = savings(annual_salary, monthly_rate)
        print(months, current_savings, high, low, average)
        if is_savings_possible(average):
            if months > 36 or current_savings < (250000 - epsilon):
                low = average
            elif months < 36 or current_savings > (250000 + epsilon):
                high = average
            else:
                return (monthly_rate, steps)
        else:
            return (None, None)


def savings(annual_salary, monthly_rate):
    annual_return_rate = 0.04
    current_savings = 0
    months = 0
    total_cost = 1000000 
    semi_annual_raise = 0.07 + 1
    portion_down_payment = total_cost * 0.25

    while current_savings < portion_down_payment:
        if months in list(range(6,999,6)):
            annual_salary = annual_salary * semi_annual_raise
        current_savings = (current_savings + annual_salary/12 * monthly_rate + 
                        current_savings * annual_return_rate/12)
        months += 1

    return (months, int(current_savings))   

main()