
from pyfiglet import Figlet
import sys

figlet = Figlet()

def main():
    fonts = figlet.getFonts()
    if len(sys.argv) == 3:
        if (sys.argv[1] == '-f' or sys.argv[1] == '-font') and sys.argv[2] in fonts:
            #sys.argv[1]
            #figlet.getFonts()
            figlet.setFont(font = sys.argv[2])
            x = input("Input: ")
            print(figlet.renderText(x))
    elif len(sys.argv) == 1:
        x = input("Input: ")
        print(figlet.renderText(x))
    else:
        print("Invalid usage")
        sys.exit()
main()

#print(figlet.getFonts())
