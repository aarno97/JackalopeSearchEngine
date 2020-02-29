import spacy
import cupy.cuda
import wikipedia


spacy.require_gpu()

nlp = spacy.load("en_core_web_lg")  # make sure to use larger model!
tokens = nlp("Putin China")
wikipedia.set_lang("en")
page_0 = wikipedia.page("Soviet_Union")
data_0 = nlp(page_0.content)

#
for token1 in tokens:
    for token2 in data_0:
        print(token1.text, token2.text, token1.similarity(token2))
