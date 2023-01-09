
from emoji import emojize

def search(x:str):
    #x = input()
    print(emojize(x))
    print(type(x))
    #print(emojize(x, languague = 'alias')) #variant = "emoji_type"))

search(":thumbs_up:")
search(":thumbsup:")