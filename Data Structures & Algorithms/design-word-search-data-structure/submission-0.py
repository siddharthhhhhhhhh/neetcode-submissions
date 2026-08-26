class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofword = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.endofword

            if word[i] == ".":
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            else:
                if word[i] in node.children:
                    return dfs(node.children[word[i]], i+1)
                else: return False
        return dfs(self.root, 0)
                    