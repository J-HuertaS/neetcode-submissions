class TreeNode:
    def __init__(self,word = True):
        self.word = word
        self.children = [None for _ in range(26)]


class PrefixTree:

    def __init__(self):
        self.head = TreeNode()

    def insert(self, word: str) -> None:
        temp = word
        curr = self.head
        while len(temp):
            if curr.children[ord(temp[0])-97] is None:
                curr.children[ord(temp[0])-97] = TreeNode(len(temp) == 1)
            elif len(temp) == 1 and curr.children[ord(temp[0])-97].word == False:
                curr.children[ord(temp[0])-97].word = True

            curr = curr.children[ord(temp[0])-97]
            temp = temp[1:]

    def search(self, word: str) -> bool:
        temp = word
        curr = self.head
        while len(temp):
            curr = curr.children[ord(temp[0])-97]
            if curr is None:
                return False
            temp = temp[1:]

        return curr.word

    def startsWith(self, prefix: str) -> bool:
        temp = prefix
        curr = self.head
        while len(temp):
            curr = curr.children[ord(temp[0])-97]
            if curr is None:
                return False
            temp = temp[1:]

        return True
        