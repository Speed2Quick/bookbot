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

def sort_on(item):
    return item["num"]

def character_sort(dict):
    sorted_dicts = []
    for character in dict:
        new_dict = {"char": character, "num": dict[character]}
        sorted_dicts.append(new_dict)
    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts
