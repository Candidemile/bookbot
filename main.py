import sys
from tabnanny import check

from stats import get_book_text, get_char_count, get_sorted_char_list, get_words_num


def check_args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]


def main():
    path = check_args()
    book = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    words_count = get_words_num(book)
    print(f"Found {words_count} total words")

    print("----------- Character Count ----------")
    char_count = get_char_count(book)
    sorted_char_list = get_sorted_char_list(char_count)
    for char in sorted_char_list:
        print(f"{char['char']}: {char['num']}")


main()
