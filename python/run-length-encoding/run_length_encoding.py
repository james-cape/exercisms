def decode(string):
    occurences = ''
    decoded = ''
    last_character = ''
    for character in string:
        if character and character.isnumeric():
            occurences += character
        elif last_character.isnumeric():
            if occurences:
                decoded += character * int(occurences)
            else:
                decoded += character
            occurences = ''
        else:
            decoded += character
        last_character = character
    return decoded

def encode(string):
    counter = 1
    last_character = ''
    encoded = ''
    for character in string:
        if last_character and character == last_character:
            counter += 1
        else:
            if counter != 1:
                encoded += str(counter)
            encoded += last_character
            counter = 1
            last_character = character
    if string and counter != 1:
        encoded += str(counter)
    encoded += last_character
    return encoded
