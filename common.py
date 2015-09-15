ALL_PUNCT = [",",";", ":", "'",'""',"''","-", "``",".","!","?"]
END_SENTENCE_PUNCT = [".","!","?"]
IGNORE_PUNCT = ["''", "``", '""']

def add_word_to_sentence(sentence, word):
	space = True

	if sentence == "":  # Handling the start of a sentence.
		if word in ALL_PUNCT:
			return sentence, None  # Continue with loop, don't start sentence with punctuation.
		else:
			word = word.title()  # Capitalize first letter of first word in a sentence.
			space = False

	elif word in ALL_PUNCT: # Handling punctuation not at the start of a sentence
		space = False
		if word in IGNORE_PUNCT:
			return sentence, None  # Continue with loop, don't write the punctuation we want to ignore.
		if sentence[-1] in ALL_PUNCT:  # Don't place two punctuation tokens next to one another.  Delete the first.
			sentence = sentence[:-1]

	if sentence.count("and") == 3 and word == "and":  # Prevent run on sentences by limiting # of "and" tokens to three.
		return sentence, None

	if space: sentence += " "
	sentence += word
	return sentence, word