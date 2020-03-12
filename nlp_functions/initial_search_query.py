# initial_search_query.py 
# By Anton A Rakos

# Can be ran with python3.7 initial_search_query.py

# This script houses the functions for processing an initial search query.

def get_decoys(target):
	decoy1_search = []
	import wikipedia
	while len(decoy1_search) < target:
		try:
			decoy1 = wikipedia.page(wikipedia.random())
			decoy1_query = wikipedia.search(decoy1)
			
			for i in range(len(decoy1_query)):
				if len(decoy1_search) >= target:
				
					break
				else:
					try:	
						member0 = wikipedia.page(decoy1_query[i])
						decoy1_search += member0.references
						
					except:	
						continue

		except:
			continue

	return decoy1_search

def tokenize_search_query(search_query):
	import wikipedia
	
	wikipedia.set_lang("en")
	print(search_query)
	
	basic_query =  wikipedia.search(search_query)
	
	basic_search = []
	
	for i in range(len(basic_query)):
		if len(basic_search) >= 256:
			break
		try:	
			member0 = wikipedia.page(basic_query[i])
			basic_search += member0.references
		except:
			continue
	
	decoy1_search = get_decoys(len(basic_search))
	decoy2_search = get_decoys(len(basic_search))

			

	wiki_pages = []

	
		
	print(len(basic_search))
	print(len(decoy1_search))
	print(len(decoy2_search))
		



tokenize_search_query("Paul Newman")
