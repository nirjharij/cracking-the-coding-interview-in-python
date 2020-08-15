from collections import defaultdict


def find_word_distance(words, word1, word2):
    word_dict = defaultdict(list)
    for i in range(len(words)):
        word_dict[words[i]].append(i)

    word1_list = word_dict[word1]
    word2_list = word_dict[word2]

    i = 0
    j = 0

    min_dist = 99999999
    while i < len(word1_list) and j < len(word2_list):
        dist1 = word1_list[i]
        dist2 = word2_list[j]

        if dist1 > dist2:
            dist = dist1 - dist2 - 1
            j += 1
        else:
            dist = dist2 - dist1 - 1
            i += 1

        if dist < min_dist:
            min_dist = dist

        if min_dist < 0:
            min_dist = 0

    return min_dist


print(find_word_distance(['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'e', 'k', 'j', 'n', 'w', 'e', 'f', 'n'], 'e', 'f'))
