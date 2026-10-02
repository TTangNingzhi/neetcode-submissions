# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def depth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            depth_left = depth(root.left)
            depth_right = depth(root.right)
            self.ans = max(depth_left + depth_right, self.ans)
            return max(depth_left, depth_right) + 1
        
        depth(root)
        return self.ans