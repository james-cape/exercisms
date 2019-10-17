def score(word):
    score = 0
    for letter in word:
        if letter.lower() in "aeioulnrst":
            score += 1
        elif letter.lower() in "dg":
            score += 2
        elif letter.lower() in "bcmp":
            score += 3
        elif letter.lower() in "fhvwy":
            score += 4
        elif letter.lower() in "k":
            score += 5
        elif letter.lower() in "jx":
            score += 8
        elif letter.lower() in "qz":
            score += 10
    return score
