from english_words import get_english_words_set


def choose_word():
    words = get_english_words_set(['gcide', 'web2'], alpha=True, lower=True)
    word = words.pop()
    words.add(word)
    return word
