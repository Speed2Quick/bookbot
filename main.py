import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
    
def print_char_report(sorted_chars):
    report = ""
    for char_data in sorted_chars:
        if char_data[0].isalpha() == True:
            if sorted_chars.index(char_data) == len(sorted_chars) - 1:
                report += f"{char_data[0]}: {char_data[1]}"
            else:
                report += f"{char_data[0]}: {char_data[1]} \n"
    return report
    
from stats import word_count
from stats import character_counter
from stats import sorter

def main():
    book = get_book_text(f"{book_path}") 
    num_words = word_count(book)
    num_characters = character_counter(book)
    sorted_list = sorter(num_characters)
    report = print_char_report(sorted_list)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(report)
    print("============= END ===============")
main()

