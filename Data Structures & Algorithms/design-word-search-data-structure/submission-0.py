class TreeNode:
    def __init__(self,word = False):
        self.word = word  
        self.children = [None] * 26


class WordDictionary:
    def __init__(self):
        self.head = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for char in word:
            idx = ord(char)-97
            if curr.children[idx] is None:
                curr.children[idx] = TreeNode()
            curr = curr.children[idx]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(initial_node, init_index, word):
            curr = initial_node
            lower = init_index
            for i in range(init_index,len(word)):
                if word[i] != ".":
                    idx = ord(word[i])-97
                    if curr.children[idx] is None:
                        return False
                    curr = curr.children[idx]
                else:
                    for op in curr.children:
                        if op is not None and dfs(op,lower+1,word):
                            return True
                    return False

                lower += 1
            return curr.word
        
        return dfs(self.head,0,word)
                    
        
            
                

        
