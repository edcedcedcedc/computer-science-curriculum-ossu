MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

MONTH = 12
DAY = 31
YEAR = 2024
COMMA = ","
SLASH = "/"
WHITE_SPACE = " "


""" 
:) outdated.py exists
:( input of 9/8/1636 outputs 1636-09-08
    Did not find "1636-09-08" in "['9', '8', '16..."
:( input of September 8, 1636 outputs 1636-09-08
    Did not find "1636-09-08" in "['September', ..."
:( input of 10/9/1701 outputs 1701-10-09
    Did not find "1701-10-09" in "['10', '9', '1..."
:( input of October 9, 1701 outputs 1701-10-09
    Did not find "1701-10-09" in "['October', '9..."
:( input of " 9/8/1636 " outputs 1636-09-08
    Did not find "1636-09-08" in "['9', '8', '16..."
:) input of 23/6/1912 results in reprompt
:( input of 10 December, 1815 results in reprompt
    expected program to reject input, but it did not
:( input of October/9/1701 results in reprompt
    expected program to reject input, but it did not
:( input of 1/50/2000 results in reprompt
    expected program to reject input, but it did not
:) input of December 80, 1980 results in reprompt
:) input of September 8 1636 results in reprompt

 """


def main():
    while True:
        param = input("Date:").strip()
        try:
            if not COMMA in param and WHITE_SPACE in param:
                raise ValueError
            if COMMA in param and WHITE_SPACE in param:
                param = param.split(WHITE_SPACE)
                for i in range(len(param)):
                    if COMMA in param[i]:
                        param[i] = param[i].split(",")[0]
                m, d, y = param
                if m.isdigit():
                    raise ValueError
            else:
                param = param.split("/")
                m, d, y = param
                if not m.isdigit():
                    raise ValueError
                elif int(d) > 31:
                    raise ValueError
        except ValueError:
            pass
        else:
            b = is_v(param)
            if not b:
                continue
            else:
                m, d, y = b
                print("{}-{:02}-{:02}".format(int(y), int(m), int(d)))
                break


def is_v(param):
    m, d, y = param

    def ___(param):
        for i in range(len(MONTHS)):
            if MONTHS[i] == param:
                return str(i + 1)

    if m.isdigit():
        m = int(m)
        d = int(d)
        y = int(y)
        if m <= 12 or m in MONTHS:
            if d <= DAY and y <= YEAR:
                return (m, d, y)
            else:
                return False
        else:
            return False
    else:
        y = int(y)
        d = int(d)
        if m in MONTHS:
            if d <= DAY and y <= YEAR:
                return (___(m), d, y)
            else:
                return False
        else:
            return False


main()
