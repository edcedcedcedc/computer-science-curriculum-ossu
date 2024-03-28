vowels = 'aeiou'

count = 0

input_str = input()

for i in range(len(input_str)):

    if input_str[i] in vowels:

        count += 1
        
print(count)
