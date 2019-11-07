def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if not isbn[0:9].isdigit() or len(isbn) != 10:
        return False
    x1 = int(isbn[0])
    x2 = int(isbn[1])
    x3 = int(isbn[2])
    x4 = int(isbn[3])
    x5 = int(isbn[4])
    x6 = int(isbn[5])
    x7 = int(isbn[6])
    x8 = int(isbn[7])
    x9 = int(isbn[8])
    if isbn[9] == 'X':
        x10 = 10
    elif isbn[9].isdigit():
        x10 = int(isbn[9])
    else:
        return False
    return (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) % 11 == 0
