def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
    
def print_char_report(sorted_chars):
    string = ""
    for item in sorted_chars:
        if item[0].isalpha() == True:
            if sorted_chars.index(item) == len(sorted_chars) - 1:
                string += f"{item[0]}: {item[1]}"
            else:
                string += f"{item[0]}: {item[1]} \n"
    return string
    
from stats import word_count
from stats import character_counter
from stats import sorter

def main():
    book = get_book_text("./books/frankenstein.txt") 
    num_words = word_count(book)
    num_characters = character_counter(book)
    sorted_list = sorter(num_characters)
    report = print_char_report(sorted_list)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(report)
    print("============= END ===============")
main()

