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
import sys
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import lxml.html
import urllib
# define ripper, any URL passed to this program will have the text on the page returned
def ripper(url):
	res = requests.get(url)
	html_page = res.content
	soup = BeautifulSoup(html_page, 'html.parser')
	text = soup.find_all(text=True)
	output = ''
	blacklist = ['[document]','noscript','header','html','meta','head', 'input','script', 'style']
	full_stop = 0;
	for t in text:
		if t.parent.name not in blacklist:
			output += '{} '.format(t)
		full_stop +=1 
		if(full_stop > 150):
			break
	print(url)
	print(soup.title.string)
	print("############")
	#print(output)
	# returns an array of strings with text in each one
	return soup.stripped_strings



# //PLACE YOUR URL BELOW\\
url = sys.argv[1]
# url = "https://en.wikipedia.org/wiki/Pokémon"
# print the URL we are going to get

# rip that URL up
ripper(url)
