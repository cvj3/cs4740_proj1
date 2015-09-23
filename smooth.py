from lib.unigram_model import write_unigram_to_file
from lib.bigram_model import  write_bigram_to_file
from lib.trigram_model import write_trigram_to_file
import os
import sys
from lib.GoodTuring import createSmoothedModel
import datetime

__author__ = "Alin Barsan, Curtis Josey"


# Good-Turning discounting/smoothing (and unknown words) in the test data;
# explain why you need this for steps 4 (perplexity) and 5 (genre classification)


# load model
# estimate probability of unseens words, by counting
# ... things only seen once / total # of words


def main():
    print "\nCreating 'Children' Unigram Model with Good-Turing Smoothing..."
    start = datetime.datetime.now()
    from saved_models.children_unigram import model    
    end = datetime.datetime.now()
    print "\tLoaded model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    smoothed_model = createSmoothedModel(1, model)
    end = datetime.datetime.now()
    print "\tSmoothed model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    write_unigram_to_file(smoothed_model, "children_unigram_smoothed")
    end = datetime.datetime.now()
    print "\tSaved model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)


    print "\nCreating 'Children' Bigram Model with Good-Turing Smoothing..."
    start = datetime.datetime.now()
    from saved_models.children_bigram import model    
    end = datetime.datetime.now()
    print "\tLoaded model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    smoothed_model = createSmoothedModel(2, model)
    end = datetime.datetime.now()
    print "\tSmoothed model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    write_unigram_to_file(smoothed_model, "children_bigram_smoothed")
    end = datetime.datetime.now()
    print "\tSaved model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)


    print "\nCreating 'Children' Trigram Model with Good-Turing Smoothing..."
    start = datetime.datetime.now()
    from saved_models.children_trigram import model    
    end = datetime.datetime.now()
    print "\tLoaded model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    smoothed_model = createSmoothedModel(3, model)
    end = datetime.datetime.now()
    print "\tSmoothed model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    write_unigram_to_file(smoothed_model, "children_trigram_smoothed")
    end = datetime.datetime.now()
    print "\tSaved model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)


    print "\nCreating 'Crime' Unigram Model with Good-Turing Smoothing..."
    start = datetime.datetime.now()
    from saved_models.crime_unigram import model    
    end = datetime.datetime.now()
    print "\tLoaded model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    smoothed_model = createSmoothedModel(1, model)
    end = datetime.datetime.now()
    print "\tSmoothed model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    write_unigram_to_file(smoothed_model, "crime_unigram_smoothed")
    end = datetime.datetime.now()
    print "\tSaved model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)


    print "\nCreating 'Crime' Bigram Model with Good-Turing Smoothing..."
    start = datetime.datetime.now()
    from saved_models.crime_bigram import model    
    end = datetime.datetime.now()
    print "\tLoaded model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    smoothed_model = createSmoothedModel(2, model)
    end = datetime.datetime.now()
    print "\tSmoothed model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    write_unigram_to_file(smoothed_model, "crime_bigram_smoothed")
    end = datetime.datetime.now()
    print "\tSaved model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)


    print "\nCreating 'Crime' Trigram Model with Good-Turing Smoothing..."
    start = datetime.datetime.now()
    from saved_models.crime_trigram import model    
    end = datetime.datetime.now()
    print "\tLoaded model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    smoothed_model = createSmoothedModel(3, model)
    end = datetime.datetime.now()
    print "\tSmoothed model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    write_unigram_to_file(smoothed_model, "crime_trigram_smoothed")
    end = datetime.datetime.now()
    print "\tSaved model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)


    print "\nCreating 'History' Unigram Model with Good-Turing Smoothing..."
    start = datetime.datetime.now()
    from saved_models.history_unigram import model    
    end = datetime.datetime.now()
    print "\tLoaded model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    smoothed_model = createSmoothedModel(1, model)
    end = datetime.datetime.now()
    print "\tSmoothed model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    write_unigram_to_file(smoothed_model, "history_unigram_smoothed")
    end = datetime.datetime.now()
    print "\tSaved model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)


    print "\nCreating 'History' Bigram Model with Good-Turing Smoothing..."
    start = datetime.datetime.now()
    from saved_models.history_bigram import model    
    end = datetime.datetime.now()
    print "\tLoaded model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    smoothed_model = createSmoothedModel(2, model)
    end = datetime.datetime.now()
    print "\tSmoothed model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    write_unigram_to_file(smoothed_model, "history_bigram_smoothed")
    end = datetime.datetime.now()
    print "\tSaved model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)


    print "\nCreating 'History' Trigram Model with Good-Turing Smoothing..."
    start = datetime.datetime.now()
    from saved_models.history_trigram import model    
    end = datetime.datetime.now()
    print "\tLoaded model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    smoothed_model = createSmoothedModel(3, model)
    end = datetime.datetime.now()
    print "\tSmoothed model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

    start = datetime.datetime.now()
    write_unigram_to_file(smoothed_model, "history_trigram_smoothed")
    end = datetime.datetime.now()
    print "\tSaved model in %s seconds." % str(float((end-start).seconds) + (end-start).microseconds / 1000000.0)

# argument for the "seed", optional number of sentences
if __name__ == "__main__":
    # cache arguments passed via command line
    args = sys.argv

    # -h or -help or --help or no arguments supplied
    if "-h" in args or "-help" in args or "--help" in args:
        print "\n\n" + os.path.basename(__file__) + " USAGE GUIDE:\n\n"

        print "\t-h, -help, or --help\n"
        print "\t\tDisplays the help menu which describes all possible arguments."

        print "\n\n\tSAMPLE USAGE:\n\t\tpython " + os.path.basename(__file__)
        quit()

    main()
