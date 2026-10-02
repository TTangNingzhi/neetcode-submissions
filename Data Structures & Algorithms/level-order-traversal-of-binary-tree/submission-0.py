# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        res = []
        queue = deque()
        if root:
            queue.append((root, 0))
            prev_level = -1

        while queue:
            curr, level = queue.popleft()
            if level == prev_level:
                res[-1].append(curr.val)
            else:
                res.append([curr.val])
                prev_level = level
            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right:
                queue.append((curr.right, level + 1))
            
        return res