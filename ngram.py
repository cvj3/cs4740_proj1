import sys
import os
import nltk
import datetime
nltk.download('punkt')  # Isn't installed by default with NLTK, needed for tokenize.
from nltk import word_tokenize

import random

ALL_PUNCT = [",",";", ":", "'",'""',"''","-", "``",".","!","?"]
END_SENTENCE_PUNCT = [".","!","?"]
IGNORE_PUNCT = ["''", "``", '""']

def add_word_to_unigram_sentence(sentence, word):
	space = True
	if word == "i": word = word.upper()  # Make i into I

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

	if space: sentence += " "
	sentence += word
	return sentence, word

def generate_unigram_sentence(sentence_number, tokens):
	for i in range(sentence_number):
		sentence = ""
		word = None
		while word not in END_SENTENCE_PUNCT:			
			word = random.choice(tokens).strip()
			sentence, word = add_word_to_unigram_sentence(sentence, word)
		print sentence
		print "\n"


def file_to_tokens(file_name):
	f = open(file_name)
	text = " ".join(f.readlines())		
	text = text.decode('ISO-8859-1').lower()
	#text = text.decode('utf-16').lower()
	tokens = nltk.word_tokenize(text)
	f.close()
	return tokens

def dir_to_tokens(dir_name):	
	tokens = []
	for f in os.listdir(dir_name):
	    if f.endswith(".txt"):
	    	tokens += file_to_tokens(dir_name + "/" + f)
	return tokens


def main(save_model_name, sentence_number, dir_name, file_name):
	start = datetime.datetime.now()
	if file_name:
		tokens = file_to_tokens(file_name)
	else:  # One of these two will always be populated, based on how this function is called.
		tokens = dir_to_tokens(dir_name)

	if random_sentence_number:
		generate_unigram_sentence(sentence_number, tokens)
	end = datetime.datetime.now()

	print "\nProcessed %d tokens." % len(tokens)
	print "Finished in %s seconds." % str((end - start).seconds)

def handleRSFlags(args):
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
	if "-s" in args:
		value_index = args.index("-s") + 1
		if len(args) <= value_index:
			print "\nExpected a field after '-s'"
			quit()
		else:
			save_model_name = args[value_index]
	return save_model_name, random_sentence_number

if __name__ == "__main__":
	args = sys.argv
	save_model_name = None
	random_sentence_number = None

	if "-h" in args or "-help" in args or "--help" in args:
		print "\n\nNGRAM.PY USAGE GUIDE:\n\nNote that multiple Flags cannot be abbreviated into one (such as '-fr')\n\n"

		print "-m\t\tModel Target Flag\n"
		print "\t\tIndicates that the field immediately following it is the\n\t\tfile name of the saved model for use.\n\t\tIt is required to use either this, the '-d', or the '-f' flag.\n\n"

		print "-d\t\tDirectory Target Flag\n"
		print "\t\tIndicates that the field immediately following it is a\n\t\tdirectory and should be used as the corpus.\n\t\tIt is required to use either this, the '-f', or the '-m' flag.\n\n"

		print "-f\t\tFile Target Flag\n"
		print "\t\tIndicates that the field immediately following it is a\n\t\t.txt file and should be used as the corpus.\n\t\tIt is required to use either this, the '-d', or the '-m' flag.\n\n"

		print "\t-r\tRandom Sentence Flag\n"
		print "\t\tIndicates that the field immediately following it is an\n\t\tinteger representing the number of random sentences to\n\t\tgenerate for the generated models.  This flag is optional.\n\t\tIf used, this flag must be used with a -f, -d, or -m flag.\n\n"
		
		print "\t-s\tSave Model Flag\n"
		print "\t\tIndicates that the field immediately following it is a\n\t\tpath to a .txt file where model computed by ngram.py should\n\t\tbe saved.  This flag is optional.  If used, this flag must\n\t\tbe used with a -f or -d flag.\n\n"

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
					save_model_name, random_sentence_number = handleRSFlags(args)
					main(save_model_name, random_sentence_number, value, None)
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
					save_model_name, random_sentence_number = handleRSFlags(args)
					main(save_model_name, random_sentence_number, None, value)
				else:
					print "\nExpected '%s' to be a .txt file." % value
					quit()
			else:
				print "\nCould not find path '%s' (assuming that the root directory is the one in which ngram.py resides)" % value
				quit()

	else:
		print "\nThis program requires you to specify at least one of the recognized arguments.  Please run 'ngram.py' with the '-h', '-help', or '--help' flag to see the available flags and arguments."
		quit()