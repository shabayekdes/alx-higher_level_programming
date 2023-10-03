#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_str = 0
    while new_str < len(text) and text[new_str] == ' ':
        new_str += 1

    while new_str < len(text):
        print(text[new_str], end="")
        if text[new_str] == "\n" or text[new_str] in ".?:":
            if text[new_str] in ".?:":
                print("\n")
            new_str += 1
            while new_str < len(text) and text[new_str] == ' ':
                new_str += 1
            continue
        new_str += 1
