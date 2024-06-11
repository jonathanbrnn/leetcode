# [537ms, 23.02mb]
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        self.trie[word] = 1

    def search(self, word: str) -> bool:
        return self.trie[word] > 0

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for i in self.trie.keys():
            if i[:n] == prefix:
                return True
        return False

# [120ms, 30.86mb]
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
