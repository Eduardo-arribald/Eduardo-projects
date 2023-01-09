
from pyfiglet import Figlet
import sys

figlet = Figlet()

def main():
    fonts = figlet.getFonts()
    """if there are 2 arguments"""
    if len(sys.argv) == 3:
        """Check if the first is a valid one and the second is an existing font"""
        if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fonts:
            #sys.argv[1]
            #figlet.getFonts()
            figlet.setFont(font = sys.argv[2])
            x = input("Input: ")
            print(figlet.renderText(x))
        """if the first is not a valid command or the second is not in the list of fonts,
        print an error message."""
        else:
            print("Invalid usage")
            print("Invalid usage")
            sys.exit()
    elif len(sys.argv) == 1:
        x = input("Input: ")
        print(figlet.renderText(x))
    """elif len(sys.argv) == 2:
        #print("Invalid usage")
        print("Invalid usage")
        sys.exit()
"""

main()

#print(figlet.getFonts())
