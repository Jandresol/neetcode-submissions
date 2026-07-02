class TrieNode:
    def __init__(self):
        # 26 branches
        self.children = [None] * 26
        self.wordEnd = False
        
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            i = ord(char) - ord('a')
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.wordEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            i = ord(char) - ord('a')
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return cur.wordEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            i = ord(char) - ord('a')
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True

        