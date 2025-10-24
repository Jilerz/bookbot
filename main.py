from stats import word_count, char_count
def main():
    frank = get_book_text("books/frankenstein.txt")
    num_words = word_count((frank))
    characters = char_count(frank)
    return print(f"Found {num_words} total words.\n {characters}")

def get_book_text(filep):
    with open(filep) as f:
        contents = f.read()
        return contents
main()