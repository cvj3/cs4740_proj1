import random

ALL_PUNCT = [",",";", ":", "-", ".","!","?", '...', '--']
END_SENTENCE_PUNCT = [".","!","?"]
IGNORE_PUNCT = ["''", "``", '""', "<", ">", '"', "'", "_", "__", "{", "}", "[", "]"]

def add_word_to_sentence(sentence, word, override=False):
	space = True

	if sentence == "":  # Handling the start of a sentence.
		if word in ALL_PUNCT:
			return sentence, None  # Continue with loop, don't start sentence with punctuation.
		else:
			word = word.title()  # Capitalize first letter of first word in a sentence.
			space = False

	elif word in ALL_PUNCT: # Handling punctuation not at the start of a sentence
		space = False
		if sentence[-1] in ALL_PUNCT:  # Don't place two punctuation tokens next to one another.  Delete the first.
			sentence = sentence[:-1]

	if not override and sentence.count("and") == 3 and word == "and":  # Prevent run on sentences by limiting # of "and" tokens to five.
		return sentence, None

	if space: sentence += " "
	sentence += word
	return sentence, word

def weighted_random_pick(model):
	# For a dictionary where key = token and value = # of occurences of that token, chooses a random token with respect to the weights
	# This means that for a dictionary {A: 5, B: 10}, B will be randomly chosen twice as often as A.
    value = random.uniform(0, sum(model.itervalues()))
    sum_weight = 0
    for token, weight in model.iteritems():
        sum_weight += weight
        if value < sum_weight: return token
    return token