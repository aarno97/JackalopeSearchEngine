""" Sources:
https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/
https://www.quora.com/How-can-I-extract-only-text-data-from-HTML-pages
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://stackoverflow.com/questions/36709165/beautifulsoup-object-of-type-response-has-no-len

Instructions on running this python script in terminal:
1. Open Terminal
2. cd into the folder where LinkRipper is held. On the original machine this command was:
% cd Documents/GitHub/CS4366-SeniorProject/TextRipper
3. run the program using the python3 command
% python3 TextRipper.py
"""

# import libraries
import requests
from bs4 import BeautifulSoup

# define ripper, any URL passed to this program will have the text on the page returned
def ripper(url):
    # use requests to get text of HTML
    page = requests.get(url).text
    # pass page to BeautifulSoup to parse
    soup = BeautifulSoup(page, 'html.parser')
    # refactor parsed page to give strings of the text on a page
    for text in soup.stripped_strings:
        print(text)
    # returns an array of strings with text in each one
    return soup.stripped_strings


# //PLACE YOUR URL BELOW\\
url = "https://en.wikipedia.org/wiki/Pokémon"
# print the URL we are going to get
print(url)
# rip that URL up
ripper(url)
