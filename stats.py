#!/usr/bin/python3

def word_count(txt: str) -> int:
    # Primitive word_count function that just splits the text
    # It returns the number of space separated characters
    # "12" would count as a word, so would "-"
    return len(txt.split())

def char_count(txt: str) -> dict:
    # counts each character in the text.
    # return a dictionary key: character value: count
    chars = dict()
    for c in txt.lower():
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

def sort_chars_by_count(chars: dict):
    # takes in a dictionary of chararters and their count
    # returns a list of tuples with the character and count in each

    l = [(k,v) for k,v in chars.items()]
    return sorted(l, reverse=True, key=lambda x: x[1])
