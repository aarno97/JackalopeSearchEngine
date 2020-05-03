"""
Sources:
https://gomilkyway.com/misc/how-to-read-an-image-from-url-in-python-3-and-get-the-height-and-width/
"""

import urllib.request

import PIL
from PIL import Image
from LinkValidate import validate


# size(url) upon being passed a link of an image will return the width and height of said image
# size(url) does not require the image to be saved and read to work
# size(url) will return -1, -1 if the link was not valid
def size(url):

    if validate(url):
        try:
            image = Image.open(urllib.request.urlopen(url))
            width, height = image.size
        except PIL.UnidentifiedImageError:
            return -1, -1
        # print(width, height)
        return width, height
    else:
        return -1, -1
