# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = None

        def dfs(node):
            if node is None:
                return False, False
            if self.lca is not None:
                return True, True
            found_p_l, found_q_l = dfs(node.left)
            found_p_r, found_q_r = dfs(node.right)
            found_p = found_p_l or found_p_r or node.val == p.val
            found_q = found_q_l or found_q_r or node.val == q.val
            if found_p and found_q and self.lca is None:
                self.lca = node
            return found_p, found_q
        
        dfs(root)
        return self.lca