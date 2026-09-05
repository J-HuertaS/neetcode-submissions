# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # caso base
        if not root:
            return False

        # se cumple la condicion
        if self.compare(root,subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)

        


    def compare(self, n1: Optional[TreeNode], n2: Optional[TreeNode]):
        # Caso base
        if not n1 and not n2:
            return True
        
        if not n1 or not n2:
            return False
        
        # si hay un nodo con valor diferente
        if n1.val != n2.val:
            return False
        
        return self.compare(n1.left,n2.left) and self.compare(n1.right,n2.right)



        
        