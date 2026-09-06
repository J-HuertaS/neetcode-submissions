# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val >= root.val or q.val >= root.val:
            return root

        pointer = root.left
        while pointer:
            if (p.val <= pointer.val and q.val >= pointer.val) or (p.val >= pointer.val and q.val <= pointer.val):
                return pointer
            elif (p.val <= pointer.val and q.val <= pointer.val):
                pointer = pointer.left
            else:
                pointer = pointer.right
