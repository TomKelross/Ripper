
banned_words = ["to"]


def remove_spaces(text):
    
    # Removes trailing and leading spaces from text.
    text = text.strip()

    return text

def remove_punct(text):
    
    # String represents valid characters
    string = ''

    for char in text:

        # If character is a letter then add it to string
        if char.isalpha() == True:
            string = string + char

        # If character is a space then add it to string
        if char.isspace() == True:
            string = string + char

    # Return string to the subprogram.
    return string

def string_to_list(text):

    list = text.split(" ")

    return list

def filter_words(words, text):

    important_words = []

    for word in words:
        
        word = word.lower()

        if word.isalpha() == True:
            if word not in banned_words:
                important_words.append(word)
        

    return important_words

text = " Hello my name to is Kyle "

test = remove_spaces(text)

print(test)

test = remove_punct(text)

print(test)

test = string_to_list(text)

print(test)

test = filter_words(test, banned_words)

print(test)
