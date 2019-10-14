def is_isogram(string):
    accumulator = {}
    string = string.translate({ord(character): None for character in ['-', ' ']})
    for i in string.lower():
        if i in accumulator:
            return False
        else:
            accumulator[i] = 1
    return True
