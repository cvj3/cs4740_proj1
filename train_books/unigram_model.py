from common import END_SENTENCE_PUNCT, add_word_to_sentence

def build_unigram_model(tokens):
	return tokens

def generate_unigram_sentences(unigram_model, number):
	for i in range(number):
		sentence = ""
		word = None
		while word not in END_SENTENCE_PUNCT:			
			word = random.choice(unigram_model).strip()
			sentence, word = add_word_to_sentence(sentence, word)
		print sentence
		print "\n"