# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = [None]
        counter = [0]

        def DFSforK(node):
            if not node or output[0]:
                return

            DFSforK(node.left)
            counter[0] += 1
            if counter[0] == k:
                output[0] = node.val
                return
            DFSforK(node.right)

        DFSforK(root)
        return output[0]