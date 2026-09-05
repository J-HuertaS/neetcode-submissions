# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # si no hay root, return
        if not root:
            return None

        # invertir ramas
        temp = root.left
        root.left = root.right
        root.right = temp

        # llamado recursivo
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        
        return root

        