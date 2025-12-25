def count_words(file_contents):
    words = file_contents.split();
    return words;

def count_chars(file_contents):
    chars_dict = {};
    full_contents = file_contents.lower();
    for char in full_contents:
        if char not in chars_dict:
            chars_dict[char] = 1;
        else:
            chars_dict[char] += 1;
    return chars_dict;

def sort_chars(chars_dict):
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1],reverse=True))
    return sorted_dict;
