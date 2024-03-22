from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()

l = lambda: len(sys.argv) - 1
v = lambda x: sys.argv[x]
io = lambda: print("Output:",figlet.renderText(input("Input:")))

if l() < 1:
    figlet.setFont(font=random.choice(font_list))
    io()
elif (
    1 <= l() < 3
    and (v(1) == "-f" or v(1) == "--font")
    and v(2).strip().lower() in font_list
):
    figlet.setFont(font=v(2))
    io()
else:
    sys.exit("Invalid Usage")
