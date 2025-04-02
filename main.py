import sys
from stats import get_word_count, get_character_count, sort_character_dict

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)

    print(f"Found {word_count} total words")

    character_dict = get_character_count(book_text)
    dict_arr = sort_character_dict(character_dict)

    for item in dict_arr:
        print(f"{item["character"]}: {item["value"]}")

main()
