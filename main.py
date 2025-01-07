def main():
    file_path ="books/frankenstein.txt"
    text = get_book_contents(file_path)
    word_count = count_of_words(text)
    print(word_count)

def get_book_contents(file_path):
    with open(file_path) as f:
        return f.read()

def count_of_words(text):
    word_count = len(text.split())
    return word_count

main()