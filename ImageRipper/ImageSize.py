import urllib.request
from PIL import Image


def size(url):
    image = Image.open(urllib.request.urlopen(url))
    width, height = image.size
    # print(width, height)
    return width, height
