
# initial_search_query.py 
# By Anton A Rakos

# Can be ran with python3.7 initial_search_query.py

# This script houses the functions for processing an initial search query.




def tokenize_search_query(search_query):
	import wikipedia
	import spacy
	
	nlp = spacy.load("en_core_web_lg")
	print(search_query)
	
	basic_search =  wikipedia.search(search_query)
	
	wiki_pages = []
	
	for i in range(len(basic_search)):
		
		member = wikipedia.page(basic_search[i])		
		
		decoy1 = wikipedia.page(wikipedia.random())
		decoy2 = wikipedia.page(wikipedia.random())
		
		wiki_pages.append(member.url)
		wiki_pages.append(decoy1.url)
		wiki_pages.append(decoy2.url)

	print(wiki_pages)	
	
	doc = nlp(search_query)

	for ent in doc.ents:
		print("-------------")
		print(ent.text, ent.label_)	
	
	
	

tokenize_search_query("When did WWII end?")
