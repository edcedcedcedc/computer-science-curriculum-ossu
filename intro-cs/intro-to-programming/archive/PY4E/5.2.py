mylist = []

def maxval(mylist):
    largest = None
    for i in mylist:
        if largest is None or i > largest:
            largest = i
    return largest

def minval(mylist):
    smallest = None
    for i in mylist:
        if smallest is None or i < smallest:
            smallest = i
    return smallest


while True:
    num = input("Enter a number: ")
    if num == "done":
          print("Maximum is", maxval(mylist))
          print("Minimum is", minval(mylist))
          break
    try: 
        mylist.append(int(num))
    except:
         print("Invalid input")
         continue

    
