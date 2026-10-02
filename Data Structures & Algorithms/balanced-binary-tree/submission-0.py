# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True

        def height(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            height_left = height(root.left)
            height_right = height(root.right)
            if abs(height_left - height_right) > 1:
                self.ans = False
            return max(height_left, height_right) + 1
        
        height(root)
        return self.ans