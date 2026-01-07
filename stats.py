#!/usr/bin/python3

def word_count(txt: str) -> int:
    # Primitive word_count function that just splits the text
    # It returns the number of space separated characters
    # "12" would count as a word, so would "-"
    return len(txt.split())

def char_count(txt: str) -> dict:
    chars = dict()
    for c in txt.lower():
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

