import re

def parse(text_input):
    text_input = text_input.lower()
    print('origninal text')
    print(text_input)
    set_words = set(re.split('\.|,|;|=| |\n|\s|\(|\)', text_input))

    #remove digits
    keep_words = [ w for w in set_words if w.isdigit() == False and len(w) > 2 ]
    removed_token = [ w for w in set_words if w.isdigit() == True or 0 < len(w) <= 2 ]

    print('tokenaze text')
    print(set_words)

    print('keep words')
    print(keep_words)

    print('removed words')
    print(removed_token)
    return keep_words, removed_token

#text = """
#If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it. If you don’t explicitly close a file, Python’s garbage collector will eventually destroy the object and close the open file for you, but the file may stay open for a while. Another risk is that different Python implementations will do this clean-up at different times. 15 12.541
#"""
#parse(text)
