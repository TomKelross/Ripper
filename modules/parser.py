
banned_words = ["to", 0]

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

        # If character is a digit then add it to string
        if char.isdigit() == True:
            string = string + char

    # Return string to the subprogram.
    return string

def filter_words(words, text):
    
    #List of 'important' words
    important_words = []

    #Creates a list of words
    words = words.split(" ")

    for word in words:
        
        word = word.lower()
        print(word)

        if word.isalpha() == True:
            if word not in banned_words:
                important_words.append(word)

        if word.isdigit() == True:
            if word not in banned_words: 
                important_words.append(word)
        
    return important_words

def normalize_input(text):

    # Remove trailing spaces from text
    text = remove_spaces(text)

    # Remove punctuation from text 
    text = remove_punct(text)

    # Remove useless words from text
    text = filter_words(text, banned_words)

    return text
