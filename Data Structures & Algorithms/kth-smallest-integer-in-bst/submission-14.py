# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    output = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.DFSforK(root,0,k)
        return self.output.val
    
    def DFSforK(self, node, counter, k):
        if node.left:
            counter = self.DFSforK(node.left,counter,k)

        counter += 1

        if counter == k:
            self.output = node

        if node.right:
            counter = self.DFSforK(node.right,counter,k)
        
        return counter