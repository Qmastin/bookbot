def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalnum():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars
def sort_on(item):
    return item["num"]
def sort_characters(char_dict):
    dict_list =[{"char": char, "num": count} for char, count in char_dict.items()]
    dict_list.sort(reverse = True, key=sort_on)
    return dict_list