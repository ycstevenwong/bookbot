from stats import count_words, count_chars;
def get_book_text(file):
    with open(file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    file_path = "./books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    words = count_words(file_contents);
    chars = count_chars(file_contents);
    print(f"Found {len(words)} total words")
    print(chars);

if __name__ == "__main__":
    main()