class TrieNode:
    def __init__(self):
        self.children = [None]*26
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

    # def get_all_prefix(self, node, word, search_word):
    #     # import pdb; pdb.set_trace()
    #     if node.is_end_of_word:
    #         return word
    #
    #     for i in range(0, 26):
    #         if node.children[i]:
    #             word += chr(i + ord('a'))
    #             word_found = self.get_all_prefix(node.children[i], word, search_word)
    #             if word_found:
    #                 print(word_found)
    #         # word = search_word

    def traverse(self, node, word=['']*20, level=0, search_word=''):
        if node.is_end_of_word:
            if search_word:
                print(search_word, end='')
            for i in range(level):
                print(word[i], end='')
            print('')

        for i in range(0, 26):
            if node.children[i]:
                word[level] = chr(i + ord('a'))
                self.traverse(node.children[i], word=word, level=level+1, search_word=search_word)
            # word = ''


if __name__ == '__main__':
    keys = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    t = Trie()
    for key in keys:
        t.insert(key)
    output = ["Not present in trie",
              "Present in trie"]

    # print("{} ---- {}".format("m", output[t.search("m")]))
    # print("{} ---- {}".format("mo", output[t.search("mo")]))
    # print("{} ---- {}".format("mou", output[t.search("mou")]))
    # print("{} ---- {}".format("mouse", output[t.search("mouse")]))
    node = t.search("mou")
    if node:
        t.traverse(node, search_word="mou")
    # t.traverse(t.root)
