class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if node.children[idx] is None:
                node.children[idx] = TrieNode()

            node = node.children[idx]

        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if node.children[idx] is None:
                return False

            node = node.children[idx]

        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            idx = ord(ch) - ord('a')

            if node.children[idx] is None:
                return False

            node = node.children[idx]

        return True