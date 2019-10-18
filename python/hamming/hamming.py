def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("String lengths don't match")
    counter = 0
    for i in range(len(strand_a)):
        if strand_a[i] is not strand_b[i]:
            counter += 1

    return counter
