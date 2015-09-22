from saved_models.unigram import unigram_model
from saved_models.bigram import bigram_model
from saved_models.trigram import trigram_model
# from nltk import word_tokenize
import os
import sys
from lib.GoodTuring import createSmoothedModel

__author__ = "Alin Barsan, Curtis Josey"


# Good-Turning discounting/smoothing (and unknown words) in the test data;
# explain why you need this for steps 4 (perplexity) and 5 (genre classification)


# load model
# estimate probability of unseens words, by counting
# ... things only seen once / total # of words


def main():
    # get number of total n-grams
    print "\nUnigram Model with Good-Turing Smoothing..."
    createSmoothedModel(1, unigram_model, "<unk>", True)

    print "\nBigram Model with Good-Turing Smoothing..."
    createSmoothedModel(2, bigram_model, "<unk>", True)

#    print "\nTrigram Mass with Good-Turing Smoothing..."
#    createSmoothedModel(3, trigram_model, "<unk>", True)

# argument for the "seed", optional number of sentences
if __name__ == "__main__":
    gen_num_sentences = 1
    seed_value = ""

    # cache arguments passed via command line
    args = sys.argv

    # -h or -help or --help or no arguments supplied
    if "-h" in args or "-help" in args or "--help" in args:
        print "\n\n" + os.path.basename(__file__) + " USAGE GUIDE:\n\n"

#        print "\t-s\tSentence Seed Flag\n"
#        print "\t\tTo be followed by a string value in double quotes.\n\t\tThis sentence fragment will be completed using the\n\t\tmost recently generated bigram model.\n\t\tThe flag and sentence fragment are required parameters.\n\n"
#        print "\t-r\tNumber of Sentences to Generate Flag\n"
#        print "\t\tTo be followed by an integer value that determines\n\t\thow many sentences to generate based on the supplied\n\t\tsentence fragment supplied.\n\t\tThis flag is optional, and defaults to 1.\n\n"

        print "\t-h, -help, or --help\n"
        print "\t\tDisplays the help menu which describes all possible arguments."

        print "\n\n\tSAMPLE USAGE:\n\t\tpython " + os.path.basename(__file__)
        quit()

    main()
