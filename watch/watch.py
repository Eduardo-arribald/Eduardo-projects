import re
import sys


def main():
    #x = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    #x_1 ='<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    #x_2 = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
    #x_3 = "https://youtube.com/embed/xvFZjo5PgG0"
    #parse(x_1)
    print(parse(input("HTTML: ")))

def parse(s):
    w = re.search(r'"(?:http|https)://(?:www.)?youtube.com/embed/(\w+)"', s)
    #w = re.search(r"(embed/([a-zA-Z0-9]+))", s)
    #w = re.search(r'"', s)
    if w:
        #print("Simon")
        #print(w.group(1))
        x = w.group(1)
        z = "https://youtu.be/"
        #x = (w.group(1)).split('"')

        x = z+x
        return x
    else:
        #print("Nel")
        return None



if __name__ == "__main__":
    main()