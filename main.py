#!/usr/bin/python3

import sys
from stats import word_count, char_count, sort_chars_by_count


def get_book_text(path: str):
    # given a path the function returns the contents.
    # The contents are expected to be text, or book like
    with open(path) as f:
        book = f.read()
    return book

def main():
    # loading the book and data 
    book = get_book_text(path_to_book)
    char_count_dict = char_count(book)

    # Header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")

    print("----------- Word Count ----------")
    print(f"Found {word_count(book)} total words")

    print("--------- Character Count -------")
    # prints each character and its count in a new line
    for char_tuple in sort_chars_by_count(char_count_dict):
        if char_tuple[0].isalpha():
            print(f"{char_tuple[0]}: {char_tuple[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1] 

    main()
    print("============= END ===============")

