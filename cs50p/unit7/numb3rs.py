import re

"""
goal: validate an ipv4
4 decimal numbers 0-255 inclusive 
3 dots 
strategy:
validate numbers 0-255 inclusive 
validate only 3 dots 
implimentation:
regexp
evaluation:
myself test and pytests
 """


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.match(
        r"(((1\d?\d?|[2-9]\d|2[0-5][0-5])|((21|22|23|24)\d)|0)\.){3}((1\d?\d?|[2-9]\d|2[0-5][0-5])|((21|22|23|24)\d)|0)$",
        ip,
    ):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
