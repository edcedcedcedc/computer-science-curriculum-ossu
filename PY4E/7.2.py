fname = input("Enter file name: ")
fh = open(fname)
x = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = x + 1
    average += float(line[line.find(":")+2:-1])
print('Average spam confidence:', average/x)