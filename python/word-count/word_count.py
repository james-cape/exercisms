def count_words(sentence):
    accumulator = {}
    words = sentence.split(" ")
    for word in words:
        # breakpoint()
        if word in accumulator:
            accumulator[word] += 1
        else:
            accumulator[word] = 1

    return accumulator
