from stats import count_words, count_chars, sort_chars;
def get_book_text(file):
    with open(file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    words = count_words(file_contents);
    chars = count_chars(file_contents);
    sorted_chars = sort_chars(chars);
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")
    print("--------- Character Count -------")
    for key,value in sorted_chars.items():
        print(f"{key}: {value}");
    print("============= END ===============")

if __name__ == "__main__":
    main()