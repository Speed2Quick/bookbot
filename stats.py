def word_count(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def character_counter(text):
    characters = list("abcdefghijklmnopqrstuvwyxz ,.!?")
    letter_counter = {}
    lower_cased_text = text.lower()
    counter = 0
    for letter in characters:
        counter = lower_cased_text.count(letter)
        letter_counter[letter] = counter
    return letter_counter