import sys
from stats import get_num_words, get_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        fileContents = f.read()
        return fileContents

def sort_on(items):
    return items["num"]

def sort_char_counts(char_counts):
    chars = []
    for key, val in char_counts.items():
        chars.append({"char": key, "num": val})
    
    chars.sort(reverse=True, key=sort_on)
    return chars


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)

    # get the stats
    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_counts = sort_char_counts(char_counts)

    # print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_counts:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')

    print("============= END ===============")


if __name__ == "__main__":
    main()
