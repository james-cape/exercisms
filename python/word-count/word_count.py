import re


def count_words(sentence):
    punctuations = "!&@$%^':&"
    sentence = sentence.lower()
    accumulator = {}
    # breakpoint()
    sentence = sentence.replace("\t", " ")
    sentence = sentence.replace(".", "")
    sentence = sentence.replace(",\n", " ")
    sentence = sentence.replace(",", " ")
    sentence = sentence.replace("_", " ")
    words = sentence.split(" ")
    for word in words:
        if word in accumulator:
            accumulator[word.strip(punctuations)] += 1
        elif word is not '' and word is not "\n":
            accumulator[word.strip(punctuations)] = 1

    return accumulator
