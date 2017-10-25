
banned_words = ["to", "the", "in"]

def remove_spaces(text):
    """
    @Description:
    This function removes extra spaces from the string
    @Author: Kyle Morris
    @Testers: Kawthar, Judith 

    >>> remove_spaces(" go to docks ")
    'go to docks'
    >>> remove_spaces("  go to docks  ")
    'go to docks'
    >>> remove_spaces(" go  to  docks  ")
    'go to docks'
    >>> remove_spaces(" go  to  docks  ")
    'go to docks'
    """
    #Removes whitespace
    text = " ".join(text.split())

    # Removes trailing and leading spaces from text.
    text = text.strip()

    return text

def remove_punct(text):
    """
    @Description: 
    This functions removes punctuations
    @Author: Kyle Morris
    @Testers: Kawthar, Judith 

    >>> remove_punct("!?!?!?!!?")
    ''
    >>> remove_punct("go! to! m!a!r!k!etplace!")
    'go to marketplace'
    >>> remove_punct("wait 50!")
    'wait 50'
    """
    
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

def filter_words(words, banned_words):
    """
    @Description:
    This function remove the words included in banned words list from the string
    @Author: Kyle Morris
    @Testers: Kawthar, Judith 

    >>> filter_words("to the 0 in", banned_words)
    []
    >>> filter_words("take the weapon", banned_words)
    ['take', 'weapon']
    >>> filter_words("0 items", banned_words)
    ['items']
    >>> filter_words("10 00000000000 50 22", banned_words)
    ['10', '50', '22']
    """

    # List of 'important' words
    important_words = []

    # Creates a list of words
    words = words.split(" ")

    for word in words:

        if word.isalpha() == True:
            if word not in banned_words:
                important_words.append(word)

        # Remove any instances of 0.
        if word.isdigit() == True:
            
            # Cast to integer to check numericaly
            word = int(word)
            
            # If zero then....
            if word != 0:
                
                # Cast back to word
                word = str(word)    

                # Append to words
                important_words.append(word)

    return important_words

def normalize_input(text):
    """
    @Descirption:
    This function removing banned words, punctuation and extra spaces
    @Author: Kyle Morris
    @Testers: Kawthar, Judith 

    >>> normalize_input("go to dock")
    ['go', 'dock']
    >>> normalize_input("go! to !factory")
    ['go', 'factory']
    >>> normalize_input("go  to  factory!")
    ['go', 'factory']
    """
    
    # Remove trailing spaces from text
    text = remove_spaces(text)

    # Remove punctuation from text 
    text = remove_punct(text)

    # Remove useless words from text
    text = filter_words(text, banned_words)

    return text
