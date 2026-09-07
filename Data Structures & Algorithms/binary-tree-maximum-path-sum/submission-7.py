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

            temp1 = sumBranch(node.left)
            temp2 = sumBranch(node.right)

            total = max(temp1+node.val,temp2+node.val,node.val)

            output[0] = max(total,output[0],temp1+temp2+node.val)
            
            return 0 if output[0] != float('inf') and total < 0 else total 

        sumBranch(root)
        return output[0]



