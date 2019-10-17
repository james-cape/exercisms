def abbreviate(words):
    acronym = ""
    for word in words.replace("-", " ").replace("_", " ").split(" "):
        if word: acronym += word[0].upper() 
    return acronym
