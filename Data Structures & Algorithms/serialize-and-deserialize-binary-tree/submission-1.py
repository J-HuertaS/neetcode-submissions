# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        output = []

        def dfs(root):
            output.append(str(root.val) if root else str(None))
            if root:
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return "$".join(output)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        values = data.split("$")

        iterator = iter(values)

        def dfs_inv():
            val = next(iterator,None)

            if val is None or val == "None":
                return None

            node = TreeNode(int(val))
            node.left = dfs_inv()
            node.right = dfs_inv()

            return node

        return dfs_inv()


