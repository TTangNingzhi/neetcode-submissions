# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        self.pre_i = 0

        def build(lo, hi):
            if lo > hi:
                return
            root = TreeNode(preorder[self.pre_i])
            pos_root = pos[root.val]
            self.pre_i += 1
            left = build(lo, pos_root - 1)
            right = build(pos_root + 1, hi)
            root.left = left
            root.right = right
            return root

        return build(0, len(inorder) - 1)