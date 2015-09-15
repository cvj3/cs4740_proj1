import sys
import os
import nltk
import datetime
nltk.download('punkt')  # Isn't installed by default with NLTK, needed for tokenize.
from nltk import word_tokenize

from bigram_model import generate_bigram_sentences, build_bigram_model
from unigram_model import generate_unigram_sentences, build_unigram_model

def file_to_tokens(file_name):
	f = open(file_name)
	text = " ".join(f.readlines())		
	text = text.decode('ISO-8859-1').lower()
	tokens = nltk.word_tokenize(text)
	f.close()
	return tokens

def dir_to_tokens(dir_name):	
	tokens = []
	for f in os.listdir(dir_name):
	    if f.endswith(".txt"):
	    	tokens += file_to_tokens(dir_name + "/" + f)
	return tokens


def main(sentence_number, dir_name, file_name):
	start = datetime.datetime.now()
	if file_name:
		tokens = file_to_tokens(file_name)
	else:  # One of these two will always be populated, based on how this function is called.
		tokens = dir_to_tokens(dir_name)
	unigram_model = build_unigram_model(tokens)
	bigram_model = build_bigram_model(tokens)

	if random_sentence_number:
		print "UNIGRAM SENTENCES:\n"
		generate_unigram_sentences(unigram_model, sentence_number)
		print "BIGRAM SENTENCES:\n"
		generate_bigram_sentences(bigram_model, sentence_number)
	end = datetime.datetime.now()

	print "\nProcessed %d tokens." % len(tokens)
	print "Finished in %s seconds." % str((end - start).seconds)

def parse_random_number_flag(args):
	save_model_name = None
	random_sentence_number = None
	if "-r" in args:
		value_index = args.index("-r") + 1
		if len(args) <= value_index:
			print "\nExpected a field after '-r'"
			quit()
		else:
			value = args[value_index]
			if not value.isdigit():
				print "\nExpected the value following '-r' to be an integer."
				quit()
			else:
				random_sentence_number = int(value)
	return random_sentence_number

if __name__ == "__main__":
	args = sys.argv
	save_model_name = None
	random_sentence_number = None

	if "-h" in args or "-help" in args or "--help" in args:
		print "\n\nNGRAM.PY USAGE GUIDE:\n\nNote that multiple Flags cannot be abbreviated into one (such as '-fr')\n\n"

		print "-d\t\tDirectory Target Flag\n"
		print "\t\tIndicates that the field immediately following it is a\n\t\tdirectory and should be used as the corpus.\n\t\tIt is required to use either this, the '-f', or the '-m' flag.\n\n"

		print "-f\t\tFile Target Flag\n"
		print "\t\tIndicates that the field immediately following it is a\n\t\t.txt file and should be used as the corpus.\n\t\tIt is required to use either this, the '-d', or the '-m' flag.\n\n"

		print "\t-r\tRandom Sentence Flag\n"
		print "\t\tIndicates that the field immediately following it is an\n\t\tinteger representing the number of random sentences to\n\t\tgenerate for the generated models.  This flag is optional.\n\t\tIf used, this flag must be used with a -f, -d, or -m flag.\n\n"
		
		print "-h, -help, or --help\n"
		print "\t\tDisplays the help menu which describes all possible arguments."
		quit()

	elif "-d" in args:
		if "-f" in args:
			print "\nCannot target both a file and a directory."
			quit()
		if "-m" in args:
			print "\nCannot target both a saved model and a directory."
			quit()
		value_index = args.index("-d") + 1
		if len(args) <= value_index:
			print "\nExpected a field after '-d'"
			quit()
		else:
			value = args[value_index]
			if os.path.exists(value):
				if os.path.isdir(value):
					random_sentence_number = parse_random_number_flag(args)
					main(random_sentence_number, value, None)
				else:
					print "\nExpected '%s' to be the path to a target directory, not file." % value
					quit()
			else:
				print "\nCould not find path '%s' (assuming that the root directory is the one in which ngram.py resides)" % value
				quit()

	elif "-f" in args:
		if "-m" in args:
			print "\nCannot target both a saved model and a file."
			quit()
		value_index = args.index("-f") + 1
		if len(args) <= value_index:
			print "\nExpected a field after '-f'"
			quit()
		else:
			value = args[value_index]
			if os.path.exists(value):
				if value[-4:] == ".txt":
					random_sentence_number = parse_random_number_flag(args)
					main(random_sentence_number, None, value)
				else:
					print "\nExpected '%s' to be a .txt file." % value
					quit()
			else:
				print "\nCould not find path '%s' (assuming that the root directory is the one in which ngram.py resides)" % value
				quit()

	else:
		print "\nThis program requires you to specify at least one of the recognized arguments.  Please run 'ngram.py' with the '-h', '-help', or '--help' flag to see the available flags and arguments."
		quit()
