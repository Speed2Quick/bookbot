def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def main():
    book = get_book_text("./books/frankenstein.txt") 
    num_words = word_count(book)
    print(book)
    print(f"{num_words} words found in the document")         
main()
