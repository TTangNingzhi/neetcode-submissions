class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True
        
    def search(self, word: str) -> bool:

        def check(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.is_end
            if word[i] in node.children:
                return check(node.children[word[i]], i + 1)
            if word[i] == ".":
                return any(check(node.children[ch], i + 1) for ch in node.children)
            return False

        return check(self.root, 0)
