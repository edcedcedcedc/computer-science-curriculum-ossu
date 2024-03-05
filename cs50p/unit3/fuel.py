while True:
    try:
        x, y = input("Fraction:").split("/")
        i = int(x)/int(y)
    except (ValueError, ZeroDivisionError, IndexError):
        pass
    else:
        if i > 1:
            continue
        elif i >= 0.99:
            print("F")
            break
        elif i <= 0.01:
            print("E")
            break
        else:
            print(f"{round((i * 100))}%")
            break