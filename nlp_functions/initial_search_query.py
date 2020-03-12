# initial_search_query.py 
# By Anton A Rakos

# Can be ran with python3.7 initial_search_query.py

# This script houses the functions for processing an initial search query.

class Tokenize_search_query:

	def __init__(self, given_input):
		self.input_query = given_input
		self.all_links = []
		self.basic_search = []
		self.decoy1_search = []
		self.decoy2_search = []
		self.start_search_query()
		self.write_binary()
 

	def get_decoys(self, target):
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
							member0_list = member0.references
							for j in range(len(member0_list)):
								decoy1_search += [['0', member0_list[j]]]
								if len(decoy1_search) >= target:
									break
							
						except:	
							continue

			except:
				continue

		return decoy1_search

	def start_search_query(self):
		import wikipedia
		
		wikipedia.set_lang("en")
		print(self.input_query)	
		basic_query =  wikipedia.search(self.input_query)
		print(len(basic_query))	
		print(basic_query)	
		for i in range(len(basic_query)):
			if len(self.basic_search) >= 256:
				break
			try:	
				member0 = wikipedia.page(basic_query[i])
				member0_list = member0.references
				for j in range(len(member0_list)):
					self.basic_search += [['1', member0_list[j]]]
					if len(self.basic_search) >= 256:
						break
			except:
				continue
		
		self.decoy1_search = self.get_decoys(len(self.basic_search))
		self.decoy2_search = self.get_decoys(len(self.basic_search))
	
			
		print(self.basic_search)
		print(len(self.decoy1_search))
		print(len(self.decoy2_search))
			
	def write_binary(self):
		output_file = open("search_domain.txt", "w")

		for i in range(len(self.basic_search)):
			output_file.write(self.basic_search[i][0]+self.basic_search[i][1]+'\n')
			output_file.write(self.decoy1_search[i][0]+self.decoy1_search[i][1]+'\n')
			output_file.write(self.decoy1_search[i][0]+self.decoy1_search[i][1]+'\n')


		output_file.close()
		
		

app = Tokenize_search_query("Paul Newman")
