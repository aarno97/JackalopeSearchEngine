import spacy
import cupy.cuda
import sys



#command1 = sys.argv[1]
#command2 = sys.argv[2]

# interpret via: $ SPACY_WARNING_IGNORE=W008 python3.7 run_nlp.py

nlp = spacy.load("en_core_web_lg")  # make sure to use larger model!
#data_0 = nlp(command1)
data_0 = nlp("Texas Tech University")

#filepath = command2
filepath = "logged_results01" 


with open(filepath) as fp:
	line = fp.readline()
	cnt = 0
	webpage_word_position = 0
	query_word_position = 0

	page_url = ""
	url_set = 0

	while line:
		line = fp.readline()
		if(line != " \n"):
			if(line.strip() != "############"):

				data_1 = nlp(line)
				for token1 in data_1:
					query_word_position = 0
					for token2 in data_0:
						if query_word_position == 0 and webpage_word_position == 0 and url_set == 0:
							page_url = token1.text
							url_set = 1
							webpage_word_position = 0
						print(page_url)
						print(query_word_position) 
						print(webpage_word_position)
						print(token1.similarity(token2))
						query_word_position += 1
					
					webpage_word_position += 1

			else:
				webpage_word_position = 0
				url_set = 0
			cnt += 1

	fp.close()
