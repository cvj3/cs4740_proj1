print "\n\nLoading Models..."
from saved_models.unigram import unigram_model
from lib.unigram_model import generate_unigram_sentences
from saved_models.bigram import bigram_model
from lib.bigram_model import generate_bigram_sentences
from saved_models.trigram import trigram_model
from lib.trigram_model import generate_trigram_sentences
print "Done!\n\n"
import sys
import datetime

def main(sentence_number):
	print "\n\n---UNIGRAM SENTENCES---\n"
	generate_unigram_sentences(unigram_model, sentence_number)

	print "\n\n---BIGRAM SENTENCES---\n"
	generate_bigram_sentences(bigram_model, sentence_number)	

	print "\n\n---TRIGRAM SENTENCES---\n"
	generate_trigram_sentences(trigram_model, sentence_number)


if __name__ == "__main__":
	args = sys.argv
	random_sentence_number = 1
	if len(args) == 1:  # If no args, run with default sentence #
		main(random_sentence_number)
	elif "-h" in args or "-help" in args or "--help" in args:
		print "\n\nGENERATE_SENTENCES.PY USAGE GUIDE:\n\nNote that multiple Flags cannot be abbreviated into one (such as '-fr')\n\nThis file generates sentences for all saved models."

		print "\t-r\tRandom Sentence Flag\n"
		print "\t\tIndicates that the field immediately following it is an\n\t\tinteger representing the number of random sentences to\n\t\tgenerate for the generated models.  This flag is optional.\n\t\tIf not used, 1 sentence will be generated per model.\n\n"
		
		print "-h, -help, or --help\n"
		print "\t\tDisplays the help menu which describes all possible arguments."
		quit()

	elif "-r" in args:
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
			main(random_sentence_number)
	else:
		print "\nThis program requires you to specify at least one of the recognized arguments.  Please run 'ngram.py' with the '-h', '-help', or '--help' flag to see the available flags and arguments."
		quit()