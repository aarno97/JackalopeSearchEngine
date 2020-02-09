""" Sources:
https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/
https://www.quora.com/How-can-I-extract-only-text-data-from-HTML-pages
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://stackoverflow.com/questions/36709165/beautifulsoup-object-of-type-response-has-no-len
"""

# import libraries
import requests
from bs4 import BeautifulSoup


def ripper(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    for text in soup.stripped_strings:
        print(text)
    return soup.stripped_strings


url = "https://www.cnn.com/2020/01/20/politics/travel-ban-immigration/index.html"
# url = '{0}?action=render'.format(url)
print(url)
ripper(url)
