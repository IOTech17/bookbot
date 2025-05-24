import os.path
import sys
from stats import count_words
from stats import character_count
from stats import beautify_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    word_count = count_words(text)
    character_count_result = character_count(text)
    character_list_and_count = beautify_report(character_count_result)
    print ("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print (f"Found {count_words(text)} total words")
    print ("--------- Character Count -------")
    for char in character_list_and_count:
        print (char["char"]+":",char["num"])
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

main()