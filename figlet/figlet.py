
from pyfiglet import Figlet
import sys

figlet = Figlet()

def main():
    fonts = figlet.getFonts()
    #check if 2 arguments were given.
    if len(sys.argv) == 3:
        #Check if those arguments are valids.
        if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fonts:
            #sys.argv[1]
            #figlet.getFonts()
            figlet.setFont(font = sys.argv[2])
            x = input("Input: ")
            print(figlet.renderText(x))
        #if not valids, print an error message.
        else:
            #print("Invalid usage")
            print("Invalid usage")
            sys.exit()
    #if no arguments given, prompt the input message anyway.
    elif len(sys.argv) == 1:
        x = input("Input: ")
        print(figlet.renderText(x))
    #If one argument given, prompt an error message.
    elif len(sys.argv) == 2:
        print("Invalid usage")
        sys.exit()
        print("Invalid usage")
        sys.exit()

main()

#print(figlet.getFonts())
