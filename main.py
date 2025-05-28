import sys
from stats import count_num_of_words, count_num_of_diff_char


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        number_of_words = count_num_of_words(text)
        char_counts = count_num_of_diff_char(text)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("--------- Character Count -------")
        for char in sorted(char_counts):
            print(f"{char}: {char_counts[char]}")

    else:
        print("Wrong arguments, Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
