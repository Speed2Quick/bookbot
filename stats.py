def word_count(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def character_counter(text):
    characters = list("abcdefghijklmnopqrstuvwyxzæâêëô")
    letter_dict = {}
    lower_cased_text = text.lower()
    counter = 0
    for letter in characters:  
        counter = lower_cased_text.count(letter)
        letter_dict[letter] = counter
    return letter_dict

def sorter(characters):
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    return sorted_characters


