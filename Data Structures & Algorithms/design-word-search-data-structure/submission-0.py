class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.wordEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            i = ord(char) - ord('a')
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.wordEnd = True


    def search(self, word: str) -> bool:
        def dfs(node, i):
            if node is None:
                return False
            if i == len(word):
                return node.wordEnd

            char = word[i]

            if char == '.':
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False

            idx = ord(char) - ord('a')
            return dfs(node.children[idx], i + 1)

        return dfs(self.root, 0)