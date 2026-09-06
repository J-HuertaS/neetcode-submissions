# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def connectAndBuildTree(pre_start, pre_end, in_start, in_end):
            # caso base
            if pre_end < pre_start:
                return None

            # encontrar raiz
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # obtener mitad del arreglo inorder
            mid = inorder_map[root_val]
            left_size = mid - in_start

            root.left = connectAndBuildTree(pre_start+1,pre_start+left_size,in_start,mid-1)
            root.right = connectAndBuildTree(pre_start+left_size+1,pre_end,mid+1,in_end)

            return root
            
            
        return connectAndBuildTree(0,len(preorder)-1,0,len(inorder)-1)


        