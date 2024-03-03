""" 
reasoning:
coke cost 50, this is the amount due;
machine accepts 5,10,25 only;
key points:
init a_due to 50, 
inserted as total, 
insert as action,
also due = change owed, it might be negative, so has to be absolute value

 """
a_inserted = 0
a_due = 50
print("Amount Due:", a_due)
while True:
    a_insert = int(input("Insert Coin:"))
    if a_insert != 5 and a_insert != 10 and a_insert != 25:
        print("Amount Due:", a_due) 
        continue
    else:    
        a_due = abs(a_due - a_insert)
        a_inserted += a_insert
        if a_inserted >= 50:
            print("Change Owed:", a_due)
            break
        else:
            print("Amount Due:", a_due) 



    


        