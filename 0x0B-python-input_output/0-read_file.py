#!/usr/bin/python3
"""define funtion"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdou

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
