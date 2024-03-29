""" 
goal/understanding: 
0.1 
to buy a house from saving in percent and return number of months 
0.2 
to invest in portion down payment which is 25 % of the house price 

total_cost - house price
portion_down_payment - 25% of the house price
current_saving - amount saved, start with 0
r - 4% annual return(each month an increase of 4% current_savings * (0.04/12 + 1))
annual_salary - salary 
portion saved - x% from the monthly salary 


strategy:
at the end of each month savings are going to increase by 4%
current savings * (0.04 + 1)/12
 + percentage of monthly salary 
0.1
init portion down payment
init current savings 
init r to 0.04
init months
input annual salary
input portion saved 
input total cost 

while loop current savings < 250000
current savings = annual salary/12 + current savings * r/12


implimentation:


evaluation:
0.1
wrong goal!!!! READ THE PROBLEM CAREFULLY!!!!!!!
0.2

            1000 + 1000m * (0.04/12 + 1)


 """
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0

annual_salary = int(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))   

while current_savings < (total_cost * portion_down_payment):
    current_savings = (current_savings + annual_salary/12 * portion_saved + 
                       current_savings * r/12)
    months += 1

print(months)