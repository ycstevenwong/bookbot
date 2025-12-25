def count_words(file_contents):
    words = file_contents.split();
    return words;

def count_chars(file_contents):
    chars_list = {};
    full_contents = file_contents.lower();
    for char in full_contents:
        if char not in chars_list:
            chars_list[char] = 1;
        else:
            chars_list[char] += 1;
    return chars_list;