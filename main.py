def main():    
    text = read_contents()
    words = word_count(text)
    num_characters = character_counter(text)
    sort = sort_characters(num_characters)
    print(sort)

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

def sort_on(characters):
    for letter in characters:
        key = characters[letter]
    return key

def sort_characters(characters):
    character_dictionaries = []
    for letter in characters:
        key = characters[letter]
        if letter.isalpha() == True:
            character_dictionaries.append({letter : key})    
    for dict in character_dictionaries:
        character_dictionaries.sort(reverse=True, key=sort_on)
    return character_dictionaries

main()



