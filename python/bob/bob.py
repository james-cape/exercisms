def response(hey_bob):
    for filler in [' ', '\t', '\r', '\n']:
        hey_bob = hey_bob.replace(filler, '')
    has_alpha = any([n.isalpha() for n in hey_bob])
    if not hey_bob:
        response = 'Fine. Be that way!'
    elif hey_bob.upper() == hey_bob and hey_bob.strip()[-1] == '?' and has_alpha:
        response = "Calm down, I know what I'm doing!"
    elif hey_bob.upper() == hey_bob and has_alpha:
        response = "Whoa, chill out!"
    elif hey_bob.strip()[-1] == '?':
        response = 'Sure.'
    else:
        response = "Whatever."
    return response
