def main():
    print(meal(convert(input("What time is it ?: "))))

def meal(time):
    if 7.0 <= time <= 8.0:
        return "breakfast time"
    elif 12.0 <= time <= 13.0:
        return "lunch time"
    elif 18.0 <= time <= 19.0:
        return "dinner time"
    else:
        return ""

def convert(time):
    hours, minutes = time.split(":")
    return float("{:.2f}".format(float(hours) + float(minutes)/60.0))

if __name__ == "__main__":
    main()