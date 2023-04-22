
#Score 6/12
#Not submited

import sys
from PIL import Image #https://pillow.readthedocs.io/en/stable/reference/Image.html
from PIL import ImageOps as op #https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit
from os.path import splitext #https://docs.python.org/3/library/csv.html#csv.DictWriter

def main():
    files = sys.argv
    #files = [1, "before1.jpg", "after.jpg"]
    costumes(files)


def costumes(file):
    extensions = [".jpg", ".jepg", ".png"]

    #I have to check up for the lenght of the given list.
    if len(file) == 3:
        x = splitext(file[1])
        y = splitext(file[2])
        mupet = file[1]
        new_mupet = file[2]
        #Then I look up for the correct extensions.
        if x[1] == y[1] and x[1] in extensions and y[1] in extensions:


            #Here is where I have to create the wished picture.
            #with Image.open(mupet) as mupet:
            with Image.open("shirt.png") as shirt:
                homework_way(shirt, mupet, new_mupet)
                #homework_way(shirt, mupet, new_mupet)


        #When the first file(x) doesn't have the correct extension.
        if x[1] not in extensions:
            sys.exit("Invalid input")
        #When the second file(y) doesn't have the correct extension.
        if y[1] not in extensions:
            sys.exit("Invalid output")
        if y[1] in extensions and x[1] in extensions and x[1] != y[1]:
            sys.exit("Input and output have different extensions")

    #If the lenght is different from 3, I have to exit and print a message.
    elif len(file) > 3:
        sys.exit("Too many command-line arguments")
    elif len(file) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Invalid input")



#Look for the hints.
#Use fit.

def homework_way(camisa, marioneta, nueva_marioneta):
    mupet = marioneta
    shirt = camisa
    new_mupet = nueva_marioneta
    #w, l = mupet.size
    size = shirt.size
    #scales = (w/w_s, l/l_s)
    """The way of the homework"""
    #mupet_size = (w, l)
    mupet = op.fit(mupet, size)
    mupet.paste(shirt, shirt)
    sys.exit(mupet.save(new_mupet))

if __name__ == "__main__":
    main()

