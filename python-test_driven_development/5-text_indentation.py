#!/usr/bin/python3
"""

"""


def text_indentation(text):
    """
    print the text with two new lines after each of the
    characters '.', '?', and ':'.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    line_without_spaces = [lines.strip(' ') for lines in text.split('\n')]
    formatted_text = "\n".join(line_without_spaces)
    print(formatted_text, end="")
