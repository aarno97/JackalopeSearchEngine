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
								decoy1_search += [['00', member0_list[j]]]
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
				go_0 = 1
				go_1 = 0
				go_2 = 0
				go_3 = 0
				go_4 = 0
				go_5 = 0
				go_6 = 0
				go_7 = 0
				go_8 = 0
				go_9 = 0
				go_10 = 0
				go_11 = 0
				go_12 = 0
				go_13 = 0
				go_14 = 0
				go_15 = 0
				for j in range(len(member0_list)):
					if(go_0 == 1):
						self.basic_search += [['01', member0_list[j]]]
						go_0 = 0
						go_1 = 1
					elif(go_1 == 1):
						self.basic_search += [['02', member0_list[j]]]
						go_1 = 0
						go_2 = 1
					elif(go_2 == 1):
						self.basic_search += [['03', member0_list[j]]]
						go_2 = 0
						go_3 = 1
					elif(go_3 == 1):
						self.basic_search += [['04', member0_list[j]]]
						go_3 = 0
						go_4 = 1
					elif(go_4 == 1):
						self.basic_search += [['05', member0_list[j]]]
						go_4 = 0
						go_5 = 1
					elif(go_5 == 1):
						self.basic_search += [['06', member0_list[j]]]
						go_5 = 0
						go_6 = 1
					elif(go_6 == 1):
						self.basic_search += [['07', member0_list[j]]]
						go_6 = 0
						go_7 = 1
					elif(go_7 == 1):
						self.basic_search += [['08', member0_list[j]]]
						go_7 = 0
						go_8 = 1
					elif(go_8 == 1):
						self.basic_search += [['09', member0_list[j]]]
						go_8 = 0
						go_9 = 1
					elif(go_9 == 1):
						self.basic_search += [['10', member0_list[j]]]
						go_9 = 0
						go_10 = 1
					elif(go_10 == 1):
						self.basic_search += [['11', member0_list[j]]]
						go_10 = 0
						go_11 = 1
					elif(go_11 == 1):
						self.basic_search += [['12', member0_list[j]]]
						go_11 = 0
						go_12 = 1
					elif(go_12 == 1):
						self.basic_search += [['13', member0_list[j]]]
						go_12 = 0
						go_13 = 1
					elif(go_13 == 1):
						self.basic_search += [['14', member0_list[j]]]
						go_13 = 0
						go_14 = 1
					elif(go_14 == 1):
						self.basic_search += [['15', member0_list[j]]]
						go_14 = 0
						go_15 = 1
					elif(go_15 == 1):
						self.basic_search += [['16', member0_list[j]]]
						go_15 = 0
						go_0 = 1



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
			output_file.write(self.decoy2_search[i][0]+self.decoy2_search[i][1]+'\n')


		output_file.close()
		
import sys
import os

search_list = sys.argv[1:]	
search_this = ' '.join(map(str,search_list ))
app = Tokenize_search_query(search_this)
os.system("rm logged*")
os.system("./runthisthread")
