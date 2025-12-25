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

def sort_on(d):
    return d["num"]

def sort_chars(chars_dict):
    chars_list = []
    for char in chars_dict:
        chars_list.append({"char": char, "num": chars_dict[char]})
    chars_list.sort(reverse=True,key=sort_on);
    return chars_list;

