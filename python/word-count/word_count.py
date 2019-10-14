def count_words(sentence):
    punctuations = "!&@$%^':&."
    accumulator = {}
    word_breaks = ["\t", "\n", ",", "_", " "]
    for word_break in word_breaks:
        sentence = sentence.lower().replace(word_break, " ")
    for word in sentence.split(" "):
        word = word.strip(punctuations)
        if word in accumulator:
            accumulator[word] += 1
        elif word is not '':
            accumulator[word] = 1
    return accumulator
