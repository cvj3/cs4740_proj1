from common import END_SENTENCE_PUNCT, add_word_to_sentence
import random

def build_bigram_model(tokens):
	bigram_model = {}
	for i in range(len(tokens) - 1):
		token_curr = tokens[i]
		token_next = tokens[i + 1]
		if not bigram_model.get(token_curr): bigram_model[token_curr] = {}
		if not bigram_model[token_curr].get(token_next): bigram_model[token_curr][token_next] = 1
		else: bigram_model[token_curr][token_next] += 1
	return bigram_model

def word_from_bigram_model_and_previous_word(bigram, word):
	tokens_for_word = []
	for second_word in bigram[word].keys():
		for i in range(bigram[word][second_word]):
			tokens_for_word.append(second_word)
	word = random.choice(tokens_for_word).strip()
	return word

def generate_bigram_sentences(bigram_model, number):
	for i in range(number):
		starting_word = "."
		while starting_word in END_SENTENCE_PUNCT:
			starting_word = random.choice(bigram_model.keys())
		sentence = starting_word.title()
		base_word = starting_word
		word = None
		while word not in END_SENTENCE_PUNCT:
			word = word_from_bigram_model_and_previous_word(bigram_model, base_word)
			sentence, word = add_word_to_sentence(sentence, word)
			if word: 
				base_word = word
		try:
			print sentence
		except:
			print "Could not print sentence due to an unrecognized character."
		print "\n"