class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def char_to_index(self, ch):
        return ord(ch) - ord('a')

    def index_to_char(self, index):
        return chr(index + ord('a'))

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

    # def traverse(self, node, word=['']*20, level=0, search_word=''):
    #     if node.is_end_of_word:
    #         if search_word:
    #             print(search_word, end='')
    #         for i in range(level):
    #             print(word[i], end='')
    #         print('')
    #
    #     for i in range(0, 26):
    #         if node.children[i]:
    #             word[level] = chr(i + ord('a'))
    #             self.traverse(node.children[i], word=word, level=level+1, search_word=search_word)
    #         # word = ''
            
    def suggestions(self, node, word):
        if node.is_end_of_word:
            self.word_list.append(word)

        for i in range(0, 26):
            if node.children[i]:
                letter = self.index_to_char(i)
                self.suggestions(node.children[i], word+letter)


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
    node = t.search("mon")
    if node:
        # t.traverse(node, search_word="mou")
        t.suggestions(node, "mon")
    print(t.word_list)
    # t.traverse(t.root)
