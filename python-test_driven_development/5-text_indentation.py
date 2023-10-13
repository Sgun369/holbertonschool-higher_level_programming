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
    
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
