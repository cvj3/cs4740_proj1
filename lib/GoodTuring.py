from __future__ import division
from common import SMOOTHING_LIMIT

# Future Improvement: consider the need to smooth Nc counts to replace any 0s
#        "use linear regression of Nc and c in log space."
#        log(Nc) = a + b log(c)
#  ... otherwise ... missing some mass

# as recommended by Katz (1987); last value of c to apply Good-Turing smoothing

# NOT IMPLEMENTED: smoothing map S[C] = c*
# NOT IMPLEMENTED: add an new <u> value
# NOT IMPLEMENTED: if value above threshold, just pass c back unmodified
# NOT IMPLEMENTED: else return smoothed c
# NOT IMPLEMENTED: add "<unk>" = computed (sum [c*'s]') * p(<unk>) / (1 - p(<unk>))


# probabilityUnknown, convert to a count* ()
# P(<u>) = u* / (u* + all)
# A { B: 1, C: 1}
# P(<u>) = .33
# A { B: 1, C: 1, <u> = 1} ... because they all sum to 1

# Pu * all / (1 - Pu) = 1/3(unknown probability) * 2(words) / (1 - 1/3 (unknown probability)) = 2/3 / 2/3 = 1


# adjust probability of singletons to account for unknown
# nGram: the unigram, bigram or trigram model
# genre: (optional), not currently used
def createSmoothedModel(nGrams, model, verboseMode=False):
    probability = 0

    # build dictionary of "c" (MLE) with counts - get dictionary of format {count: number_of_occurences}
    # get total count and max count
    bins, N, cMax = getCounts(nGrams, model)
    # turn into format: {count: [number_of_occurences, 0, 0]}
    # also adds in any unseen counts up to max with # of occurences = 0
    for c in range(0, cMax+1):
        bins[c] = [bins.get(c,0), 0, 0]

    if verboseMode:
        print "Total %d-nGram count:\t%d" % (nGrams, N)
        print "Max Frequency:\t\t%d" % (cMax)
        print "\r\nc\tNc\tc*\t\tP*_GT"
        print "=============================================="

    # loop through each "c", and set/update probability
    for c in range(0, cMax+1):
        probability = 0
        c_star = c
        # print c
        if c <= SMOOTHING_LIMIT:
            if c == 0:
                # return unknown probability
                singletonCount = bins[1][0]
                probability = unknown_probability(singletonCount, N)
            else:
                # get smoothed probability
                if bins[c+1][0] != 0:
                    c_star = c_smoothed(c, bins[c+1][0], bins[c][0])
                    probability = smoothed_probability(c, bins[c+1][0], bins[c][0], N)
                else:
                    probability = 0
                    # naive catch-all for when Nc+1 = 0
                    probability = float(normal_probability(c, N) * unknown_probability(singletonCount, N))
        else:
            # return unsmoothed probability; large counts assumed reliable
            if bins[c][0] != 0:
                probability = normal_probability(c, N)

        # print c_star
        bins[c][1] = c_star
        bins[c][2] = probability

    if verboseMode:
        cnt = 0
        for c in range(0, cMax+1):
            if (bins[c][0] != 0) or (c == 0):
                print "%d\t%d\t%f\t%.12f" % (c, bins[c][0], bins[c][1], bins[c][2])
                cnt += 1
            if cnt > 10:
                break
        if cMax > 10:
            for c in range((cMax - 10), cMax+1):
                if (bins[c][0] != 0) or (c == 0):
                    print "%d\t%d\t%f\t%.12f" % (c, bins[c][0], bins[c][1], bins[c][2])
                    cnt += 1
    smoothed_model = updateModel(nGrams, model, bins)
    return model


# c*=(c + 1) N(c+1)/Nc
def c_smoothed(c, Nc_plus1, Nc):
    ret_value = (c + 1) * float(Nc_plus1 / Nc)
    return ret_value


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


def getCounts(nGrams, model):
    bins = {}
    N = 0
    cMax = 0

    if nGrams == 1:
        for token in model:
            value = model[token]
            bins[value] = bins.get(value, 0) + 1
            N += value
            if value > cMax: cMax = value
    elif nGrams == 2:
        for bigram in model.values():
            for token in bigram:
                value = bigram[token]
                bins[value] = bins.get(value, 0) + 1
                N += value
                if value > cMax: cMax = value
    elif nGrams == 3:
        for trigram in model:
            for key in model[trigram]:
                for value in model[trigram][key].values():
                    bins[value] = bins.get(value, 0) + 1
                    N += value
                    if value > cMax: cMax = value

    return bins, N, cMax

def updateModel(nGrams, model, bins):
    prob_unk = bins[0][2]
    if nGrams == 1:
        local_sum = 0
        for token in model:
            value = model[token]
            model[token] = bins[value][1]
            local_sum += model[token]
        model["<unk>"] = (prob_unk * local_sum) / (1 - prob_unk)
            
    elif nGrams == 2:
        for bigram in model.values():
            local_sum = 0
            for token in bigram:
                value = bigram[token]                
                bigram[token] = bins[value][1]
                local_sum += bigram[token]
            bigram["<unk>"] = (prob_unk * local_sum) / (1 - prob_unk)
    elif nGrams == 3:
        for one in model:
            for two in model[one]:
                local_sum = 0
                for three in model[one][two].keys():
                    value = model[one][two][three]
                    model[one][two][three] = bins[value][1]
                    local_sum += model[one][two][three]
                model[one][two]["<unk>"] = (prob_unk * local_sum) / (1 - prob_unk)
    return model