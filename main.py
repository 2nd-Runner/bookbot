import sys
from stats import get_num_words
from stats import get_num_characters
from stats import make_sorted_dics

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def format_character_count(func):
    for item in func:
        print(item["char"] + ": " + str(item["num"]))

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(get_book_text(filepath))} total words")
        print("--------- Character Count -------")
        format_character_count(make_sorted_dics(get_num_characters(get_book_text(filepath))))
        print("============= END ===============")

main()