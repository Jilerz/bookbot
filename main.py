from stats import word_count, char_count, sorted_list
import sys 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    frank = get_book_text(sys.argv[1])
    num_words = word_count((frank))
    characters = char_count(frank)
    my_sort = sorted_list(characters) 
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("--------- Character Count -------")
    for item in my_sort:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    return


def get_book_text(filep):
    with open(filep, encoding="utf-8") as f:
        contents = f.read()
        return contents
main()