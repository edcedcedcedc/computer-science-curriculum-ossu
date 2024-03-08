""" 
understanding/goal:
terminal program with command line argument n, if the argument cannot be converted to float exit sys.exit
with an error message
query the api and among whos nested keys is the current bitcoin as float as, catch exceptions
output the n current cost of bitcoins in usd to four decimal places and ',' as a thosand separator 

strategy:
while try except block 
for handling input and input exceptions
query the api with get, check json, parse it,
get http exceptions 
format the output read about format in general a little 

implimentation:



evaluation:

 """
import requests
import sys

def is_decimal(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def _(d,key):
    for k, v in d.items():
        if k == key:
            r = d.get(key)['rate_float']
            return r 
        elif isinstance(v, dict):
            bc = _(v,key)
            if bc:
                return _(v,key)
            
try:
    if len(sys.argv) - 1 == 0:
        raise ValueError("Missing command-line argument")
    elif len(sys.argv) - 1 == 1 and not is_decimal(sys.argv[1]):
        raise ValueError("Command-line argument is not a number")
    else:
        try:
            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            r = r.json()
        except requests.RequestException as e:
            sys.exit(e)
        else:
            rate = _(r,'USD') 
            print(f"${rate * float(sys.argv[1]):,.4f}")
                            
except (ValueError, KeyError) as e:
    sys.exit(e)

    

