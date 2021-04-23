word_dict = dict()


def get_word_freq(word):
    if word in word_dict:
        return word_dict[word]


def count_frequencies(book):
    for word in book:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
