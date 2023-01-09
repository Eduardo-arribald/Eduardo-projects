
from emoji import emojize

def search(x:str):
    #x = input()
    #print(emojize(x))

    print(emojize(emojize(x, language = 'alias'))) #variant = "emoji_type"))

search(":thumbsup:   :thumbs_up:")
search(":thumbsup:")