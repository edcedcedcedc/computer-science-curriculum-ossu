def main():
    i = input()
    c = convert(i)
    print(c)

def convert(str):
        return str.replace(':)', '🙂').replace(":(", '🙁')

main()