
from pyfiglet import Figlet

figlet = Figlet()

def main():
    figlet.getFonts()
    figlet.setFont(font = f)
    x = input("Input: ")
    print(figlet.renderText(x))