#!/usr/bin/python3
""" function that prints a text with 
2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """define function

    Args:
        text (str): string

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    newline_chars = ('.', '?', ':')
    current_line = ""
    
    for char in text:
        if current_line in newline_chars and char == " ":
            continue
        print(char, end='')
        print('\n' * 1) if char in newline_chars else None
        current_line = char
        
