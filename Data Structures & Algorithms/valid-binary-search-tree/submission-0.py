# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.verify(root, float('-inf'), float('inf'))

    def verify(self, node: Optional[TreeNode], min_value: int, max_value: int):
        # caso base
        if not node:
            return True

        # verifica
        if not (min_value < node.val < max_value):
            return False

        return self.verify(node.left, min_value,node.val) and self.verify(node.right,node.val,max_value)
            

        