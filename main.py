import sys
from stats import count_words, count_chars, sort_dict

def main ():

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    sorted_chars = sort_dict(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_path)} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()
