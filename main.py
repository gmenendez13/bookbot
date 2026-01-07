#!/usr/bin/python3

from stats import word_count, char_count

path_to_frankenstein =  "/Users/main/workspace/github/gmenendez/bookbot/books/frankenstein.txt"


def get_book_text(path: str):
    # given a path the function returns the contents.
    # The contents are expected to be text, or book like
    with open(path) as f:
        book = f.read()
    return book


def main():
    frankenstein = get_book_text(path_to_frankenstein)
    # print(frankenstein)
    print(f"Found {word_count(frankenstein)} total words")
    print(char_count(frankenstein))


if __name__ == "__main__":
    main()

