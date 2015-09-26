from common import ALL_PUNCT, END_SENTENCE_PUNCT, add_word_to_sentence, weighted_random_pick
from collections import Counter
import random


def build_trigram_model(tokens):
    q = {}
    for i in range(len(tokens) - 3):
        one = tokens[i]
        two = tokens[i + 1]
        three = tokens[i + 2]
        q[one] = q.get(one, {})
        q[one][two] = q[one].get(two, {})
        q[one][two][three] = q[one][two].get(three, 0) + 1
    return q


def write_trigram_to_file(trigram_model, name):
    f = open("saved_models/" + name + ".py", "w")
    str_model = str(trigram_model).replace(", ", ",\n\t").replace("{", "{\n\t").replace("}", "\n}").replace("},\n\t", "},\n").replace("\t", "", 1)
    write_str = 'model = ' + str_model
    f.write(write_str)
    f.close()


def word_from_trigram_model_and_previous_word(trigram, one, two):
    word = weighted_random_pick(trigram[one][two])
    return word


def generate_trigram_sentences(trigram_model, number):
    for i in range(number):
        one = "."
        while one in ALL_PUNCT:
            one = random.choice(trigram_model.keys())
            two = "."
            all_sub_keys_punct = True
            for key in trigram_model[one].keys():
                if key not in ALL_PUNCT:
                    all_sub_keys_punct = False
            if all_sub_keys_punct:
                one = "."  # Choose new first word if all following tokens are punctuation

            while two in ALL_PUNCT:
                two = random.choice(trigram_model[one].keys())
                all_sub_keys_punct = True
                for key in trigram_model[one][two].keys():
                    if key not in ALL_PUNCT:
                        all_sub_keys_punct = False
                if all_sub_keys_punct:
                    one = "."  # Don't choose a pair of words that are only ever followed by punctuation
                    two = "a"
                    break

        sentence, x = add_word_to_sentence("", one)
        sentence, x = add_word_to_sentence(sentence, two)
        word = None
        while word not in END_SENTENCE_PUNCT:
            word = word_from_trigram_model_and_previous_word(trigram_model, one, two)
            sentence, word = add_word_to_sentence(sentence, word, override=True)
            if word:
                one = two
                two = word
        try:
            print sentence
        except:
            print "Could not print sentence due to an unrecognized character."
        print "\n"
