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
        return node!=None and node.is_end_of_word


if __name__ == '__main__':
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    t = Trie()
    for key in keys:
        t.insert(key)
    output = ["Not present in trie",
              "Present in trie"]

    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))