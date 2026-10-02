# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p and q:
                return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            return p is None and q is None

        if isSameTree(root, subRoot):
            return True
        
        if root is None:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)