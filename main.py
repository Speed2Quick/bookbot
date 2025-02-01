def main():    
    text = read_contents()
    words = word_count(text)
    characters = character_counter(text)
    print(characters)

def read_contents():
    with open("books/frankenstein.txt") as f:
        return f.read()

def word_count(book):
    split_str = book.split()
    return len(split_str)

def character_counter(book):
    lower_case_words = book.lower()
    num_characters = {}
    character_list = list("abcdefghijklmnopqrstuvwyxz0123456789!@#$%^&* ")
    for letter in character_list:
        counter = lower_case_words.count(letter)
        num_characters.update({letter : counter})
    return num_characters











main()



