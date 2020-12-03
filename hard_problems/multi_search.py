def multi_search(big_str, small_str_list):
    t = Trie()
    final_out = []
    for word in small_str_list:
        t.insert(word)

    for i in range(len(big_str)):
        for j in range(i, len(big_str)):
            search_word = big_str[i:j+1]
            if t.search(search_word):
                final_out.append(search_word)

    print(final_out)


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        node = self.root
        for i in range(0, len(key)):
            index = self.char_to_index(key[i])
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True

    def search(self, key):
        node = self.root
        for i in range(0, len(key)):
            index = self.char_to_index(key[i])
            if not node.children[index]:
                return False
            node = node.children[index]
        return node


multi_search("nirjhari", ["jhari", "nir", "jha", "alcalk", "abc"])
