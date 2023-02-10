
import sys
from PIL import Image

def main():
    files = sys.argv
    files_1 = [1, "before.jpg", "after.jpg"]
    files_2 = [1, "before.jpg", "after.jpg"]
    files_3 = [1, "before.jpg", "after.jpg"]
    costumes(file_1)


def costumes(file):
    x = splitext(file[1])
    print(x)
    extensions = [".jpg", ".jpeg", ".png"]
    if len(file) == 3 and x[1] in extensions:
        images = []
        x = splitext(file)
        print(x)
        #for arg in sys.argv:
     #   image = Image.open(arg)
      #  images.append(image)
    elif len(file) > 3:

        
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