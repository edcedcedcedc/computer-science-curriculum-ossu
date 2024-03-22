import re


def main():
    print(count(input("Text: ")))


def count(s):
    if matches := re.findall(r"\b(u|U)(m|M)\b", s):
        return len(matches)
    else:
        return 0


if __name__ == "__main__":
    main()
