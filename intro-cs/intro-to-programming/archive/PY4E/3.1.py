hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs = float(hrs)
rate = float(rate)
pay = 0.0
if float(hrs) > 40:
    pay = ((hrs - 40) * rate * 1.50) + (40.0 * rate)
    print("Pay + Overpay:", pay)
else:
    pay = hrs * rate
    print("Pay:", pay)