def decode(string):
    occurences = ''
    decoded = ''
    last_character = ''
    for character in string:
        if character:
            if not character.isnumeric():
                if last_character.isnumeric():
                    if occurences:
                        decoded += character * int(occurences)
                    else:
                        decoded += character
                    occurences = ''
                else:
                    decoded += character
            else:
                occurences += character
        last_character = character
    return decoded


def encode(string):
    counter = 1
    last_character = ''
    encoded = ''
    for character in string:
        if last_character:
            if character == last_character:
                counter += 1
            else:
                if counter != 1:
                    encoded += str(counter)
                encoded += last_character
                counter = 1
        last_character = character
    if string:
        if counter != 1:
            encoded += str(counter)
        encoded += last_character
    return encoded
