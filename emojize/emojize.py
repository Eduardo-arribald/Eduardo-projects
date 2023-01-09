
from emoji import emojize

def main():
    x = input("Input: ")
    search(x)

def search(x:str):
    print("Output:", emojize(emojize(x, language = 'alias'))) #variant = "emoji_type"))

#search(":thumbsup:   :thumbs_up:")
#search(":thumbsup:")

main()