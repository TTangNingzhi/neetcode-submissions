"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(n):
            if not n or n in old_to_new:
                return
            curr = Node(n.val)
            old_to_new[n] = curr
            for neighbor in n.neighbors:
                dfs(neighbor)
                curr.neighbors.append(old_to_new[neighbor])
                
        dfs(node)
        
        return old_to_new[node] if node else None
