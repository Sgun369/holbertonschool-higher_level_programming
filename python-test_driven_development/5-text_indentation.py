#!/usr/bin/python3
"""

"""

def text_indentation(text):
    """
    print the text with two new lines after each of the 
    characters '.', '?', and ':'.

    parameters:
        tect(str): The input text.
    
    Raises:
        TypeError: If the text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    lines = text.split('.')
    for line in lines:
        sentences = line.split('?')
        for sentence in sentences:
            phrases = sentence.split(':')
            for phrase in phrases:
                print(phrase.strip())
            print()
        print()
