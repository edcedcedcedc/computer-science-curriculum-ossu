hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs = float(hrs)
rate = float(rate)

def computepay(hrs, rate):
    pay = 0.0
    if float(hrs) > 40:
        pay = ((hrs - 40) * rate * 1.50) + (40.0 * rate)
        return pay
    else:
        pay = hrs * rate
        return pay

print("Pay:", computepay(hrs, rate))