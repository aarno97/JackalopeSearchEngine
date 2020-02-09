""" Sources:
https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/
https://www.quora.com/How-can-I-extract-only-text-data-from-HTML-pages
"""

# import libraries
import requests
from bs4 import BeautifulSoup


def theripper():
    # save HTML as 'page'
    page = requests.get('https://en.wikipedia.org/wiki/Pokémon')
    # begin parsing the page
    soup = BeautifulSoup(page, 'html.parser')
    txt = soup.get_text()
    print(txt)


