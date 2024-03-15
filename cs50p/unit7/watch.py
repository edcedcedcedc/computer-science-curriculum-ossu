import re

def main():
    print(parse(input("HTML: ")))
 
def parse(s):
    if _ := re.search(r'((http|https)://)?(www.)?youtube.com/embed/\S+(?=")', s):
        __ = re.search(r'(?<=youtube.com/embed/).+', _.group()).group()
        return f'https://youtu.be/{__}'
    else:
        return None
    
if __name__ == "__main__":
    main()