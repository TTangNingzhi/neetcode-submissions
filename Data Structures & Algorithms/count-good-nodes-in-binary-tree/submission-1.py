# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 1
        
        def dfs(node, maximum):
            if node.left:
                if node.left.val >= maximum:
                    self.res += 1
                dfs(node.left, max(maximum, node.left.val))
            if node.right:
                if node.right.val >= maximum:
                    self.res += 1
                dfs(node.right, max(maximum, node.right.val))
        
        dfs(root, root.val)
        return self.res