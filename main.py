def main():
    file_path ="books/frankenstein.txt"
    text = get_book_contents(file_path)
    word_count = count_of_words(text)
    #print(word_count)
    lower_case = text.lower()
    #print(lower_case)
    character_counter = count_characters(lower_case)
    print(character_counter)


def get_book_contents(file_path):
    with open(file_path) as f:
        return f.read()

def count_of_words(text):
    word_count = len(text.split())
    return word_count

def count_characters(lower_case):

    characters = {}
    key = ""
    counter = 0

    for symbol in lower_case:
        key = symbol
        counter = key.count(key)
        characters[key] = counter

    for key in characters.keys():
        characters[key] = lower_case.count(key)

    return characters

main()