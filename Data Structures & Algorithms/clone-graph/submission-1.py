"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        queue = deque()
        check = {}
        if node is None:
            return None
            
        queue.append(node)
        check[node.val] = Node(node.val)

        while queue:
            curr_node = queue.popleft()
            for n in curr_node.neighbors:
                if n.val not in check:
                    check[n.val] = Node(n.val)
                    queue.append(n)
                check[curr_node.val].neighbors.append(check[n.val])

        return check[1]
                

        