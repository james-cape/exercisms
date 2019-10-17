def recite(start_verse, end_verse):
    last_line = "a Partridge in a Pear Tree."
    if end_verse > 1:
        last_line = "and " + last_line

    numbers = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    first_line = "On the {} day of Christmas my true love gave to me: ".format(numbers[start_verse])
    all_lines = [
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ",
        last_line
        ]
    song = ""

    if start_verse == end_verse:
        for i in range(1, end_verse):


            


    song = all_lines[end_verse - start_verse]
    for i in range(1, end_verse + 1):
        if i == end_verse:
            song += last_line
        else:
            song = all_lines[i] + song
    breakpoint()
    return [song]
