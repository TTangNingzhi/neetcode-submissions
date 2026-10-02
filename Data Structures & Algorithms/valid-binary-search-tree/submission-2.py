# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.last = float("-inf")
        self.valid = True

        def dfs(node: Optional[TreeNode]) -> None:
            if not self.valid:
                return
            if not node:
                return
            dfs(node.left)
            if node.val <= self.last:
                self.valid = False
                return
            self.last = node.val
            dfs(node.right)
        
        dfs(root)
        
        return self.valid