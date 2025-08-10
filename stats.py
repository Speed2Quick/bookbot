def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    for letter in text.lower():
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1
    return characters
