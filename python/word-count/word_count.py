import re


def count_words(sentence):
    # punctuations = ''':!()-[]{};'"\,<>./?@#$%^&*_~'''
    punctuations = ':!&@$%^&'
    sentence = sentence.strip(punctuations)
    accumulator = {}
    sentence = sentence.replace(":", "")
    sentence = sentence.replace(",\n", " ")
    sentence = sentence.replace(",", " ")
    words = sentence.split(" ")
    for word in words:
        if word in accumulator:
            accumulator[word] += 1
        else:
            accumulator[word] = 1

    return accumulator
