from collections import Counter


class Solution:
    def topKFrequent(self, words, k):
        word_dict = Counter(words)
        sorted_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        top_k = sorted_list[:k]
        return [item[0] for item in top_k]
