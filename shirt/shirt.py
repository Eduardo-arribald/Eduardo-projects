
import sys
from PIL import Image #https://pillow.readthedocs.io/en/stable/reference/Image.html
from PIL import ImageOps as op #https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit
from os.path import splitext #https://docs.python.org/3/library/csv.html#csv.DictWriter

def main():
    files = sys.argv
    files_1 = [1, "before1.jpg", "after.jpg"]
    files_2 = [1, "before1.png", "after.jpg"] #check. Exits. Input and output have different extensions
    files_3 = [1, "before1.jpg", "after.png"] #check. Exits. Input and output have different extensions
    files_4 = [1, "before1.jpg", "after.jpg"]
    files_5 = [1, "before1.jpg", "after.jpg", "long.jpg"] #check. Exits. Too many command-line arguments
    files_6 = [1, "before1.jpg"] #check. Exits. Too few command-line arguments
    files_7 = [1] #check. Exits. Too few command-line arguments
    files_8 = [1, "before1.gif", "after.gif"] #check. Exits. Invalid input
    files_9 = [1, "before1.jpg", "after.gif"] #Exits. Invalid output
    costumes(files_9)


def costumes(file):
    #print("x =", x)
    #print("y =", y)
    extensions = [".jpg", ".jpeg", ".png"]
    #I have to check up for the lenght of the given list.
    if len(file) == 3:
        x = splitext(file[1])
        y = splitext(file[2])
        mupet = file[1]
        new_mupet = file[2]
        print(f'{mupet} /// {new_mupet}')

        #Then I look up for the correct extensions.
        if x[1] == y[1] and x[1] in extensions and y[1] in extensions:
            images = []
            try:
                with Image.open(mupet) as mupet:
                    shirt = Image.open("shirt.png")
                    #print("Shirt:",shirt.size)
                    #print("Mupet:",mupet.size)
                    #mupet_size = mupet.size
                    w = mupet.size[0]
                    l = mupet.size[1]
                    mupet_size = (w , l -150)
                    shirt = op.fit(shirt, size = mupet_size)
                    #print("Shirt:",shirt.size)
                    mupet.paste(shirt, shirt)
                    #mupet = op.fit(mupet)
                    mupet.save("new_shirt.png")
                    #p_2 = ImageOps.fit(p_1)
                    #Image.paste
                    #Image.save
            except:
                sys.exit("Invalid input")
        #When the first file(x) doesn't have the correct extension.
        elif x[1] not in extensions:
            sys.exit("Invalid input")
        #When the second file(y) doesn't have the correct extension.
        elif y[1] not in extensions:
            sys.exit("Invalid output")
        elif y[1] in extensions and x[1] in extensions and x[1] != y[1]:
            sys.exit("Input and output have different extensions")

    #If the lenght is different from 3, I have to exit and print a message.
    elif len(file) > 3:
        sys.exit("Too many command-line arguments")
    elif len(file) < 3:
        sys.exit("Too few command-line arguments")
    else:
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