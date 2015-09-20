from saved_models.unigram import unigram_model
from lib.unigram_model import getTotalCount
from lib.unigram_model import getSingletonCount

from saved_models.bigram import bigram_model
from lib.bigram_model import getTotalCount as getTotalCount2
from lib.bigram_model import getSingletonCount as getSingletonCount2

from saved_models.trigram import trigram_model
from lib.trigram_model import getTotalCount as getTotalCount3
from lib.trigram_model import getSingletonCount as getSingletonCount3
# from nltk import word_tokenize
import os
import sys
from lib.GoodTuring import unknown_probability, discount_probability

__author__ = "Alin Barsan, Curtis Josey"


# Good-Turning discounting/smoothing (and unknown words) in the test data;
# explain why you need this for steps 4 (perplexity) and 5 (genre classification)


# load model
# estimate probability of unseens words, by counting
# ... things only seen once / total # of words


def main():
    # get number of total n-grams
    print "\n...Unigram Mass..."
    thisModel = unigram_model
    # get number of singleton n-grams
    singletonMass = getSingletonCount(thisModel)
    print "singletonMass:\t%d" % (singletonMass)
    totalMass = getTotalCount(thisModel)
    print "totalMass:\t%d" % (totalMass)

    # calculate probably of unknown
    print "%% Unknown Unigram:\t%.12f" % unknown_probability(singletonMass, totalMass)
    # discount the MLE probability for known singletons
    print "%% Singleton (Smoothed):\t%.12f" % discount_probability(singletonMass, totalMass)

    print "\n...Bigram Mass..."
    thisModel2 = bigram_model
    # get number of singleton n-grams
    singletonMass = getSingletonCount2(thisModel2)
    print "singletonMass:\t%d" % (singletonMass)
    totalMass = getTotalCount2(thisModel2)
    print "totalMass:\t%d" % (totalMass)

    # calculate probably of unknown
    print "%% Unknown Bigram:\t%.12f" % unknown_probability(singletonMass, totalMass)
    # discount the MLE probability for known singletons
    print "%% Singleton (Smoothed):\t%.12f" % discount_probability(singletonMass, totalMass)

    print "\n...Trigram Mass..."
    thisModel3 = trigram_model
    # get number of singleton n-grams
    singletonMass = getSingletonCount3(thisModel3)
    print "singletonMass:\t%d" % (singletonMass)
    totalMass = getTotalCount3(thisModel3)
    print "totalMass:\t%d" % (totalMass)

    # calculate probably of unknown
    print "%% Unknown Trigram:\t%.12f" % unknown_probability(singletonMass, totalMass)
    # discount the MLE probability for known singletons
    print "%% Singleton (Smoothed):\t%.12f" % discount_probability(singletonMass, totalMass)

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
