
import sys
from PIL import Image
from PIL import ImageOps as op
from os.path import splitext

def main():
    files = sys.argv
    files_1 = [1, "before1.jpg", "after.jpg"]
    files_2 = [1, "before.png", "after.jpg"]
    files_3 = [1, "before.png", "after.png"]
    files_4 = [1, "before.png", "after.png"]
    files_5 = [1]
    costumes(files_1)


def costumes(file):
    x = splitext(file[1])
    y = splitext(file[2])
    print("x =", x)
    print("y =", y)
    extensions = [".jpg", ".jpeg", ".png"]
    if len(file) == 3 and x[1] in extensions and y[1] in extensions:
        if x[1] == y[1]:
            #try:
            images = []
            mupet = file[1]
            print(mupet)
            with Image.open(mupet) as mupet:
                shirt = Image.open("shirt.png")
                print("Shirt:",shirt.size)
                print("Mupet:",mupet.size)
                mupet_size = mupet.size
                shirt = op.fit(shirt, size = mupet.size)
                mupet_with_shirt.paste(shirt, shirt)


                #p_2 = ImageOps.fit(p_1)
                #Image.paste
                #Image.save


        else:
            sys.exit("Input and output have different extensions")

    elif len(file) > 3:
        sys.exit("Too many command-line arguments")
    elif len(file) < 3:
        sys.exit("Too few command-line arguments")
    elif x[1] not in extensions or y[1] not in extensions:
        sys.exit("Invalid input")

    """
    image1 = Image.open("costume1.gif")
    image2 = Image.open("costume2.gif")
    images.append(image1)
    images.append(image2)

    images[0].save(
        "costumes.gif",
        save_all = True,
        append_images = [images[1]],
        duration = 200,
        loop = 0
    )"""

main()