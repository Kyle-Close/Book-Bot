def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    # create a dict
    # iterate over each char in text
    # add to dict as either a new entry and set value to 1 OR increment value for that entry

    char_dict = {}
    for c in text:
        lower = c.lower()
        if lower in char_dict:
            char_dict[lower] = char_dict[lower] + 1
        else:
            char_dict[lower] = 1

    return sort_by_char_count(char_dict)

def sort_by_char_count(char_dict):
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)

