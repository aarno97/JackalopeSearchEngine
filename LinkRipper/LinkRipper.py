"""Sources:
https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
"""

# import libraries
import requests
from bs4 import BeautifulSoup
import re


# define linker, any URL passed to this program will have the links on the page returned as a list
def linker(url):
    # use requests to get text of HTML
    page = requests.get(url).text
    # pass page to BeautifulSoup to parse
    soup = BeautifulSoup(page, 'html.parser')
    # refactor parsed page to give strings of the urls on a page
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
    print(links)
    return links


# //PLACE YOUR URL BELOW\\
website = "https://en.wikipedia.org/wiki/Pokémon"
# print the URL we are going to get
print(website)
# find those links
linker(website)
