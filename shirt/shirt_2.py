import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirtfile = 