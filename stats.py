def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_counts(text):
    letter_counts = dict()
    for char in text:
        lowercase_char = char.lower()
        if letter_counts.get(lowercase_char):
            letter_counts[lowercase_char] += 1
        else:
            letter_counts[lowercase_char] = 1
    return letter_counts

def sort_letter_counts(letter_counts):
    dictionary_list = []
    for key, value in letter_counts.items():
        if not key.isalpha():
            continue
        dictionary_list.append({'character': key, 'count': value})
    dictionary_list.sort(reverse=False, key=lambda x: x['character'])
    return dictionary_list