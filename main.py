def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

from stats import word_count
from stats import character_counter

def main():
    book = get_book_text("./books/frankenstein.txt") 
    num_words = word_count(book)
    num_characters = character_counter(book)
    print(book)
    print(f"{num_words} words found in the document")      
    print(num_characters)   
main()
