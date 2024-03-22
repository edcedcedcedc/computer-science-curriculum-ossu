def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        is_at_least_two_letters(s)
        and is_interval(s)
        and is_num_aggregate(s)
        and is_not_psp(s)
    )


is_not_psp = lambda param: "." not in param and "," not in param and " " not in param

is_interval = lambda param: 2 <= len(param) <= 6


def is_at_least_two_letters(s):
    if isinstance(s, int):
        return False
    else:
        for i in range(len(s)):
            if 0 == len(s) - 1:
                return False
            elif s[i].isdigit() and 1 == len(s) - 1:
                return False
            else:
                return True


def is_num_aggregate(param):
    for i in range(len(param)):
        if param[i].isdigit():
            s = split_at_first_digit(param)
            return is_first_digit_not_zero(s) and is_all_digits(s)
        elif i == len(param) - 1:
            return True


def split_at_first_digit(s):
    n = ""
    for i in range(len(s)):
        if s[i].isdigit():
            n = s[i:]
            break
    return n


def is_first_digit_not_zero(s):
    return not s.startswith("0")


def is_all_digits(s):
    return s.isdigit()


if __name__ == "__main__":
    main()
