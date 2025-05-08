import sys
from stats import count_words, appearances, sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = count_words(text) 
    appearances_count = appearances(text)
    sorted_chars = sorted_list(appearances_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    for x in sorted_chars:
        y = x["char"]
        z = x["num"]
        if y.isalpha():
            print(f"{y}: {z}")
    
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()