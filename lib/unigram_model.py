from common import END_SENTENCE_PUNCT, add_word_to_sentence, weighted_random_pick
import random


def build_unigram_model(tokens):
    unigram_model = {}
    for token in tokens:
        unigram_model[token] = unigram_model.get(token, 0) + 1
    return unigram_model


def write_unigram_to_file(unigram_model, name):
    f = open("saved_models/" + name + ".py", "w")
    str_model = str(unigram_model).replace(", ", ",\n\t").replace("{","{\n\t").replace("}","\n}")
    write_str = 'model = ' + str_model
    f.write(write_str)
    f.close()


def generate_unigram_sentences(unigram_model, number):
    for i in range(number):
        sentence = ""
        word = None
        while word not in END_SENTENCE_PUNCT:
            word = weighted_random_pick(unigram_model)
            sentence, word = add_word_to_sentence(sentence, word)
        try:
            print sentence
        except:
            print "Could not print sentence due to an unrecognized character."
        print "\n"


def getSingletonCount(unigram_model):
    count = 0

    for token in unigram_model:
        if unigram_model[token] == 1:
            count += unigram_model[token]

    return count


def getTotalCount(unigram_model):
    count = 0

    for token in unigram_model:
        count += unigram_model[token]
    # short-hand for above logic:
    # print float(sum(unigram_model.values()))

    return count

