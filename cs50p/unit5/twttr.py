def main():
    print("Output:", shorten(input("Input: ")))
    

def shorten(para):
    c = 'aeiouAEIOU'
    r = ""
    for l in para:
        if l not in c:
            r += l
            r.strip()
    return r



if __name__ == "__main__":
    main()