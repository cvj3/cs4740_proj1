from __future__ import division
from common import SMOOTHING_LIMIT
from lib.unigram_model import write_unigram_to_file
from lib.bigram_model import write_bigram_to_file
from lib.trigram_model import write_trigram_to_file

# Future Improvement: consider the need to smooth Nc counts to replace any 0s
#        "use linear regression of Nc and c in log space."
#        log(Nc) = a + b log(c)
#  ... otherwise ... missing some mass

# as recommended by Katz (1987); last value of c to apply Good-Turing smoothing

# [X] renamed primary function to createSmoothedModel
# [X]: moved _THRESHOLD to common.py, renamed / all caps
# [X]: import lib.*gram_model.py
# TODO: smoothing map S[C] = c*
# TODO: replace counts of existing model, with c_smoothed counts
# TODO: call write_unigram_to_file(smoothed_unigram)
# TODO: add optional filename parameter
# <smoothed>/>_<genre>_<ngram>_model
# e.g.  crime_bigram_model
# e.g., crime_bigram_model_smoothed


# adjust probability of singletons to account for unknown
# nGram: the unigram, bigram or trigram model
# genre: (optional), not currently used
def createSmoothedModel(nGrams, model, genre="<unk>", verboseMode=False):
    probability = 0

    # cache totalCounts
    N = getTotalCount(nGrams, model)
    # cache max frequency
    cMax = getMaxCount(nGrams, model)
    if verboseMode:
        print "Total %d-nGram count:\t%d" % (nGrams, N)
        print "Max Frequency:\t\t%d" % (cMax)
        print "\r\nc\tNc\tc*\tP*_GT"
        print "=============================="
    # initialize dictionary object
    bins = dict()
    # build dictionary of "c" (MLE) with counts
    for c in range(0, cMax+1):
        Nc = getCount(nGrams, model, c)
        newEntry = [Nc, 0, 0]
        bins.update({c: newEntry})
#        if verboseMode:
#            print "bin[%d]: \t%d" % (c, bins[c][0])

    # loop through each "c", and set/update probability
    for c in range(0, cMax):
        probability = 0
        c_new = c

        if c == 0:
            # return unknown probability
            singletonCount = bins[1][0]
            c_new = c_unknown(singletonCount, N)
            probability = unknown_probability(singletonCount, N)
        if c <= SMOOTHING_LIMIT:
            # get smoothed probability
            if bins[c][0] != 0:
                if bins[c+1][0] != 0:
                    c_new = c_smoothed(c, bins[c+1][0], bins[c][0])
                    probability = smoothed_probability(c, bins[c+1][0], bins[c][0], N)
                else:
                    # naive catch-all for when Nc+1 = 0
                    probability = float(normal_probability(c, N) * unknown_probability(singletonCount, N))
        else:
            # return unsmoothed probability; large counts assumed reliable
            if bins[c][0] != 0:
                probability = normal_probability(c, N)

        bins[c][1] = c_new
        bins[c][2] = probability

    if verboseMode:
        cnt = 0
        for c in range(0, cMax+1):
            if (bins[c][0] != 0) or (c == 0):
                print "%d\t%d\t%f\t%.12f" % (c, bins[c][0], bins[c][1], bins[c][2])
                cnt += 1
            #if cnt > 10:
            #    break

    return probability



def c_smoothed(c, Nc1, Nc):
    c_smoothed = float((c + 1) * (float(Nc1) / Nc))  # shouldn't this be Nc1 / Nc??

    return c_smoothed


# c: number of times an n-gram occurs
# Nc: number of n-grams that occur "c" times
def smoothed_probability(c, Nc1, Nc, totalCount):
    c_smoothed = (c + 1) * (float(Nc1) / Nc)  # shouldn't this be Nc1 / Nc??
    # print float(c_smoothed)

    probabilityGT = float(c_smoothed / totalCount)
    return probabilityGT


# probability of unknown
def unknown_probability(singletonCount, totalCount):
    probability = float(singletonCount / totalCount)
    return probability


# probability of unknown
def c_unknown(singletonCount, totalCount):
    probability = float(singletonCount / totalCount)
    return probability


# c: number of times an n-gram occurs
# Nc: number of n-grams that occur "c" times
def normal_probability(c, totalCount):
    probabilityMLE = float(c / totalCount)
    return probabilityMLE


# export probability table based on "c" (ala page 103 in textbook)
def exportTable(bins, genre):
    raise NotImplementedError
    return False


def getCount(nGrams, model, Nc=1):
    count = 0

    if nGrams == 1:
        for token in model:
            if model[token] == Nc:
                count += 1
    elif nGrams == 2:
        for bigram in model.values():
            for token in bigram:
                if bigram[token] == Nc:
                    count += 1
    elif nGrams == 3:
        for trigram in model:
            for key in model[trigram]:
                # count += float(sum(key.values()))
                for value in model[trigram][key].values():
                    if value == Nc:
                        count += 1

    return count


def getTotalCount(nGrams, model):
    count = 0

    if nGrams == 1:
        for token in model:
            count += model[token]
    elif nGrams == 2:
        for bigram in model.values():
            count += float(sum(bigram.values()))
    elif nGrams == 3:
        for trigram in model:
            for key in model[trigram].values():
                count += float(sum(key.values()))

    return count


def getMaxCount(nGrams, model):
    count = 0

    if nGrams == 1:
        for token in model:
            if model[token] > count:
                count = model[token]
    elif nGrams == 2:
        for bigram in model.values():
            for token in bigram:
                if bigram[token] > count:
                    count += bigram[token]
    elif nGrams == 3:
        for trigram in model:
            for key in model[trigram]:
                # count += float(sum(key.values()))
                for value in model[trigram][key].values():
                    if value > count:
                        count = value

    return count
