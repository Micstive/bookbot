from stats import get_num_words, get_num_chars, get_sorted
import sys

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(sys.argv[1])
    number_of_words = get_num_words(contents)
    number_of_different_chars = get_num_chars(contents)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {number_of_words} total words\n--------- Character Count -------")
    char_key = "char"
    num_key = "num"
    for char_dict in get_sorted(number_of_different_chars):
        if char_dict["char"].isalpha():
            print(f"{char_dict[char_key]}: {char_dict[num_key]}")
    


main()