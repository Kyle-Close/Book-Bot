from stats import count_words, count_chars;
import sys

def main():
    args = sys.argv
    
    if(len(args) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = args[1]
    text = get_book_text(path)

    word_count = count_words(text)
    char_dict = count_chars(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for key, value in char_dict:
        if(key.isalpha()):
            print(f"{key}: {value}")

    print("============= END ===============")

def get_book_text(filepath):
    try:
        with open(filepath, "r") as f:
            file_contents = f.read()
            return file_contents
    except Exception as e:
        print(e)

main()
