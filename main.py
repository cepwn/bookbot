from stats import get_num_words, get_letter_counts, sort_letter_counts
from sys import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    print("============ BOOKBOT ============")
    file_path = argv[1]
    print(f'Analyzing book found at {file_path}')
    text = get_book_text(f'./{file_path}')
    print("----------- Word Count ----------")
    word_count = get_num_words(text)
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    letter_count = get_letter_counts(text)
    sorted_letter_count = sort_letter_counts(letter_count)
    for dictionary in sorted_letter_count:
        print(f'{dictionary["character"]}: {dictionary["count"]}')
    print("============= END ===============")

main()