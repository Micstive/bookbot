from stats import get_num_words, get_num_chars, get_sorted

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    contents = get_book_text("./books/frankenstein.txt")
    number_of_words = get_num_words(contents)
    number_of_different_chars = get_num_chars(contents)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {number_of_words} total words\n--------- Character Count -------")
    char_key = "char"
    num_key = "num"
    for char_dict in get_sorted(number_of_different_chars):
        if char_dict["char"].isalpha():
            print(f"{char_dict[char_key]}: {char_dict[num_key]}")
    


main()