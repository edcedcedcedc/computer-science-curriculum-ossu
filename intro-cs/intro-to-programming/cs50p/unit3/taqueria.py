d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

t = 0

while True:
    try:
        i = input("Item:").title().strip()
        for k in d:
            if k == i:
                t = t + d[i]
                print("Total:${:.2f}".format(t))
                break
    except EOFError:
       exit()


    