from saved_models.children_unigram import model as model1
from saved_models.children_bigram import model as model2
from saved_models.children_trigram import model as model3
from saved_models.crime_unigram import model as model4
from saved_models.crime_bigram import model as model5
from saved_models.crime_trigram import model as model6
from saved_models.history_unigram import model as model7
from saved_models.history_bigram import model as model8
from saved_models.history_trigram import model as model9

# from nltk import word_tokenize
import os
import sys
from lib.GoodTuring import createSmoothedModel

__author__ = "Alin Barsan, Curtis Josey"
# DEVNOTE: DO NOT IMPORT THIS FILE, ALIN is working on an improved version


# Good-Turning discounting/smoothing (and unknown words) in the test data;
# explain why you need this for steps 4 (perplexity) and 5 (genre classification)


# load model
# estimate probability of unseens words, by counting
# ... things only seen once / total # of words
def main():
    # get number of total n-grams
    print "\nUnigram Model with Good-Turing Smoothing..."
    createSmoothedModel(1, model1, True)

    print "\nBigram Model with Good-Turing Smoothing..."
    createSmoothedModel(2, model2, True)

#    print "\nTrigram Mass with Good-Turing Smoothing..."
#    createSmoothedModel(3, trigram_model, "<unk>", True)

# argument for the "seed", optional number of sentences
if __name__ == "__main__":
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
