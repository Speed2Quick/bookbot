def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def word_count(text):
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
        text = str(file_contents)
        words = text.split()
        counter = 0
        for word in words:
            counter += 1
        print(counter)
    
word_count(main)

main()



