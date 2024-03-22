def main():
    while True:
        try:
            print(gauge(convert(input("Fraction:"))))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(param):
    x, y = param.split("/")
    if int(x) / int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError
    else:
        i = int(x) / int(y)
        return round((i * 100))


def gauge(param):
    if param >= 99:
        return "F"
    elif param <= 1:
        return "E"
    else:
        return f"{param}%"


if __name__ == "__main__":
    main()
