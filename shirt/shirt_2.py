import sys
import Image


def main():
    check_command_line_arg()
    try:
        imagefile = Image.open(sys.argv[1])