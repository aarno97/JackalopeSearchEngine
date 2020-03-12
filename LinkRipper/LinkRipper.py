"""Sources:
https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

How to run this program in terminal:
1. Open Terminal
2. cd into the folder where LinkRipper is held. On the original machine this command was:
% cd Documents/GitHub/JackalopeSearchEngine/LinkRipper
3. run the program using the python3 command
% python3 LinkRipper.py
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
    for reference in links:
        print(reference)
    return links


# //PLACE YOUR URL BELOW\\
website = "https://en.wikipedia.org/wiki/South_Park"
# print the URL we are going to get
print(website)
# find those links
linker(website)
