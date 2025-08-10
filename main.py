from stats import word_count, character_count, character_sort
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    characters = character_count(text)
    sorted_characters = character_sort(characters)

    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}...")
    print("--------- Word Count ---------")
    print(f"Found {word_count(text)} total words")
    print("-------- Character Count -----")
    for dict in sorted_characters:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("========== END ==========")

def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
    return book_contents

if __name__ == "__main__":
    main()