# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        output = [root.val]

        def sumBranch(node):
            # caso base
            if not node:
                return 0

            left = max(sumBranch(node.left),0)
            right = max(sumBranch(node.right),0)
            output[0] = max(output[0],left+right+node.val)

            return node.val + max(left,right)

        sumBranch(root)
        return output[0]



