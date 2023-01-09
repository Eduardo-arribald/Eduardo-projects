
import emoji

def search():
    x = input()
    print(emoji.emojize(x))
    print(emoji.emojize(x, languague = "alias")) #variant = "emoji_type"))

search()