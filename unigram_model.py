from common import END_SENTENCE_PUNCT, add_word_to_sentence
import random

def build_unigram_model(tokens):
	return tokens

def write_model_to_file(tokens):
	unigram_model = {}
	for token in tokens:
		if token not in unigram_model.keys(): unigram_model[token] = 1
		else: unigram_model[token] += 1
	f = open("saved_models/unigram.txt")


def generate_unigram_sentences(unigram_model, number):
	for i in range(number):
		sentence = ""
		word = None
		while word not in END_SENTENCE_PUNCT:			
			word = random.choice(unigram_model).strip()
			sentence, word = add_word_to_sentence(sentence, word)
		try:
			print sentence
		except:
			print "Could not print sentence due to an unrecognized character."
		print "\n"