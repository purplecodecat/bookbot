def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
       char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

