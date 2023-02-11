
#Score: 4/7
#Not submited

from pyfiglet import Figlet
import sys

figlet = Figlet()

def main():
    fonts = figlet.getFonts()
    #check if 2 arguments were given.
    if len(sys.argv) == 3:
        #Check if those arguments are valids.
        if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fonts:
            figlet.setFont(font = sys.argv[2])
            x = input("Input: ")
            if x != " " or x != "":
                print("Output:")
                print("")
                print(figlet.renderText(x))
            else:
                sys.exit()
        #if not valids, print an error message.
        else:
            sys.exit("Invalid usage")
    #if no arguments given, prompt the input message anyway.
    elif len(sys.argv) == 1:
        #x = input("Input: ")
        #print("Output:", figlet.renderText(x))
        sys.exit()
    #If one argument given, prompt an error message.
    elif len(sys.argv) == 2:
        sys.exit("Invalid usage")



main()

#print(figlet.getFonts())
