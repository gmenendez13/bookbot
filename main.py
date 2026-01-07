#!/usr/bin/python3

path_to_frankenstein =  "/Users/main/workspace/github/gmenendez/bookbot/books/frankenstein.txt"


def get_book_text(path: str):
    # given a path the function returns the contents.
    # The contents are expected to be text, or book like
    with open(path) as f:
        book = f.read()
    return book

def word_count(txt: str) -> int:
    return len(txt.split())


def main():
    frankenstein = get_book_text(path_to_frankenstein)
    # print(frankenstein)
    print(f"Found {word_count(frankenstein)} total words")

if __name__ == "__main__":
    main()

