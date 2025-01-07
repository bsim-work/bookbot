def main():
    file_path ="books/frankenstein.txt"
    text = get_book_contents(file_path)
    print(text)

def get_book_contents(file_path):
    with open(file_path) as f:
        return f.read()

main()    