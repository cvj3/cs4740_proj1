from common import END_SENTENCE_PUNCT, add_word_to_sentence, weighted_random_pick
from collections import Counter
import random


def build_bigram_model(tokens):
    bigram_model = {}
    for i in range(len(tokens) - 1):
        token_curr = tokens[i]
        token_next = tokens[i + 1]
        bigram_model[token_curr] = bigram_model.get(token_curr, {})
        bigram_model[token_curr][token_next] = bigram_model[token_curr].get(token_next, 0) + 1
    return bigram_model


def write_bigram_to_file(bigram_model):
    f = open("saved_models/bigram.py", "w")
    str_model = str(bigram_model).replace(", ", ",\n\t").replace("{", "{\n\t").replace("}", "\n}").replace("},\n\t", "},\n").replace("\t", "", 1)
    write_str = 'bigram_model = ' + str_model
    f.write(write_str)
    f.close()


def word_from_bigram_model_and_previous_word(bigram, word):
    word = weighted_random_pick(bigram[word])
    return word


def generate_bigram_sentences(bigram_model, number, sentence="", starting_word="."):
    for i in range(number):
        if starting_word != "." and not bigram_model.get(starting_word):
            starting_word = "."
            sentence = ""
            print "Error occurred, starting word = '" + starting_word + "' doesn't exist in corpus.  Generating random sentence."
        while starting_word in END_SENTENCE_PUNCT:
            starting_word = random.choice(bigram_model.keys())
        if not sentence:
            sentence = starting_word.title()
        base_word = starting_word
        word = None
        while word not in END_SENTENCE_PUNCT:
            word = word_from_bigram_model_and_previous_word(bigram_model, base_word)
            sentence, word = add_word_to_sentence(sentence, word)
            if word:
                base_word = word
        try:
            print sentence
        except:
            print "Could not print sentence due to an unrecognized character."
        print "\n"


def getSingletonCount(bigram_model):
    count = 0

    for bigram in bigram_model.values():
        for token in bigram:
            if bigram[token] == 1:
                count += 1

    return count


def getTotalCount(bigram_model):
    count = 0

    for bigram in bigram_model.values():
        count += float(sum(bigram.values()))

    return count
