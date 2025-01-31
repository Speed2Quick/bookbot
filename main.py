def main():    
    text = read_contents()
    words = word_count(text)
    print(words)

def word_count(book):
    split_str = book.split()
    return len(split_str)


def read_contents():
    with open("books/frankenstein.txt") as f:
        return f.read()







main()



