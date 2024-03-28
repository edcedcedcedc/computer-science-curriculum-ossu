import re

count = 0

input_str = input()

if matches := re.findall("bob", input_str):
    
    print(f"Number of times bob occurs is: {matches}")

