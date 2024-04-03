""" 
goal/understanding: 
0.1 
semi-annual raise by a percent 

strategy:
0.1
range function(start,stop,step)? -
variable to count it each time till 6 ? + -
generate a sequence with range and search if the number is in this sequence 

implimentation:


evaluation:
1000 + 1000m * (0.04/12 + 1)


 """
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0

annual_salary = int(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))   
semi_annual_raise = float(input("Enter semi-annual raise, as decimal: "))
semi_annual_raise = semi_annual_raise + 1

arithmetic_sequence = list(range(6,999,6))
portion_down_payment = total_cost * portion_down_payment

while current_savings < portion_down_payment:
    if months in arithmetic_sequence:
        annual_salary = annual_salary * semi_annual_raise
    current_savings = (current_savings + annual_salary/12 * portion_saved + 
                       current_savings * r/12)
    months += 1
    print(current_savings, months)
    
print("Number of months: ",months,)


