from stats import word_count, character_count

def main():

    text = get_book_text("books/frankenstein.txt")
    characters = character_count(text)
    print(f"{word_count(text)} words found in the document")
    print(character_count(text))

def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
    return book_contents

if __name__ == "__main__":
    main()