from lib.bigram_model import generate_bigram_sentences
from saved_models.children_bigram import model as bigram_model
from nltk import word_tokenize
import os
import sys


__author__ = "Alin Barsan, Curtis Josey"


def main(seed_value, gen_num_sentences):
    # tokenize the supplied sentence fragment
    seed_tokens = word_tokenize(seed_value)

    # create "N" random sentences, based on sentence fragment "seed"
    if len(seed_tokens) > 0:
        for i in range(gen_num_sentences):
            generate_bigram_sentences(bigram_model, 1, seed_value, seed_tokens[-1])
    else:
        # if sentence fragment missing, just generate from a random word in corpus
        for i in range(gen_num_sentences):
            generate_bigram_sentences(bigram_model, 1, seed_value, ".")

# argument for the "seed", optional number of sentences
if __name__ == "__main__":
    gen_num_sentences = 1
    seed_value = ""

    # cache arguments passed via command line
    args = sys.argv

    # -h or -help or --help or no arguments supplied
    if "-h" in args or "-help" in args or "--help" in args or len(args) < 2:
        print "\n\n" + os.path.basename(__file__) + " USAGE GUIDE:\n\n"

        print "\t-s\tSentence Seed Flag\n"
        print "\t\tTo be followed by a string value in double quotes.\n\t\tThis sentence fragment will be completed using the\n\t\tmost recently generated bigram model.\n\t\tThe flag and sentence fragment are required parameters.\n\n"

        print "\t-r\tNumber of Sentences to Generate Flag\n"
        print "\t\tTo be followed by an integer value that determines\n\t\thow many sentences to generate based on the supplied\n\t\tsentence fragment supplied.\n\t\tThis flag is optional, and defaults to 1.\n\n"

        print "\t-h, -help, or --help\n"
        print "\t\tDisplays the help menu which describes all possible arguments."

        print "\n\n\tSAMPLE USAGE:\n\t\tpython seed.py -s \"Thou shalt\" -r 2"
        quit()

    # -s: the "seed" sentence fragment
    if "-s" in args:
        # get number of sentences to generate
        value_index = args.index("-s") + 1
        if len(args) <= value_index:
            print "\nExpected a field after '-s'"
            quit()
        else:
            seed_value = args[value_index]
    else:
        print "-s command missing, use -help for additional details."

    # -r: the number of senteneces to generate, defaults to 1
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
                gen_num_sentences = int(value)

    main(seed_value, gen_num_sentences)
