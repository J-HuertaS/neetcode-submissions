class TreeNode:
    def __init__(self,word = True):
        self.word = word
        self.children = [None for _ in range(26)]


class PrefixTree:

    def __init__(self):
        self.head = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            idx = ord(char)-97
            if curr.children[idx] is None:
                curr.children[idx] = TreeNode(False)
            curr = curr.children[idx]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            idx = ord(char)-97
            curr = curr.children[idx]
            if curr is None:
                return False

        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            idx = ord(char)-97
            curr = curr.children[idx]
            if curr is None:
                return False

        return True
        