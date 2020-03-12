"""
Sources:
https://www.thepythoncode.com/article/download-web-page-images-python

How to run this program in terminal:
1. Open Terminal
2. cd into the folder where LinkRipper is held. On the original machine this command was:
% cd Documents/GitHub/JackalopeSearchEngine/ImageRipper
3. run the program using the python3 command
% python3 ImageRipper.py
"""

# import libraries
import re
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup


# define images, a URL sent to this will save all images
def images(url):
    # use requests to get the text of the HTML
    page = requests.get(url).text

    # pass page to BeautifulSoup to parse
    soup = BeautifulSoup(page, 'html.parser')

    # refactor parsed page to return urls of images
    img_urls = soup.find_all('img')

    # put all image links into a list
    urls = [img['src'] for img in img_urls]

    # using set() to remove duplicates
    nodupes = list(set(urls))

    # make urls absolute in for in the event we don't get the full url in the beginning
    absolute = []
    for image in nodupes:
        absolute.append(urljoin(url, image))

    # print all links
    for reference in absolute:
        print(reference)
    return


url = "https://unsplash.com"
print(url)
images(url)
