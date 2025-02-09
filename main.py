def main():
    file_path ="books/frankenstein.txt"
    text = get_book_contents(file_path)
    word_count = count_of_words(text)
    #print(word_count)
    lower_case = text.lower()
    #print(lower_case)
    character_counter = count_characters(lower_case)
    #print(character_counter)
    print_report(word_count, character_counter)

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

def print_report(word_count, character_counter):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for key in character_counter.keys():
        if key.isalpha() == True:
            value = character_counter.get(key)
            print (f"The '{key}' character was found {value} times")

    print("--- End report ---")

main()