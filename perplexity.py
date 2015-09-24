from build_ngram import dir_to_tokens, filter_tokens
import datetime
import sys
from math import log

def probability_unigram(target, model, totals):
	# get probability of target based on model
	total = totals[0]
	if not model.get(target):  # if token is unknown
		target = "<unk>"
	count = model[target]
	p = float(count) / total
	return p


def probability_bigram(target, models, word_prev, totals):
	# get probability of target based on model and previous word
	bigram = models[1]
	bigram_totals = totals[1]
	if not bigram.get(word_prev):  # if root word is unknown, revert to unigram
		return probability_unigram(target, models[0], totals)
	if not bigram[word_prev].get(target):  # if target is unkown
		target = "<unk>"
	count = bigram[word_prev][target]
	total = bigram_totals[word_prev]
	p = float(count) / total
	return p

def probability_trigram(target, models, word_prev, word_prev_two, totals):
	# get probability of target based on model and previous two words
	unigram, bigram, trigram = models[0], models[1], models[2]
	trigram_totals = totals[2]

	if not trigram.get(word_prev_two):  # if root word is unknown, revert to bigram
		return probability_bigram(target, models, word_prev, totals)
	elif not trigram[word_prev_two].get(word_prev):
		return probability_unigram(target, unigram, totals)
	else:
		if not trigram[word_prev_two][word_prev].get(target):
			target = "<unk>"
		count = trigram[word_prev_two][word_prev][target]
		total = trigram_totals[word_prev_two][word_prev]		
		p = float(count) / total
		return p

def parse_test_data(dir_path):
	tokens = dir_to_tokens(dir_path)
	#tokens = filter_tokens(tokens)
	return tokens

def buildCounts(models):
	unigram_count = 0
	bigram_counts = {}
	trigram_counts = {}

	model = models[0]
	unigram_count = sum(model.values())

	model = models[1]
	for key in model:
		bigram_counts[key] = sum(model[key].values())

	model = models[2]
	for key_one in model:
		trigram_counts[key_one] = {}        	
		for key_two in model[key_one]:
			trigram_counts[key_one][key_two] = sum(model[key_one][key_two].values())
	return [unigram_count, bigram_counts, trigram_counts]

def get_model_perplexity(models, nGrams, tokens, totals):
	token_range = range(len(tokens))	
	N = len(tokens)
	running_product = 1
	if nGrams == 1:
		model = models[0]
		for i in token_range:
			target = tokens[i]
			p = probability_unigram(target, model, totals)
			#running_logs -= log10(p)
			running_product *= pow( (1.0/float(p)) , (1.0 / float(N)) )
	if nGrams == 2:
		models = models[:-1]
		for i in token_range:
			target = tokens[i]
			if i == 0: #use unigram model if no previous info.		
				p = probability_unigram(target, models[0], totals)
			else:		
				p = probability_bigram(target, models, tokens[i-1], totals)
			#running_logs -= log10(p)
			running_product *= pow( (1.0/float(p)) , (1.0 / float(N)) )
			
	if nGrams == 3:
		for i in token_range:
			target = tokens[i]
			if i == 0: #use unigram model if no previous info.		
				p = probability_unigram(target, models[0], totals)
			elif i == 1:		
				p = probability_bigram(target, models[:-1], tokens[i-1], totals)
			else:
				p = probability_trigram(target, models, tokens[i-1], tokens[i-2], totals)
			#running_logs -= log10(p)
			running_product *= pow( (1.0/float(p)) , (1.0 / float(N)) )
	return running_product

def get_scaled_trigram_perplexity(trigram, tokens, perplexity):
	tokens = set(tokens)
	N = len(tokens)
	count = 0
	for token in tokens:
		if trigram.get(token):
			count += 1
	return perplexity * ( 1 - (float(count) / float(N)))


def main(dir_path):
	start = datetime.datetime.now()
	tokens = parse_test_data(dir_path)
	end = datetime.datetime.now()
	print "\nParsed test data in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

	start = datetime.datetime.now()
	from saved_models.children_unigram_smoothed import model as unigram
	from saved_models.children_bigram_smoothed import model as bigram
	from saved_models.children_trigram_smoothed import model as trigram	
	models = [unigram, bigram, trigram]
	end = datetime.datetime.now()
	print "\nLoaded 'Children' models in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

	start = datetime.datetime.now()
	totals = buildCounts([unigram, bigram, trigram])
	end = datetime.datetime.now()
	print "\nProcessed counts for 'Children' models in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)
	
	start = datetime.datetime.now()
	u_p = (get_model_perplexity(models, 1, tokens, totals))
	b_p = (get_model_perplexity(models, 2, tokens, totals))
	t_p = (get_model_perplexity(models, 3, tokens, totals))
	end = datetime.datetime.now()
	print "\nCalculated 'Children' models perplexity in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)
	print "\tUnigram Perplexity: %5f\n\tBigram Perplexity: %5f\n\tTrigram Perplexity: %5f\n" % (u_p, b_p, t_p)
	#print "\tScaled Trigram Perplexity: %5f" % get_scaled_trigram_perplexity(trigram, tokens, t_p)

	start = datetime.datetime.now()
	from saved_models.crime_unigram_smoothed import model as unigram
	from saved_models.crime_bigram_smoothed import model as bigram
	from saved_models.crime_trigram_smoothed import model as trigram	
	models = [unigram, bigram, trigram]
	end = datetime.datetime.now()
	print "\nLoaded 'Crime' models in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

	start = datetime.datetime.now()
	totals = buildCounts([unigram, bigram, trigram])
	end = datetime.datetime.now()
	print "\nProcessed counts for 'Crime' models in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)
	
	start = datetime.datetime.now()
	u_p = (get_model_perplexity(models, 1, tokens, totals))
	b_p = (get_model_perplexity(models, 2, tokens, totals))
	t_p = (get_model_perplexity(models, 3, tokens, totals))
	end = datetime.datetime.now()
	print "\nCalculated 'Crime' models perplexity in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)
	print "\tUnigram Perplexity: %5f\n\tBigram Perplexity: %5f\n\tTrigram Perplexity: %5f\n" % (u_p, b_p, t_p)
	#print "\tScaled Trigram Perplexity: %5f" % get_scaled_trigram_perplexity(trigram, tokens, t_p)


	start = datetime.datetime.now()
	from saved_models.history_unigram_smoothed import model as unigram
	from saved_models.history_bigram_smoothed import model as bigram
	from saved_models.history_trigram_smoothed import model as trigram	
	models = [unigram, bigram, trigram]
	end = datetime.datetime.now()
	print "\nLoaded 'History' models in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

	start = datetime.datetime.now()
	totals = buildCounts([unigram, bigram, trigram])
	end = datetime.datetime.now()
	print "\nProcessed counts for 'History' models in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)
	
	start = datetime.datetime.now()
	u_p = (get_model_perplexity(models, 1, tokens, totals))
	b_p = (get_model_perplexity(models, 2, tokens, totals))
	t_p = (get_model_perplexity(models, 3, tokens, totals))
	end = datetime.datetime.now()
	print "\nCalculated 'History' models perplexity in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)
	print "\tUnigram Perplexity: %5f\n\tBigram Perplexity: %5f\n\tTrigram Perplexity: %5f" % (u_p, b_p, t_p)
	#print "\tScaled Trigram Perplexity: %5f" % get_scaled_trigram_perplexity(trigram, tokens, t_p)


if __name__ == "__main__":
	args = sys.argv
	# expect first arg to be the directory path
	dir_path = args[1]
	main(dir_path)